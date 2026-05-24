#!/usr/bin/env python3
"""
debugging_tools.py — Debugging and analysis tools: regex, logs, errors, security, API docs

Usage:
  python debugging_tools.py regex "match email addresses"
  python debugging_tools.py regex "extract IPv4 addresses" --language javascript
  python debugging_tools.py analyze-log --file app.log
  python debugging_tools.py analyze-log --file app.log --last 100 --level error
  python debugging_tools.py decode-error "SegmentationFault 11 in libssl"
  python debugging_tools.py decode-error --file stacktrace.txt
  python debugging_tools.py scan-security --file mycode.py
  python debugging_tools.py scan-security --file mycode.py --focus owasp-top10
  python debugging_tools.py api-docs --file routes/users.py --format markdown
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"


def stream_chat(system_prompt: str, user_message: str) -> None:
    """Send a chat request to Ollama and stream the response to stdout."""
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "stream": True,
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=180)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        print(
            "Error: Cannot connect to Ollama at http://localhost:11434.\n"
            "Make sure Ollama is running: `ollama serve`",
            file=sys.stderr,
        )
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Error: Ollama returned HTTP {e.response.status_code}", file=sys.stderr)
        sys.exit(1)

    for line in response.iter_lines():
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        content = data.get("message", {}).get("content", "")
        if content:
            print(content, end="", flush=True)
        if data.get("done"):
            print()
            break


def read_file(path: str) -> str:
    """Read a file and return its content."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error reading file '{path}': {e}", file=sys.stderr)
        sys.exit(1)


