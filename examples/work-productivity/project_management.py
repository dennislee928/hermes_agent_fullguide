#!/usr/bin/env python3
"""
project_management.py — Project management and planning tools using Hermes via Ollama

Usage:
  python project_management.py prioritize --tasks "Fix bug, Write report, Review PRs, Update docs"
  python project_management.py prioritize --file tasks.txt --framework moscow
  python project_management.py timeline --project "Build feedback portal" --team "2 engineers, 1 PM" --deadline "3 months"
  python project_management.py okr --team "Engineering" --quarter Q3 --themes "reliability, velocity"
  python project_management.py retro --sprint "Sprint 24" --went-well "shipped on time" --improve "deploys broke twice"
  python project_management.py outline --topic "Product roadmap 2025" --audience "Board" --slides 12 --goal "Get alignment"
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


def cmd_prioritize(args: argparse.Namespace) -> None:
    """Prioritize a task list using a decision framework."""
    system_prompt = (
        "You are a productivity expert and project manager specializing in task prioritization. "
        "Apply prioritization frameworks precisely and consistently. "
        "For Eisenhower Matrix: categorize by urgency (time-sensitive) and importance (strategic value). "
        "For MoSCoW: Must Have, Should Have, Could Have, Won't Have. "
        "Output clean, formatted tables for each category. "
        "For each task, briefly explain the categorization reasoning. "
        "Always end with a 'Start Here Today' recommendation."
    )

    # Get tasks from argument or file
    if args.file:
        tasks_text = read_file(args.file)
    elif args.tasks:
        tasks_text = args.tasks
    else:
        print("Error: Provide tasks via --tasks or --file.", file=sys.stderr)
        sys.exit(1)

    framework_instructions = {
        "eisenhower": (
            "Use the Eisenhower Matrix with four quadrants:\n"
            "- DO FIRST: Urgent + Important (do today)\n"
            "- SCHEDULE: Important, Not Urgent (plan time for these)\n"
            "- DELEGATE: Urgent, Not Important (hand off)\n"
            "- DROP/DEFER: Not Urgent, Not Important"
        ),
        "moscow": (
            "Use MoSCoW prioritization:\n"
            "- MUST HAVE: Critical, non-negotiable\n"
            "- SHOULD HAVE: Important but not critical\n"
            "- COULD HAVE: Nice to have\n"
            "- WON'T HAVE: Not now, explicitly deferred"
        ),
    }

    framework = args.framework.lower()
    framework_text = framework_instructions.get(framework, framework_instructions["eisenhower"])

    user_message = (
        f"Prioritize the following tasks using the {args.framework.upper()} framework.\n\n"
        f"{framework_text}\n\n"
        f"Tasks to prioritize:\n---\n{tasks_text}\n---\n\n"
        f"For each category, use a formatted table: | Task | Reason/Notes |\n"
        f"End with a 'Start Here Today' box listing the top 1-3 tasks to begin immediately."
    )

    if args.context:
        user_message = f"Context: {args.context}\n\n" + user_message

    print(f"\n--- Task Prioritization ({args.framework.upper()} Framework) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_timeline(args: argparse.Namespace) -> None:
    """Generate a project timeline with phases and milestones."""
    system_prompt = (
        "You are a senior project manager with expertise in realistic project planning. "
        "Create phased project timelines that identify dependencies, parallel tracks, "
        "and critical path items. "
        "Always include: phase names with week ranges, key activities per phase, "
        "milestone checkpoints, and a risk flags section. "
        "Be realistic about how long things take — don't compress timelines optimistically. "
        "Highlight the critical path and note where capacity constraints create schedule risk."
    )

    user_message = (
        f"Create a project timeline for:\n"
        f"- Project: {args.project}\n"
        f"- Team composition: {args.team}\n"
        f"- Deadline/duration: {args.deadline}\n"
    )

    if args.deliverables:
        user_message += f"- Key deliverables: {args.deliverables}\n"

    if args.constraints:
        user_message += f"- Constraints: {args.constraints}\n"

    if args.buffer:
        user_message += f"- Apply a {args.buffer}% buffer to all estimates\n"

    user_message += (
        "\nFormat as:\n"
        "1. Project header with total duration\n"
        "2. Phases with week ranges, key activities, and milestone for each phase\n"
        "3. Risk Flags section\n"
        "4. Critical Path note (which team member or dependency is the bottleneck)"
    )

    print(f"\n--- Project Timeline: {args.project} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_okr(args: argparse.Namespace) -> None:
    """Generate OKRs for a team and quarter."""
    system_prompt = (
        "You are an OKR expert and strategy consultant. "
        "Write well-formed OKRs following best practices: "
        "Objectives must be qualitative, aspirational, and memorable (not tasks). "
        "Key Results must be quantitative, specific, measurable, and time-bound. "
        "Key Results should NOT be tasks or activities — they are outcomes and metrics. "
        "Generate 2-4 objectives with 2-4 key results each. "
        "Each KR should have a clear baseline (current state) and target. "
        "End with an alignment note showing how these OKRs connect to company-level goals."
    )

    user_message = (
        f"Generate OKRs for:\n"
        f"- Team: {args.team}\n"
        f"- Quarter: {args.quarter}\n"
        f"- Strategic themes: {args.themes}\n"
    )

    if args.company_goal:
        user_message += f"- Company-level goal to align with: {args.company_goal}\n"

    if args.objectives:
        user_message += f"- Number of objectives to generate: {args.objectives}\n"

    user_message += (
        "\nFormat each OKR as:\n"
        "OBJECTIVE N: [Inspirational objective statement]\n"
        "  KR N.1: [Measurable key result with baseline -> target]\n"
        "  KR N.2: ...\n\n"
        "End with an Alignment Note explaining how these support company strategy."
    )

    print(f"\n--- OKRs: {args.team} Team | {args.quarter} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_retro(args: argparse.Namespace) -> None:
    """Facilitate a sprint retrospective."""
    system_prompt = (
        "You are an experienced Agile coach and retrospective facilitator. "
        "Transform raw retrospective input into structured, productive output. "
        "Identify patterns and root causes — don't just restate the problems. "
        "Frame everything constructively: problems become hypotheses to test, "
        "complaints become discussion questions. "
        "Action items must be specific, assigned, and achievable in one sprint. "
        "Check follow-through on previous actions if provided."
    )

    user_message = (
        f"Facilitate a retrospective for:\n"
        f"- Sprint/period: {args.sprint}\n"
        f"- Went well: {args.went_well}\n"
        f"- Needs improvement: {args.improve}\n"
    )

    if args.actions_last:
        user_message += f"- Actions from last retro (check follow-through): {args.actions_last}\n"

    if args.team_size:
        user_message += f"- Team size: {args.team_size} people\n"

    if args.format == "action-plan":
        user_message += "\nFocus on producing a clear action plan with owners and timelines."
    elif args.format == "discussion-only":
        user_message += "\nFocus on generating discussion prompts only — do not prescribe solutions."

    user_message += (
        "\nFormat as:\n"
        "1. WENT WELL — what to keep/reinforce and why\n"
        "2. NEEDS IMPROVEMENT — root cause hypothesis and discussion prompt for each issue\n"
        "3. ACTION ITEMS — table: # | Action | Owner | Due\n"
    )

    if args.actions_last:
        user_message += "4. FOLLOW-THROUGH CHECK — status on last retro's actions\n"

    print(f"\n--- Retrospective: {args.sprint} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_outline(args: argparse.Namespace) -> None:
    """Generate a presentation outline."""
    system_prompt = (
        "You are a presentation coach and communication strategist. "
        "Create compelling, narrative-driven presentation outlines. "
        "Every presentation should have: a hook opening, a clear problem/opportunity statement, "
        "evidence/body slides, and a strong call to action. "
        "For each slide provide: slide title, talking points (2-4 bullets), and a visual suggestion. "
        "Adapt structure to the goal: informing vs. persuading vs. training requires different narrative arcs. "
        "Keep audiences in mind — technical vs. executive vs. general audience needs different depth."
    )

    user_message = (
        f"Create a presentation outline:\n"
        f"- Topic: {args.topic}\n"
        f"- Audience: {args.audience}\n"
        f"- Number of slides: {args.slides}\n"
        f"- Goal: {args.goal}\n"
    )

    if args.key_points:
        user_message += f"- Key points to cover: {args.key_points}\n"

    if args.format == "pitch":
        user_message += "- Format: investor/executive pitch style\n"
    elif args.format == "workshop":
        user_message += "- Format: interactive workshop with activities\n"

    user_message += (
        f"\nGenerate exactly {args.slides} slides.\n"
        f"For each slide:\n"
        f"  Slide N — [Slide Title]\n"
        f"  Talking points: [2-4 bullet points]\n"
        f"  Visual suggestion: [what to show on this slide]\n\n"
        f"End with 3 presenter tips for this specific audience/topic combination."
    )

    print(f"\n--- Presentation Outline: {args.topic} ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Project management and planning tools with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- prioritize ---
    pri_p = subparsers.add_parser("prioritize", help="Prioritize a task list")
    pri_source = pri_p.add_mutually_exclusive_group()
    pri_source.add_argument("--tasks", help="Comma-separated task list")
    pri_source.add_argument("--file", help="File with one task per line")
    pri_p.add_argument(
        "--framework",
        default="eisenhower",
        choices=["eisenhower", "moscow"],
        help="Prioritization framework",
    )
    pri_p.add_argument("--context", default="", help="Additional context about urgency or deadlines")
    pri_p.set_defaults(func=cmd_prioritize)

    # --- timeline ---
    tl_p = subparsers.add_parser("timeline", help="Generate a project timeline")
    tl_p.add_argument("--project", required=True, help="Project name and brief description")
    tl_p.add_argument("--team", required=True, help="Team composition, e.g. '2 engineers, 1 PM'")
    tl_p.add_argument("--deadline", required=True, help="Target deadline or duration")
    tl_p.add_argument("--deliverables", default="", help="Key deliverables")
    tl_p.add_argument("--constraints", default="", help="Constraints (part-time, dependencies, etc.)")
    tl_p.add_argument("--buffer", type=int, default=0, help="Percentage buffer to add to estimates")
    tl_p.set_defaults(func=cmd_timeline)

    # --- okr ---
    okr_p = subparsers.add_parser("okr", help="Generate OKRs for a team")
    okr_p.add_argument("--team", required=True, help="Team name")
    okr_p.add_argument("--quarter", required=True, help="Quarter, e.g. Q3 or Q4-2024")
    okr_p.add_argument("--themes", required=True, help="Strategic themes or focus areas")
    okr_p.add_argument("--company-goal", default="", help="Company-level goal to align with")
    okr_p.add_argument("--objectives", type=int, default=3, help="Number of objectives to generate")
    okr_p.set_defaults(func=cmd_okr)

    # --- retro ---
    retro_p = subparsers.add_parser("retro", help="Facilitate a sprint retrospective")
    retro_p.add_argument("--sprint", required=True, help="Sprint or period name")
    retro_p.add_argument("--went-well", required=True, help="What went well (comma-separated or prose)")
    retro_p.add_argument("--improve", required=True, help="What needs improvement")
    retro_p.add_argument("--actions-last", default="", help="Actions from the previous retrospective")
    retro_p.add_argument("--team-size", type=int, default=0, help="Number of team members")
    retro_p.add_argument(
        "--format",
        default="action-plan",
        choices=["action-plan", "discussion-only"],
        help="Output format",
    )
    retro_p.set_defaults(func=cmd_retro)

    # --- outline ---
    outline_p = subparsers.add_parser("outline", help="Generate a presentation outline")
    outline_p.add_argument("--topic", required=True, help="Presentation topic")
    outline_p.add_argument("--audience", required=True, help="Target audience")
    outline_p.add_argument("--slides", type=int, default=10, help="Number of slides")
    outline_p.add_argument("--goal", required=True, help="Presentation goal (inform/persuade/train)")
    outline_p.add_argument("--key-points", default="", help="Must-cover key points")
    outline_p.add_argument(
        "--format",
        default="standard",
        choices=["standard", "pitch", "workshop"],
        help="Presentation format style",
    )
    outline_p.set_defaults(func=cmd_outline)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
