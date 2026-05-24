#!/usr/bin/env python3
"""
code_tools.py — Code review, bug explanation, refactoring, and complexity analysis using Hermes

Usage:
  python code_tools.py review --file mycode.py
  python code_tools.py review --file mycode.py --focus security
  python code_tools.py review --code "def divide(a, b): return a/b"
  python code_tools.py explain-bug --file buggy.py --error "ZeroDivisionError: division by zero"
  python code_tools.py explain-bug --code "def foo(): return 1/0" --error "ZeroDivisionError"
  python code_tools.py refactor --file messy.py --goal "add type hints and remove duplication"
  python code_tools.py refactor --code "def f(x): ..." --goal "apply early return pattern"
  python code_tools.py complexity --file mycode.py
  python code_tools.py complexity --file mycode.py --threshold 5
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


def get_code(args: argparse.Namespace) -> str:
    """Get code from --file or --code argument."""
    if hasattr(args, "file") and args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except OSError as e:
            print(f"Error reading file '{args.file}': {e}", file=sys.stderr)
            sys.exit(1)
    elif hasattr(args, "code") and args.code:
        return args.code
    else:
        if not sys.stdin.isatty():
            return sys.stdin.read()
        print("Error: Provide code via --file or --code.", file=sys.stderr)
        sys.exit(1)


def cmd_review(args: argparse.Namespace) -> None:
    """Perform a code review."""
    system_prompt = (
        "You are a senior software engineer performing a thorough code review. "
        "Identify issues in these categories: CRITICAL (bugs, security vulnerabilities, data loss risks), "
        "HIGH (performance problems, missing error handling, logic errors), "
        "MEDIUM (maintainability, code smells, missing tests), "
        "LOW (style, naming, documentation). "
        "For every issue: cite the line/function, explain the problem clearly, "
        "and provide a concrete fix with example code. "
        "End with a summary count by severity. "
        "Praise genuinely good patterns — a balanced review is more useful."
    )

    code = get_code(args)
    source = args.file if args.file else "inline code"

    user_message = f"Review the following code from '{source}':\n\n```\n{code}\n```\n"

    if args.focus:
        focus_instructions = {
            "security": "Focus specifically on security vulnerabilities (injection, auth, crypto, etc.).",
            "performance": "Focus specifically on performance bottlenecks, inefficient algorithms, and resource leaks.",
            "style": "Focus specifically on code style, naming, and readability.",
            "all": "Review all categories thoroughly.",
        }
        user_message += f"\nFocus: {focus_instructions.get(args.focus, args.focus)}\n"

    if args.language:
        user_message += f"\nLanguage: {args.language}\n"

    print(f"\n--- Code Review: {source} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_explain_bug(args: argparse.Namespace) -> None:
    """Explain a bug and provide a fix."""
    system_prompt = (
        "You are a debugging expert and educator. "
        "When given buggy code and/or an error message, explain: "
        "1. WHAT IS HAPPENING — in plain English, what the error actually means "
        "2. ROOT CAUSE — the exact line/logic that causes the problem "
        "3. STEP-BY-STEP TRACE — walk through code execution to show when/where it breaks "
        "4. THE FIX — corrected code with explanation "
        "5. RELATED BUGS TO CHECK — other similar issues to look for in the codebase "
        "Be precise about the difference between where an error surfaces vs. where it originates."
    )

    code = get_code(args)

    user_message = f"Explain this bug:\n\nCode:\n```\n{code}\n```\n"

    if args.error:
        user_message += f"\nError message / stack trace:\n```\n{args.error}\n```\n"

    if args.context:
        user_message += f"\nAdditional context: {args.context}\n"

    print("\n--- Bug Explanation ---\n")
    stream_chat(system_prompt, user_message)


def cmd_refactor(args: argparse.Namespace) -> None:
    """Refactor code according to a specified goal."""
    system_prompt = (
        "You are a senior software engineer specializing in code refactoring. "
        "Refactor code precisely according to the stated goal without changing behavior. "
        "Output: "
        "1. The complete refactored code (ready to use, not a diff) "
        "2. A numbered list of every change made and why "
        "3. A note confirming which behaviors are preserved "
        "Apply only the changes relevant to the stated goal — "
        "don't refactor things that weren't asked about."
    )

    code = get_code(args)
    source = args.file if args.file else "inline code"

    user_message = (
        f"Refactor the following code:\n\n"
        f"Goal: {args.goal}\n\n"
        f"Original code from '{source}':\n```\n{code}\n```\n\n"
        f"Provide:\n"
        f"1. Complete refactored code (the full file/function, ready to copy-paste)\n"
        f"2. Changes made (numbered list with brief explanation for each)\n"
        f"3. Behavior preservation note"
    )

    if args.language:
        user_message += f"\nLanguage: {args.language}\n"

    print(f"\n--- Refactor: {source} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_complexity(args: argparse.Namespace) -> None:
    """Analyze code complexity and suggest simplifications."""
    system_prompt = (
        "You are a software architect specializing in code quality and complexity reduction. "
        "Analyze code for complexity indicators: high cyclomatic complexity, deep nesting, "
        "long functions, large classes, excessive parameters, duplicated logic. "
        "For each high-complexity area: "
        "- Explain WHY it is complex (not just that it is) "
        "- Show a simplified version using appropriate patterns "
        "  (early return, decomposition, strategy pattern, etc.) "
        "Present a complexity leaderboard if multiple functions exist. "
        "Be specific about which refactoring pattern addresses each issue."
    )

    code = get_code(args)
    source = args.file if args.file else "inline code"
    threshold = args.threshold if hasattr(args, "threshold") and args.threshold else 5

    user_message = (
        f"Analyze the complexity of this code from '{source}':\n\n"
        f"```\n{code}\n```\n\n"
        f"Flag functions/methods with cyclomatic complexity above {threshold}.\n\n"
        f"For each complex area provide:\n"
        f"1. Complexity metrics (nesting depth, parameter count, cyclomatic complexity estimate)\n"
        f"2. Root cause of complexity (why is it hard to understand/test?)\n"
        f"3. Simplified refactored version with pattern name used\n\n"
        f"End with a summary table: | Function | Est. Complexity | Priority |"
    )

    print(f"\n--- Complexity Analysis: {source} ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Code review, bug explanation, refactoring, and complexity tools with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Shared arguments for commands that accept code input
    def add_code_input(p: argparse.ArgumentParser) -> None:
        group = p.add_mutually_exclusive_group()
        group.add_argument("--file", default=None, help="Path to source code file")
        group.add_argument("--code", default=None, help="Inline code snippet")

    # --- review ---
    review_p = subparsers.add_parser("review", help="Perform a code review")
    add_code_input(review_p)
    review_p.add_argument(
        "--focus",
        default="all",
        choices=["all", "security", "performance", "style"],
        help="Review focus area",
    )
    review_p.add_argument("--language", default="", help="Programming language (auto-detected if omitted)")
    review_p.set_defaults(func=cmd_review)

    # --- explain-bug ---
    bug_p = subparsers.add_parser("explain-bug", help="Explain a bug and provide a fix")
    add_code_input(bug_p)
    bug_p.add_argument("--error", default="", help="Error message or stack trace")
    bug_p.add_argument("--context", default="", help="Additional context about when the bug occurs")
    bug_p.set_defaults(func=cmd_explain_bug)

    # --- refactor ---
    refactor_p = subparsers.add_parser("refactor", help="Refactor code according to a goal")
    add_code_input(refactor_p)
    refactor_p.add_argument(
        "--goal",
        required=True,
        help='Refactoring goal, e.g. "add type hints" or "extract magic numbers to constants"',
    )
    refactor_p.add_argument("--language", default="", help="Programming language")
    refactor_p.set_defaults(func=cmd_refactor)

    # --- complexity ---
    complexity_p = subparsers.add_parser("complexity", help="Analyze code complexity")
    add_code_input(complexity_p)
    complexity_p.add_argument(
        "--threshold",
        type=int,
        default=5,
        help="Cyclomatic complexity threshold to flag (default: 5)",
    )
    complexity_p.set_defaults(func=cmd_complexity)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
