#!/usr/bin/env python3
"""
code_generation.py — Code generation tools: unit tests, docstrings, shell scripts, Dockerfiles

Usage:
  python code_generation.py tests --file mymodule.py --framework pytest
  python code_generation.py tests --file mymodule.py --framework unittest --coverage edge-cases
  python code_generation.py docstrings --file mymodule.py --style google
  python code_generation.py docstrings --file mymodule.py --style numpy
  python code_generation.py shell --task "backup postgres db daily at 2am"
  python code_generation.py shell --task "deploy docker image to ECS with rollback" --safety strict
  python code_generation.py dockerfile --stack "python fastapi redis" --target production
  python code_generation.py dockerfile --stack "node express postgres" --target development --compose
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


def cmd_tests(args: argparse.Namespace) -> None:
    """Generate a unit test suite for a Python module."""
    system_prompt = (
        "You are a senior Python engineer specializing in test-driven development. "
        "Generate comprehensive unit tests that cover: "
        "1. Happy path (normal expected behavior) "
        "2. Edge cases (empty inputs, boundary values, zero, None, empty strings) "
        "3. Error conditions (exceptions that should be raised) "
        "4. Type boundary cases (ints vs floats, empty collections, single-element collections) "
        "Write idiomatic, readable tests. Use descriptive test method names that explain what is being tested. "
        "Group related tests in classes. "
        "Use fixtures and parametrize decorators where they reduce duplication. "
        "Note which external dependencies need mocking but don't mock unnecessarily."
    )

    code = read_file(args.file)
    filename = args.file.split("/")[-1]

    module_name = filename.replace(".py", "")

    user_message = (
        f"Generate a complete unit test suite for this Python module ({filename}):\n\n"
        f"```python\n{code}\n```\n\n"
        f"Requirements:\n"
        f"- Framework: {args.framework}\n"
        f"- Coverage focus: {args.coverage}\n"
        f"- Import the module as: from {module_name} import ...\n\n"
        f"Generate tests for ALL public functions and classes. "
        f"Include at minimum: 1 happy path test, 2+ edge case tests, and 1+ error condition test per function. "
        f"The tests should be runnable with: {args.framework} {filename.replace('.py', '_test.py')}"
    )

    if args.mock_deps:
        user_message += "\nUse unittest.mock to mock external dependencies (DB, HTTP, filesystem)."

    print(f"\n--- Unit Tests: {filename} ({args.framework}) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_docstrings(args: argparse.Namespace) -> None:
    """Add docstrings to all functions and classes in a Python file."""
    system_prompt = (
        "You are a Python documentation expert. "
        "Add accurate, complete docstrings to Python functions and classes. "
        "Infer parameter semantics from the code — don't just repeat variable names. "
        "Describe WHAT the function does (not HOW) and WHY parameters matter. "
        "Always document: raises, returns (including type and meaning), and side effects. "
        "Include usage examples for non-trivial functions. "
        "Output the complete file with docstrings added — do not omit any original code."
    )

    code = read_file(args.file)
    filename = args.file.split("/")[-1]

    style_formats = {
        "google": "Google style (Args:, Returns:, Raises:, Example:)",
        "numpy": "NumPy/SciPy style (Parameters, Returns, Raises sections with underlines)",
        "sphinx": "Sphinx/reStructuredText style (:param:, :type:, :returns:, :rtype:)",
    }

    style_desc = style_formats.get(args.style, args.style)

    user_message = (
        f"Add docstrings to all functions, methods, and classes in this file ({filename}).\n\n"
        f"Style: {style_desc}\n\n"
        f"```python\n{code}\n```\n\n"
        f"Return the COMPLETE file with all docstrings added. "
        f"Do not change any existing code — only add docstrings. "
        f"For the module itself, add a module-level docstring at the top describing the module's purpose."
    )

    if args.include_examples:
        user_message += "\nInclude usage examples in docstrings for all non-trivial functions."

    print(f"\n--- Docstrings: {filename} ({args.style} style) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_shell(args: argparse.Namespace) -> None:
    """Generate a production-quality shell script."""
    system_prompt = (
        "You are a DevOps engineer and shell scripting expert. "
        "Write production-quality Bash scripts that are: "
        "- Defensive: always start with `set -euo pipefail` "
        "- Self-documenting: include usage comments and section headers "
        "- Robust: validate inputs, handle missing arguments, catch errors "
        "- Logged: include timestamp-based logging function "
        "- Safe: use trap for cleanup on exit/error "
        "- Maintainable: use variables for all configurable values (never hardcode paths/values) "
        "Write complete, runnable scripts — not skeleton templates."
    )

    user_message = f"Write a complete, production-quality Bash script for this task:\n\n{args.task}\n\n"

    if args.safety == "strict":
        user_message += (
            "Safety requirements:\n"
            "- Include a --dry-run mode that prints actions without executing them\n"
            "- Include rollback logic where applicable\n"
            "- Validate all prerequisites (required tools, environment variables, permissions) before starting\n"
        )

    if args.shell != "bash":
        user_message += f"\nWrite for {args.shell} shell instead of bash.\n"

    user_message += (
        "\nInclude:\n"
        "1. Shebang line and `set -euo pipefail`\n"
        "2. Usage comment block\n"
        "3. Configuration variables section\n"
        "4. Logging function\n"
        "5. Main logic with clear section comments\n"
        "6. Error handling with meaningful messages"
    )

    print(f"\n--- Shell Script Generator ---\n")
    stream_chat(system_prompt, user_message)


def cmd_dockerfile(args: argparse.Namespace) -> None:
    """Generate a Dockerfile (and optionally docker-compose.yml)."""
    system_prompt = (
        "You are a container and DevOps expert specializing in production Docker configurations. "
        "Generate Dockerfiles that follow best practices: "
        "- Multi-stage builds to minimize final image size "
        "- Non-root user for security "
        "- Proper layer caching (copy dependency files before source code) "
        "- Minimal base images (alpine where appropriate) "
        "- STOPSIGNAL and graceful shutdown support "
        "- No secrets or credentials baked into the image "
        "Also generate a .dockerignore recommendation. "
        "For development targets: include hot-reload, dev dependencies, and bind mounts."
    )

    user_message = (
        f"Generate a Dockerfile for the following stack:\n"
        f"- Stack: {args.stack}\n"
        f"- Target: {args.target}\n\n"
    )

    if args.port:
        user_message += f"- Exposed port: {args.port}\n"

    if args.secrets:
        user_message += "- Include guidance for injecting secrets at runtime (not baked in).\n"

    user_message += (
        "\nProvide:\n"
        "1. The complete Dockerfile with comments\n"
        "2. Recommended .dockerignore contents\n"
        "3. Build and run commands\n"
        "4. Key decisions explained (why multi-stage, why this base image, etc.)"
    )

    if args.compose:
        user_message += (
            "\n5. A docker-compose.yml for local development "
            "with all services in the stack, volume mounts, and environment variable placeholders."
        )

    print(f"\n--- Dockerfile Generator: {args.stack} ({args.target}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Code generation tools: tests, docstrings, shell scripts, Dockerfiles",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- tests ---
    tests_p = subparsers.add_parser("tests", help="Generate a unit test suite")
    tests_p.add_argument("--file", required=True, help="Path to Python module to test")
    tests_p.add_argument(
        "--framework",
        default="pytest",
        choices=["pytest", "unittest"],
        help="Test framework to use",
    )
    tests_p.add_argument(
        "--coverage",
        default="comprehensive",
        choices=["comprehensive", "edge-cases", "happy-path"],
        help="Coverage focus",
    )
    tests_p.add_argument(
        "--mock-deps",
        action="store_true",
        help="Include mocks for external dependencies",
    )
    tests_p.set_defaults(func=cmd_tests)

    # --- docstrings ---
    docs_p = subparsers.add_parser("docstrings", help="Add docstrings to a Python file")
    docs_p.add_argument("--file", required=True, help="Path to Python file")
    docs_p.add_argument(
        "--style",
        default="google",
        choices=["google", "numpy", "sphinx"],
        help="Docstring style",
    )
    docs_p.add_argument(
        "--include-examples",
        action="store_true",
        help="Include usage examples in docstrings",
    )
    docs_p.set_defaults(func=cmd_docstrings)

    # --- shell ---
    shell_p = subparsers.add_parser("shell", help="Generate a production shell script")
    shell_p.add_argument("--task", required=True, help="Description of what the script should do")
    shell_p.add_argument(
        "--safety",
        default="standard",
        choices=["standard", "strict"],
        help="Safety level: strict adds dry-run mode and rollback",
    )
    shell_p.add_argument(
        "--shell",
        default="bash",
        choices=["bash", "zsh", "sh"],
        help="Shell to target",
    )
    shell_p.set_defaults(func=cmd_shell)

    # --- dockerfile ---
    docker_p = subparsers.add_parser("dockerfile", help="Generate a Dockerfile")
    docker_p.add_argument(
        "--stack",
        required=True,
        help='Tech stack description, e.g. "python fastapi redis"',
    )
    docker_p.add_argument(
        "--target",
        default="production",
        choices=["production", "development"],
        help="Build target",
    )
    docker_p.add_argument("--port", default="", help="Port to expose")
    docker_p.add_argument(
        "--compose",
        action="store_true",
        help="Also generate docker-compose.yml",
    )
    docker_p.add_argument(
        "--secrets",
        action="store_true",
        help="Include runtime secret injection guidance",
    )
    docker_p.set_defaults(func=cmd_dockerfile)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