def cmd_regex(args: argparse.Namespace) -> None:
    """Generate a regex pattern from a natural language description."""
    lang_notes = {
        "python": "Python `re` module. Use raw strings: r'pattern'",
        "javascript": "JavaScript RegExp. Note: use \\\\ for literal backslash in strings",
        "java": "Java `java.util.regex`. Double-escape backslashes: \\\\\\\\ for literal \\\\",
        "go": "Go `regexp` package (RE2 syntax — no lookaheads)",
        "bash": "GNU grep / sed compatible extended regex (ERE with -E flag)",
    }

    lang_note = lang_notes.get(args.language.lower(), args.language)

    system_prompt = (
        f"You are a regular expression expert specializing in {lang_note}. "
        "Generate correct, well-explained regex patterns. "
        "Always provide: "
        "1. The regex pattern itself (ready to use) "
        "2. Token-by-token explanation of what each part does "
        "3. Test cases — strings that SHOULD match and strings that should NOT "
        "4. Usage example in code "
        "5. Edge cases and limitations to be aware of "
        "Be precise about greedy vs. lazy quantifiers, anchoring, and Unicode handling. "
        "If the pattern is inherently imperfect (e.g., email validation), "
        "explain why and suggest the right tool for strict validation."
    )

    user_message = f"Generate a regex to: {args.description}\n\n"

    if args.anchored:
        user_message += "The pattern should match the ENTIRE string (add anchors ^ and $).\n"
    else:
        user_message += "The pattern should match a substring within larger text.\n"

    if args.multiline:
        user_message += "The pattern needs to work in multiline mode.\n"

    user_message += (
        f"\nFormat:\n"
        f"1. REGEX ({args.language.upper()}):\n   [the pattern]\n\n"
        f"2. EXPLAINED:\n   [token-by-token breakdown]\n\n"
        f"3. TEST CASES:\n   [should match] / [should NOT match]\n\n"
        f"4. {args.language.upper()} USAGE EXAMPLE:\n   [code snippet]\n\n"
        f"5. NOTES / LIMITATIONS"
    )

    print(f"\n--- Regex Generator ({args.language}) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_analyze_log(args: argparse.Namespace) -> None:
    """Analyze log files to surface errors, patterns, and root causes."""
    system_prompt = (
        "You are a systems reliability engineer specializing in log analysis and incident investigation. "
        "Analyze log files to: "
        "1. Identify incidents, outages, and anomalies "
        "2. Find error frequency patterns and error clusters "
        "3. Hypothesize root causes based on timing and error sequences "
        "4. Distinguish signal from noise (expected warnings vs. actual problems) "
        "5. Provide actionable investigation leads "
        "Always note the time window of any incident found. "
        "Group errors by type and show frequency counts. "
        "Identify cascading failure patterns (one error leading to another)."
    )

    log_text = read_file(args.file)

    # Take last N lines if requested
    if args.last:
        lines = log_text.splitlines()
        log_text = "\n".join(lines[-args.last:])
        line_note = f"(last {args.last} lines)"
    else:
        line_note = ""

    # Filter by level if requested
    if args.level and args.level != "all":
        filtered = [line for line in log_text.splitlines() if args.level.upper() in line.upper()]
        log_text = "\n".join(filtered)
        level_note = f"[{args.level.upper()} only]"
    else:
        level_note = ""

    user_message = (
        f"Analyze these logs {line_note} {level_note}:\n\n"
        f"```\n{log_text[:8000]}\n```\n\n"  # Truncate very large logs
        f"Provide:\n"
        f"1. INCIDENT SUMMARY (if any incidents occurred: severity, duration, impact)\n"
        f"2. ERROR FREQUENCY TABLE (| Error Type | Count | First Seen |)\n"
        f"3. ROOT CAUSE HYPOTHESIS (based on sequence and timing)\n"
        f"4. INVESTIGATION LEADS (specific things to check)\n"
        f"5. NORMAL ACTIVITY (confirm what is working correctly)"
    )

    if len(log_text) == 0:
        print("Error: No log content to analyze (file may be empty or level filter returned nothing).", file=sys.stderr)
        sys.exit(1)

    print(f"\n--- Log Analysis: {args.file} {line_note} {level_note} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_decode_error(args: argparse.Namespace) -> None:
    """Decode a cryptic error message or stack trace."""
    system_prompt = (
        "You are a debugging expert with deep knowledge of error types across all major languages, "
        "frameworks, operating systems, databases, and cloud platforms. "
        "When given an error message or stack trace: "
        "1. Explain in plain English WHAT the error means (not just restate it) "
        "2. Identify the ROOT CAUSE — often different from where the error surfaces "
        "3. Provide STEP-BY-STEP DEBUGGING guidance (ordered by likelihood) "
        "4. Provide FIXES ranked by impact and effort "
        "5. Note related issues to check that commonly occur alongside this error "
        "Be specific about language/framework/version-specific nuances."
    )

    # Get error from --file or positional argument
    if args.file:
        error_text = read_file(args.file)
    elif args.error_text:
        error_text = args.error_text
    elif not sys.stdin.isatty():
        error_text = sys.stdin.read().strip()
    else:
        print("Error: Provide error text as argument, via --file, or via stdin.", file=sys.stderr)
        sys.exit(1)

    if not error_text:
        print("Error: No error text to decode.", file=sys.stderr)
        sys.exit(1)

    user_message = f"Decode and explain this error:\n\n```\n{error_text}\n```\n"

    if args.context:
        user_message += f"\nContext: {args.context}\n"

    if args.language:
        user_message += f"\nLanguage/Runtime: {args.language}\n"

    user_message += (
        "\nProvide:\n"
        "1. PLAIN ENGLISH explanation (what is actually happening)\n"
        "2. ROOT CAUSE (what actually caused this, not just where it surfaced)\n"
        "3. DEBUGGING STEPS (numbered, ordered by likelihood of finding the cause)\n"
        "4. FIXES (ranked by impact — most effective fix first)\n"
        "5. RELATED ISSUES TO CHECK"
    )

    print("\n--- Error Message Decoder ---\n")
    stream_chat(system_prompt, user_message)


def cmd_scan_security(args: argparse.Namespace) -> None:
    """Scan source code for security vulnerabilities."""
    system_prompt = (
        "You are a security engineer and application security expert (AppSec). "
        "Perform thorough security code reviews using OWASP Top 10 and CWE classifications. "
        "Identify vulnerabilities at the semantic level — understand code flow, "
        "not just pattern matching. "
        "For each finding: "
        "1. Severity (CRITICAL/HIGH/MEDIUM/LOW) "
        "2. CWE ID and name "
        "3. Exact location (function/line reference) "
        "4. Clear explanation of the attack vector "
        "5. Proof of concept (show what malicious input could exploit this) "
        "6. Concrete fix with corrected code "
        "End with a risk summary and 'fix before deploy' list."
    )

    code = read_file(args.file)
    filename = args.file.split("/")[-1]

    user_message = f"Perform a security review of this code ({filename}):\n\n```\n{code}\n```\n\n"

    if args.focus == "owasp-top10":
        user_message += (
            "Focus on OWASP Top 10 vulnerabilities: "
            "A01 Broken Access Control, A02 Cryptographic Failures, A03 Injection, "
            "A04 Insecure Design, A05 Security Misconfiguration, A06 Vulnerable Components, "
            "A07 Auth Failures, A08 Integrity Failures, A09 Logging Failures, A10 SSRF.\n\n"
        )
    elif args.focus:
        user_message += f"Focus area: {args.focus}\n\n"

    user_message += (
        "Format:\n"
        "1. FINDINGS (each with: Severity, CWE, Location, Explanation, Proof of Concept, Fix)\n"
        "2. SUMMARY (counts by severity)\n"
        "3. FIX BEFORE DEPLOY list (critical and high severity only)"
    )

    print(f"\n--- Security Scan: {filename} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_api_docs(args: argparse.Namespace) -> None:
    """Generate API documentation from source code."""
    system_prompt = (
        "You are a technical writer and API documentation expert. "
        "Generate clear, complete API documentation from source code. "
        "For each endpoint or function document: "
        "- Purpose and behavior (including edge cases) "
        "- Authentication requirements "
        "- Parameters (path, query, body) with types, required/optional, defaults "
        "- Request body schema with field descriptions "
        "- Response schemas for all status codes "
        "- Error responses with codes and when they occur "
        "- Usage examples with realistic sample data "
        "Infer implicit behavior from the code (auth checks, defaults, error conditions)."
    )

    code = read_file(args.file)
    filename = args.file.split("/")[-1]

    format_instructions = {
        "markdown": "Format as Markdown with headers, tables for parameters, and code blocks for examples.",
        "openapi": "Format as OpenAPI 3.0 YAML suitable for Swagger UI.",
    }

    format_note = format_instructions.get(args.format, "Format as Markdown.")

    user_message = (
        f"Generate API documentation for this code ({filename}):\n\n"
        f"```\n{code}\n```\n\n"
        f"{format_note}\n"
    )

    if args.base_url:
        user_message += f"\nBase URL: {args.base_url}\n"

    user_message += (
        "\nFor each endpoint/function:\n"
        "1. Method, path, and one-sentence description\n"
        "2. Authentication requirements\n"
        "3. Parameters table\n"
        "4. Request body (if applicable)\n"
        "5. Response table (status codes, schemas)\n"
        "6. Example request and response"
    )

    print(f"\n--- API Documentation: {filename} ({args.format}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Debugging tools: regex, log analysis, error decoding, security scanning, API docs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- regex ---
    regex_p = subparsers.add_parser("regex", help="Generate a regex pattern from a description")
    regex_p.add_argument("description", help="What you want the regex to match")
    regex_p.add_argument(
        "--language",
        default="python",
        choices=["python", "javascript", "java", "go", "bash"],
        help="Target language for the regex",
    )
    regex_p.add_argument(
        "--anchored",
        action="store_true",
        help="Match entire string (add ^ and $ anchors)",
    )
    regex_p.add_argument(
        "--multiline",
        action="store_true",
        help="Pattern needs multiline support",
    )
    regex_p.set_defaults(func=cmd_regex)

    # --- analyze-log ---
    log_p = subparsers.add_parser("analyze-log", help="Analyze log files for errors and incidents")
    log_p.add_argument("--file", required=True, help="Path to log file")
    log_p.add_argument("--last", type=int, default=0, help="Analyze only the last N lines")
    log_p.add_argument(
        "--level",
        default="all",
        choices=["all", "error", "warn", "info"],
        help="Filter by log level",
    )
    log_p.set_defaults(func=cmd_analyze_log)

    # --- decode-error ---
    error_p = subparsers.add_parser("decode-error", help="Decode an error message or stack trace")
    error_p.add_argument(
        "error_text",
        nargs="?",
        default="",
        help="Error message or stack trace (or use --file or stdin)",
    )
    error_p.add_argument("--file", default=None, help="Path to file containing the stack trace")
    error_p.add_argument("--context", default="", help="Additional context (stack, framework, env)")
    error_p.add_argument("--language", default="", help="Language/runtime for more targeted advice")
    error_p.set_defaults(func=cmd_decode_error)

    # --- scan-security ---
    sec_p = subparsers.add_parser("scan-security", help="Scan code for security vulnerabilities")
    sec_p.add_argument("--file", required=True, help="Path to source code file to scan")
    sec_p.add_argument(
        "--focus",
        default="",
        help='Security focus, e.g. "owasp-top10", "injection", "authentication"',
    )
    sec_p.set_defaults(func=cmd_scan_security)

    # --- api-docs ---
    api_p = subparsers.add_parser("api-docs", help="Generate API documentation from source code")
    api_p.add_argument("--file", required=True, help="Path to source file with API handlers/routes")
    api_p.add_argument(
        "--format",
        default="markdown",
        choices=["markdown", "openapi"],
        help="Output format",
    )
    api_p.add_argument("--base-url", default="", help="Base URL to include in examples")
    api_p.set_defaults(func=cmd_api_docs)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
