#!/usr/bin/env python3
"""
email_and_comms.py — Email Drafter and Tone Checker using Hermes via Ollama

Usage:
  python email_and_comms.py draft --to "client" --subject "project update" --tone professional
  python email_and_comms.py draft --to "manager" --subject "PTO request" --context "Need Friday off for appointment"
  python email_and_comms.py tone-check --file email.txt
  python email_and_comms.py tone-check --text "Per my last email, this was clearly stated."
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
        response = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120)
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
            print()  # Final newline
            break


def cmd_draft(args: argparse.Namespace) -> None:
    """Draft a professional email."""
    system_prompt = (
        "You are an expert business writing assistant specializing in professional email composition. "
        "Write clear, concise, and effective emails that achieve the sender's goal. "
        "Always include: a subject line, appropriate greeting, well-structured body, and sign-off. "
        "Adapt tone precisely as instructed. Never add filler or fluff. "
        "Do not fabricate facts — only use the information provided."
    )

    parts = [
        f"Write a professional email with the following details:",
        f"- Recipient/audience: {args.to}",
        f"- Subject: {args.subject}",
        f"- Tone: {args.tone}",
    ]

    if args.context:
        parts.append(f"- Context and key information: {args.context}")

    if args.length:
        parts.append(f"- Length preference: {args.length}")

    if args.sender:
        parts.append(f"- Sender name: {args.sender}")

    parts.append(
        "\nOutput the complete email starting with 'Subject:' on the first line, "
        "followed by a blank line, then the email body."
    )

    user_message = "\n".join(parts)
    print(f"\n--- Drafting email ({args.tone} tone) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_tone_check(args: argparse.Namespace) -> None:
    """Analyze tone of a piece of text and suggest improvements."""
    system_prompt = (
        "You are an expert in professional communication and tone analysis. "
        "Analyze text for tone, register, and communication effectiveness. "
        "Be specific: identify exact phrases that are problematic and explain why. "
        "Provide concrete rewrites for flagged phrases. "
        "Format your analysis clearly with sections: "
        "Detected Tone, Flagged Phrases (with rewrites), and a Revised Version."
    )

    # Read text from file or --text argument
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                text = f.read().strip()
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except OSError as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.text:
        text = args.text
    else:
        # Try reading from stdin
        if not sys.stdin.isatty():
            text = sys.stdin.read().strip()
        else:
            print(
                "Error: Provide text via --file, --text, or pipe to stdin.",
                file=sys.stderr,
            )
            sys.exit(1)

    if not text:
        print("Error: No text provided to analyze.", file=sys.stderr)
        sys.exit(1)

    intended = args.intended_tone or "professional and collaborative"

    user_message = (
        f"Analyze the tone of the following text.\n"
        f"Intended tone: {intended}\n\n"
        f"Text to analyze:\n---\n{text}\n---\n\n"
        f"Provide:\n"
        f"1. Detected tone (1-2 words)\n"
        f"2. Whether it matches the intended tone\n"
        f"3. Specific flagged phrases with explanations and rewrites\n"
        f"4. A fully revised version of the text in the intended tone"
    )

    print(f"\n--- Tone Analysis (intended: {intended}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Email drafting and tone checking with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- draft subcommand ---
    draft_parser = subparsers.add_parser(
        "draft", help="Draft a professional email"
    )
    draft_parser.add_argument(
        "--to",
        required=True,
        metavar="RECIPIENT",
        help='Recipient description, e.g. "manager", "client", "team"',
    )
    draft_parser.add_argument(
        "--subject", required=True, help="Email subject line or topic"
    )
    draft_parser.add_argument(
        "--tone",
        default="professional",
        choices=["professional", "formal", "friendly", "assertive", "empathetic", "concise"],
        help="Desired tone of the email (default: professional)",
    )
    draft_parser.add_argument(
        "--context",
        default="",
        help="Key facts, background, or specific points to include",
    )
    draft_parser.add_argument(
        "--length",
        default="",
        choices=["short", "medium", "long"],
        help="Preferred email length",
    )
    draft_parser.add_argument(
        "--sender", default="", help="Sender name for sign-off"
    )
    draft_parser.set_defaults(func=cmd_draft)

    # --- tone-check subcommand ---
    tone_parser = subparsers.add_parser(
        "tone-check", help="Analyze and improve the tone of a piece of text"
    )
    tone_source = tone_parser.add_mutually_exclusive_group()
    tone_source.add_argument("--file", help="Path to a text file to analyze")
    tone_source.add_argument("--text", help="Text to analyze (inline)")
    tone_parser.add_argument(
        "--intended-tone",
        default="professional and collaborative",
        help='The tone you were aiming for, e.g. "firm but friendly"',
    )
    tone_parser.set_defaults(func=cmd_tone_check)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
