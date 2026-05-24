#!/usr/bin/env python3
"""
meetings_and_docs.py — Meeting and documentation tools using Hermes via Ollama

Usage:
  python meetings_and_docs.py agenda --title "Sprint Kickoff" --duration 60 --attendees "PM, Dev, Design" --topics "goals, backlog, blockers"
  python meetings_and_docs.py summarize --file notes.txt
  cat transcript.txt | python meetings_and_docs.py summarize
  python meetings_and_docs.py report --title "Q2 Report" --audience executive --data "revenue up 12%, churn down 3%"
  python meetings_and_docs.py sop --process "Customer refund process" --department "Support" --tools "Stripe, Intercom"
  python meetings_and_docs.py onboarding --role "Frontend Engineer" --team "Product" --tools "Jira, GitHub, Figma"
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


def read_file_or_stdin(file_path: str | None) -> str:
    """Read content from a file or from stdin."""
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        except FileNotFoundError:
            print(f"Error: File not found: {file_path}", file=sys.stderr)
            sys.exit(1)
        except OSError as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)

    if not sys.stdin.isatty():
        return sys.stdin.read().strip()

    return ""


def cmd_agenda(args: argparse.Namespace) -> None:
    """Generate a meeting agenda."""
    system_prompt = (
        "You are an expert meeting facilitator and productivity consultant. "
        "Generate clear, time-boxed meeting agendas that keep meetings focused and productive. "
        "Assign realistic time allocations, put the most important items first, "
        "and assign owners to each agenda item based on attendee roles. "
        "Format with a clean header, a table of agenda items, and a stated meeting goal."
    )

    user_message = (
        f"Generate a meeting agenda with the following details:\n"
        f"- Meeting title: {args.title}\n"
        f"- Total duration: {args.duration} minutes\n"
        f"- Attendees/roles: {args.attendees}\n"
        f"- Topics to cover: {args.topics}\n"
    )

    if args.goal:
        user_message += f"- Meeting goal: {args.goal}\n"

    if args.recurring:
        user_message += f"- Recurring: {args.recurring}\n"

    user_message += (
        "\nFormat the output as:\n"
        "1. A header with meeting name, duration, and facilitator\n"
        "2. A table with columns: #, Topic, Owner, Time\n"
        "3. Pre-read links section (if applicable)\n"
        "4. One-sentence meeting goal"
    )

    print(f"\n--- Meeting Agenda: {args.title} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_summarize(args: argparse.Namespace) -> None:
    """Summarize meeting notes."""
    system_prompt = (
        "You are an expert at synthesizing meeting notes and transcripts into clear, actionable summaries. "
        "Extract: key decisions made, action items with owners and deadlines, and next steps. "
        "Format the summary with clear sections. "
        "Do not add information not present in the notes. "
        "If owners or deadlines are unclear, flag them as '[Owner: TBD]' or '[Due: TBD]'."
    )

    text = read_file_or_stdin(args.file)

    if not text:
        print(
            "Error: No meeting notes provided. Use --file or pipe text to stdin.",
            file=sys.stderr,
        )
        sys.exit(1)

    extract = args.extract or "all"

    user_message = (
        f"Summarize the following meeting notes.\n"
        f"Extract focus: {extract}\n\n"
        f"Meeting notes:\n---\n{text}\n---\n\n"
        f"Format the output with these sections:\n"
        f"1. Meeting Summary (date, attendees if mentioned)\n"
        f"2. Key Decisions\n"
        f"3. Action Items (as a table: Owner | Action | Due Date)\n"
        f"4. Next Meeting (if mentioned)"
    )

    if args.format == "slack":
        user_message += (
            "\n\nFormat for Slack: use *bold* for headers, no markdown tables, "
            "use bullet points, keep it under 300 words."
        )

    print("\n--- Meeting Notes Summary ---\n")
    stream_chat(system_prompt, user_message)


def cmd_report(args: argparse.Namespace) -> None:
    """Write a business report."""
    system_prompt = (
        "You are a professional business report writer. "
        "Transform data points and bullet notes into polished, well-structured business reports. "
        "Always include: executive summary, key metrics table (if data provided), analysis, "
        "and concrete recommendations. "
        "Adapt depth and vocabulary to the specified audience. "
        "Executive audience: brevity and strategic implications first. "
        "Technical audience: include methodology and detailed breakdowns."
    )

    user_message = (
        f"Write a business report with the following:\n"
        f"- Title: {args.title}\n"
        f"- Audience: {args.audience}\n"
        f"- Data and findings: {args.data}\n"
    )

    if args.tone:
        user_message += f"- Tone: {args.tone}\n"

    user_message += (
        "\nStructure:\n"
        "1. Executive Summary (2-3 sentences)\n"
        "2. Key Metrics (table format if data is numeric)\n"
        "3. Analysis (insights from the data)\n"
        "4. Recommendations (numbered, actionable)"
    )

    print(f"\n--- Business Report: {args.title} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_sop(args: argparse.Namespace) -> None:
    """Generate a Standard Operating Procedure document."""
    system_prompt = (
        "You are a process documentation specialist with expertise in writing clear, "
        "precise Standard Operating Procedures (SOPs). "
        "Write SOPs that are unambiguous, follow a numbered step structure, "
        "include decision points (if/else conditions), assign role ownership, "
        "and define success criteria. "
        "Use professional but plain language — procedures should be followable by someone new to the role."
    )

    user_message = (
        f"Write a Standard Operating Procedure (SOP) for the following:\n"
        f"- Process: {args.process}\n"
        f"- Department: {args.department}\n"
        f"- Tools used: {args.tools}\n"
    )

    if args.roles:
        user_message += f"- Roles involved: {args.roles}\n"

    user_message += (
        "\nFormat as a formal SOP document with:\n"
        "1. Header (title, department, version, date, owner)\n"
        "2. Purpose section\n"
        "3. Scope section\n"
        "4. Procedure (numbered steps with role assignments and decision points)\n"
        "5. Success Criteria\n"
        "6. Revision History table"
    )

    print(f"\n--- SOP: {args.process} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_onboarding(args: argparse.Namespace) -> None:
    """Generate an onboarding document."""
    system_prompt = (
        "You are an expert at creating role-specific onboarding documentation. "
        "Generate practical, structured onboarding guides that follow a realistic ramp pattern: "
        "Week 1 (orientation/context), Month 1 (learn and observe), "
        "Month 2 (ramp up with support), Month 3 (independent contribution). "
        "Include concrete checklists, resource links placeholders, and measurable goals. "
        "Adapt content to the specific role and team context."
    )

    user_message = (
        f"Create a comprehensive onboarding guide for a new hire:\n"
        f"- Role: {args.role}\n"
        f"- Team: {args.team}\n"
        f"- Tools to set up: {args.tools}\n"
    )

    if args.process:
        user_message += f"- Key processes: {args.process}\n"

    if args.goal:
        user_message += f"- 90-day goal: {args.goal}\n"

    user_message += (
        "\nFormat as:\n"
        "1. Onboarding Guide header (role, team)\n"
        "2. Week 1 schedule (day-by-day or key activities)\n"
        "3. Month 1 Goals (checklist format)\n"
        "4. Month 2 Goals (checklist format)\n"
        "5. Month 3 Goals (checklist format)\n"
        "6. Resources & Links section (with placeholders for actual URLs)"
    )

    print(f"\n--- Onboarding Guide: {args.role} ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Meeting and documentation tools with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- agenda ---
    agenda_p = subparsers.add_parser("agenda", help="Generate a meeting agenda")
    agenda_p.add_argument("--title", required=True, help="Meeting title")
    agenda_p.add_argument("--duration", type=int, default=60, help="Duration in minutes")
    agenda_p.add_argument("--attendees", required=True, help="Attendees and their roles")
    agenda_p.add_argument("--topics", required=True, help="Comma-separated list of topics to cover")
    agenda_p.add_argument("--goal", default="", help="One-sentence meeting goal")
    agenda_p.add_argument("--recurring", default="", help='Recurring cadence, e.g. "weekly"')
    agenda_p.set_defaults(func=cmd_agenda)

    # --- summarize ---
    summarize_p = subparsers.add_parser("summarize", help="Summarize meeting notes or transcript")
    summarize_p.add_argument("--file", default=None, help="Path to notes file")
    summarize_p.add_argument(
        "--extract",
        choices=["all", "decisions", "actions"],
        default="all",
        help="What to extract from the notes",
    )
    summarize_p.add_argument(
        "--format",
        choices=["markdown", "slack"],
        default="markdown",
        help="Output format",
    )
    summarize_p.set_defaults(func=cmd_summarize)

    # --- report ---
    report_p = subparsers.add_parser("report", help="Write a structured business report")
    report_p.add_argument("--title", required=True, help="Report title")
    report_p.add_argument(
        "--audience",
        default="executive",
        choices=["executive", "technical", "general"],
        help="Target audience",
    )
    report_p.add_argument("--data", required=True, help="Data points, metrics, and findings")
    report_p.add_argument(
        "--tone",
        default="formal",
        choices=["formal", "conversational"],
        help="Writing tone",
    )
    report_p.set_defaults(func=cmd_report)

    # --- sop ---
    sop_p = subparsers.add_parser("sop", help="Generate a Standard Operating Procedure")
    sop_p.add_argument("--process", required=True, help="Process name and description")
    sop_p.add_argument("--department", required=True, help="Department or team")
    sop_p.add_argument("--tools", default="", help="Tools and systems used in this process")
    sop_p.add_argument("--roles", default="", help="Roles involved (e.g., 'Manager, Accountant, CFO')")
    sop_p.set_defaults(func=cmd_sop)

    # --- onboarding ---
    onboarding_p = subparsers.add_parser("onboarding", help="Generate an onboarding guide")
    onboarding_p.add_argument("--role", required=True, help="Job role/title")
    onboarding_p.add_argument("--team", required=True, help="Team name")
    onboarding_p.add_argument("--tools", required=True, help="Comma-separated list of tools to set up")
    onboarding_p.add_argument("--process", default="", help="Key processes and workflows")
    onboarding_p.add_argument("--goal", default="", help="Expected achievement by 90 days")
    onboarding_p.set_defaults(func=cmd_onboarding)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
