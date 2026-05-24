#!/usr/bin/env python3
"""
devops_tools.py — DevOps tools: git commits, CI/CD, architecture, dependency analysis

Usage:
  git diff --staged | python devops_tools.py commit-message
  python devops_tools.py commit-message --diff changes.diff
  python devops_tools.py commit-message --diff changes.diff --type feat --scope auth
  python devops_tools.py cicd-advisor --stack "python fastapi pytest docker" --platform github-actions --envs "staging,production"
  python devops_tools.py architecture-advisor --description "monolith rails app, 50k users" --goal "scalability"
  python devops_tools.py analyze-deps --file requirements.txt --ecosystem python
  python devops_tools.py analyze-deps --file package.json --ecosystem node --licenses commercial
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
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"Error reading file '{path}': {e}", file=sys.stderr)
        sys.exit(1)


def cmd_commit_message(args: argparse.Namespace) -> None:
    """Generate a conventional commit message from a git diff."""
    system_prompt = (
        "You are an expert at writing clear, meaningful git commit messages. "
        "Follow the Conventional Commits specification: "
        "<type>(<scope>): <short summary>\n\n<body>\n\n<footer> "
        "Types: feat, fix, refactor, chore, docs, test, perf, ci, build, style "
        "Rules: "
        "- Subject line: max 72 chars, imperative mood ('add' not 'added') "
        "- Body: explain WHY, not just WHAT (the diff shows what changed) "
        "- Include body when the change is non-trivial "
        "- If the diff touches multiple concerns, suggest splitting into separate commits "
        "- Never include file paths in the subject — describe the behavior change "
        "Read the diff carefully to understand what the code actually does, not just what files changed."
    )

    # Get diff from --diff file or stdin
    if args.diff:
        diff_text = read_file(args.diff)
    elif not sys.stdin.isatty():
        diff_text = sys.stdin.read().strip()
    else:
        print(
            "Error: Provide diff via --diff file or pipe: git diff --staged | python devops_tools.py commit-message",
            file=sys.stderr,
        )
        sys.exit(1)

    if not diff_text:
        print("Error: Empty diff provided.", file=sys.stderr)
        sys.exit(1)

    user_message = f"Generate a conventional commit message for this git diff:\n\n```diff\n{diff_text}\n```\n"

    if args.type:
        user_message += f"\nCommit type override: {args.type}\n"

    if args.scope:
        user_message += f"\nScope override: {args.scope}\n"

    user_message += (
        "\nOutput:\n"
        "1. The commit message (subject + optional body)\n"
        "2. If the diff mixes concerns, suggest how to split it into separate commits"
    )

    print("\n--- Git Commit Message ---\n")
    stream_chat(system_prompt, user_message)


def cmd_cicd_advisor(args: argparse.Namespace) -> None:
    """Generate CI/CD pipeline configuration advice and YAML."""
    platform_labels = {
        "github-actions": "GitHub Actions",
        "gitlab-ci": "GitLab CI/CD",
        "circleci": "CircleCI",
        "jenkins": "Jenkins (Jenkinsfile)",
    }

    platform_label = platform_labels.get(args.platform, args.platform)

    system_prompt = (
        f"You are a DevOps engineer and CI/CD expert specializing in {platform_label}. "
        "Design complete, production-grade CI/CD pipelines. "
        "Always include: "
        "- Test stage (unit tests, linting) "
        "- Security scanning stage (SAST, secrets scanning) "
        "- Build and artifact stage "
        "- Environment-specific deploy stages "
        "- Proper caching to minimize build times "
        "- Secrets management (never hardcoded) "
        "- Manual approval gates for production deploys "
        "Generate actual pipeline YAML, not pseudocode. "
        "Explain non-obvious design decisions."
    )

    envs_list = [e.strip() for e in args.envs.split(",")]

    user_message = (
        f"Design a CI/CD pipeline for:\n"
        f"- Stack: {args.stack}\n"
        f"- Platform: {platform_label}\n"
        f"- Environments: {', '.join(envs_list)}\n"
    )

    if args.current_state:
        user_message += f"- Current deployment process: {args.current_state}\n"

    if args.cost_optimize:
        user_message += "- Optimize for cost: minimize unnecessary job runs and compute time\n"

    if args.security_focused:
        user_message += "- Security focus: include SBOM generation, SLSA provenance, secret scanning\n"

    user_message += (
        "\nProvide:\n"
        "1. Complete pipeline YAML file\n"
        "2. Required secrets/environment variables to configure\n"
        "3. Setup notes (any one-time configuration needed)\n"
        "4. Recommendations for improving the pipeline over time"
    )

    print(f"\n--- CI/CD Pipeline Advisor ({platform_label}) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_architecture_advisor(args: argparse.Namespace) -> None:
    """Provide architecture recommendations."""
    system_prompt = (
        "You are a principal software architect with experience across startups and enterprise systems. "
        "Provide pragmatic, context-appropriate architecture advice. "
        "Key principles: "
        "1. Recommend the SIMPLEST architecture that meets current needs — not future-proofed over-engineering "
        "2. Consider team size and operational burden in every recommendation "
        "3. Prioritize by impact/effort ratio "
        "4. Explicitly call out what NOT to do and why "
        "5. Give concrete next steps, not vague advice "
        "For performance problems: diagnose before prescribing. "
        "For reliability problems: consider failure modes and recovery time. "
        "Be honest about tradeoffs."
    )

    user_message = (
        f"Provide architecture recommendations for:\n"
        f"- Current architecture: {args.description}\n"
        f"- Goal: {args.goal}\n"
    )

    if args.team:
        user_message += f"- Team size: {args.team}\n"

    if args.scale:
        user_message += f"- Current scale: {args.scale}\n"

    if args.budget:
        user_message += f"- Budget constraint: {args.budget}\n"

    if args.mode == "greenfield":
        user_message += "\nThis is a greenfield project — recommend a starting architecture.\n"

    user_message += (
        "\nStructure as:\n"
        "1. Current State Assessment (risk level, critical issues)\n"
        "2. Recommended Improvements (prioritized by impact/effort, with rationale)\n"
        "3. What NOT To Do (common over-engineering traps to avoid)\n"
        "4. Estimated Impact (what improves if recommendations are followed)"
    )

    print("\n--- Architecture Advisor ---\n")
    stream_chat(system_prompt, user_message)


def cmd_analyze_deps(args: argparse.Namespace) -> None:
    """Analyze project dependencies for vulnerabilities, outdated packages, and license issues."""
    ecosystem_labels = {
        "python": "Python (pip/PyPI)",
        "node": "Node.js (npm/yarn)",
        "go": "Go (go.mod)",
        "ruby": "Ruby (Gemfile)",
        "java": "Java (Maven/Gradle)",
    }

    ecosystem_label = ecosystem_labels.get(args.ecosystem.lower(), args.ecosystem)

    system_prompt = (
        f"You are a software security and dependency management expert for {ecosystem_label} projects. "
        "Analyze dependency manifests to identify: "
        "1. Known security vulnerabilities (CVEs) — flag CRITICAL and HIGH severity "
        "2. Packages at end-of-life or no longer maintained "
        "3. Significantly outdated packages with important security fixes "
        "4. License compatibility issues (especially GPL for commercial products) "
        "5. Unnecessary or redundant dependencies "
        "Provide a prioritized upgrade plan with estimated effort and breaking change warnings. "
        "Be specific about CVE IDs and fix versions where known."
    )

    deps_text = read_file(args.file)

    user_message = (
        f"Analyze these {ecosystem_label} dependencies:\n\n"
        f"```\n{deps_text}\n```\n\n"
        f"Provide:\n"
        f"1. CRITICAL issues (security vulnerabilities requiring immediate action)\n"
        f"2. HIGH priority (EOL packages, major unpatched vulnerabilities)\n"
        f"3. MEDIUM priority (significantly outdated, performance regressions)\n"
        f"4. Upgrade plan (recommended order with breaking change notes)\n"
    )

    if args.licenses:
        user_message += (
            f"5. License audit (flag any {args.licenses}-incompatible licenses, "
            f"especially GPL/AGPL for commercial use)\n"
        )

    print(f"\n--- Dependency Analysis: {args.file} ({ecosystem_label}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="DevOps tools: git commits, CI/CD pipelines, architecture, dependencies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- commit-message ---
    commit_p = subparsers.add_parser(
        "commit-message", help="Generate a conventional commit message from a git diff"
    )
    commit_p.add_argument("--diff", default=None, help="Path to diff file (or pipe via stdin)")
    commit_p.add_argument(
        "--type",
        default="",
        choices=["feat", "fix", "refactor", "chore", "docs", "test", "perf", "ci", "build", "style", ""],
        help="Override inferred commit type",
    )
    commit_p.add_argument("--scope", default="", help="Commit scope override (e.g., auth, api, db)")
    commit_p.set_defaults(func=cmd_commit_message)

    # --- cicd-advisor ---
    cicd_p = subparsers.add_parser("cicd-advisor", help="Design a CI/CD pipeline")
    cicd_p.add_argument("--stack", required=True, help="Tech stack and tools")
    cicd_p.add_argument(
        "--platform",
        default="github-actions",
        choices=["github-actions", "gitlab-ci", "circleci", "jenkins"],
        help="CI/CD platform",
    )
    cicd_p.add_argument("--envs", default="staging,production", help="Deployment environments (comma-separated)")
    cicd_p.add_argument("--current-state", default="", help="Current deployment process description")
    cicd_p.add_argument("--cost-optimize", action="store_true", help="Optimize for CI cost reduction")
    cicd_p.add_argument("--security-focused", action="store_true", help="Include advanced security scanning")
    cicd_p.set_defaults(func=cmd_cicd_advisor)

    # --- architecture-advisor ---
    arch_p = subparsers.add_parser("architecture-advisor", help="Get architecture recommendations")
    arch_p.add_argument("--description", required=True, help="Current architecture description")
    arch_p.add_argument("--goal", required=True, help="Architectural goal (scalability, reliability, cost, etc.)")
    arch_p.add_argument("--team", default="", help="Team size, e.g. '4 engineers'")
    arch_p.add_argument("--scale", default="", help="Current scale, e.g. '100k users, 500 RPS'")
    arch_p.add_argument("--budget", default="", help="Budget constraints")
    arch_p.add_argument(
        "--mode",
        default="existing",
        choices=["existing", "greenfield"],
        help="Existing system review or new system design",
    )
    arch_p.set_defaults(func=cmd_architecture_advisor)

    # --- analyze-deps ---
    deps_p = subparsers.add_parser("analyze-deps", help="Analyze project dependencies")
    deps_p.add_argument("--file", required=True, help="Path to dependency manifest file")
    deps_p.add_argument(
        "--ecosystem",
        default="python",
        choices=["python", "node", "go", "ruby", "java"],
        help="Package ecosystem",
    )
    deps_p.add_argument(
        "--licenses",
        default="",
        choices=["commercial", "open-source", ""],
        help="License compatibility check for project type",
    )
    deps_p.set_defaults(func=cmd_analyze_deps)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
