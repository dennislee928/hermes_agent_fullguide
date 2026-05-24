#!/usr/bin/env python3
"""
habits_and_budget.py — Hermes Daily Life Examples
Covers: personal-budget-advisor, habit-tracker-coach, book-movie-recommender

Usage:
    python habits_and_budget.py budget --income 4500 --expenses "rent:1400,food:600,transport:200"
    python habits_and_budget.py budget --income 3000 --goal "save 500/month for emergency fund"

    python habits_and_budget.py habits --habits "daily exercise, reading 20 min, no phone before bed" --duration 30
    python habits_and_budget.py habits --habit "meditate 10 min daily" --obstacle "forget and feel too tired"

    python habits_and_budget.py recommend books --liked "The Martian, Project Hail Mary" --mood "uplifting"
    python habits_and_budget.py recommend movies --liked "Inception, Interstellar" --time 2h
    python habits_and_budget.py recommend books --genre "historical fiction" --count 5
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
        with requests.post(OLLAMA_URL, json=payload, stream=True, timeout=120) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if not line:
                    continue
                try:
                    chunk = json.loads(line)
                except json.JSONDecodeError:
                    continue
                content = chunk.get("message", {}).get("content", "")
                if content:
                    print(content, end="", flush=True)
                if chunk.get("done"):
                    break
    except requests.exceptions.ConnectionError:
        print(
            "\n[ERROR] Could not connect to Ollama at http://localhost:11434.\n"
            "Make sure Ollama is running: `ollama serve`",
            file=sys.stderr,
        )
        sys.exit(1)
    except requests.exceptions.HTTPError as exc:
        print(f"\n[ERROR] HTTP error from Ollama: {exc}", file=sys.stderr)
        sys.exit(1)
    print()


# ---------------------------------------------------------------------------
# Helper: parse "key:value,key:value" expense strings
# ---------------------------------------------------------------------------

def parse_expenses(expense_str: str) -> dict:
    """Parse 'rent:1400,food:600' into {'rent': 1400, 'food': 600}."""
    expenses = {}
    if not expense_str:
        return expenses
    for item in expense_str.split(","):
        item = item.strip()
        if ":" in item:
            key, _, val = item.partition(":")
            try:
                expenses[key.strip()] = float(val.strip())
            except ValueError:
                pass
    return expenses


# ---------------------------------------------------------------------------
# Sub-command handlers
# ---------------------------------------------------------------------------

def cmd_budget(args: argparse.Namespace) -> None:
    system = (
        "You are a certified financial educator and budget coach. "
        "Analyze household budgets using proven frameworks (50/30/20, zero-based budgeting). "
        "Provide honest, non-judgmental, actionable advice. "
        "Compare spending to 50/30/20 targets in a markdown table. "
        "Identify the top 2-3 spending optimization opportunities. "
        "Provide a concrete step-by-step action plan to reach the stated goal. "
        "End with 3 'Quick Wins This Week' that take under 30 minutes to implement. "
        "Use markdown formatting. "
        "Note: This is educational guidance, not licensed financial advice."
    )

    # Build expense summary
    if args.expenses:
        expense_dict = parse_expenses(args.expenses)
        total_expenses = sum(expense_dict.values())
        expense_lines = "\n".join(
            f"  - {k.capitalize()}: ${v:,.0f}" for k, v in expense_dict.items()
        )
        expense_summary = f"Monthly expenses (total: ${total_expenses:,.0f}):\n{expense_lines}"
        surplus = args.income - total_expenses
        surplus_note = f"\nCurrent surplus: ${surplus:,.0f}/month"
    else:
        expense_summary = "No expense breakdown provided — give general budgeting guidance."
        surplus_note = ""

    goal_note = f"\nFinancial goal: {args.goal}" if args.goal else ""
    savings_note = f"\nCurrent monthly savings: ${args.savings:,.0f}" if args.savings else ""

    user_msg = (
        f"Monthly take-home income: ${args.income:,.0f}\n"
        f"{expense_summary}{surplus_note}{savings_note}{goal_note}\n\n"
        "Please provide:\n"
        "1. A table comparing current spending vs. 50/30/20 framework targets\n"
        "2. Analysis of the current financial situation\n"
        "3. Specific steps to reach the stated goal (with timelines if a goal was given)\n"
        "4. Top 2-3 spending optimization opportunities with estimated monthly savings\n"
        "5. Three 'Quick Wins This Week' (actions under 30 minutes each)\n"
        "6. A note about automating savings"
    )
    print(f"\n=== Personal Budget Advisor ===\nMonthly income: ${args.income:,}\n")
    stream_chat(system, user_msg)


def cmd_habits(args: argparse.Namespace) -> None:
    system = (
        "You are a behavioral science coach specializing in habit formation. "
        "You apply James Clear's atomic habits principles, BJ Fogg's tiny habits method, "
        "and identity-based behavior change strategies. "
        "For each habit: diagnose why past attempts failed, provide a minimum viable habit version, "
        "create an implementation intention ('When X happens, I will do Y'), "
        "suggest a habit stack (attach to existing behavior), and identify the keystone cue. "
        "Provide a 4-week progressive tracking table. "
        "End with the 'Never miss twice' rule and an identity-shift reframe. "
        "Use markdown formatting."
    )

    # Handle both --habits (multiple) and --habit (single)
    habits_list = args.habits if args.habits else args.habit
    obstacle_note = f"\nMy main obstacles: {args.obstacle}." if args.obstacle else ""
    duration_note = f"\nTimeframe: {args.duration} days." if args.duration else "\nTimeframe: 30 days."

    user_msg = (
        f"I want to build these habit(s): {habits_list}.{obstacle_note}{duration_note}\n\n"
        "I've tried and failed before. For each habit please provide:\n"
        "1. Why I've likely failed before (diagnosis)\n"
        "2. Minimum viable habit version (smaller than I think I need)\n"
        "3. Implementation intention in the format 'When [CUE], I will [ROUTINE]'\n"
        "4. Habit stack (attach to an existing daily behavior)\n"
        "5. Physical cue/trigger to set up in the environment\n\n"
        "Then provide a 4-week progressive tracking table showing weekly targets for each habit.\n"
        "End with: the 'Never miss twice' principle and an identity-shift statement for each habit."
    )
    print(f"\n=== Habit Tracker Coach ===\nHabits: {habits_list}\n")
    stream_chat(system, user_msg)


def cmd_recommend(args: argparse.Namespace) -> None:
    media_type = args.media_type  # 'books' or 'movies'
    system = (
        f"You are a passionate {media_type[:-1]} critic and recommendation specialist "
        f"with encyclopedic knowledge of {media_type} across all genres and eras. "
        "Go beyond surface-level genre matching — understand the thematic, stylistic, and "
        "emotional essence of what the user loved and find works with the same core appeal. "
        f"For each recommended {media_type[:-1]}: give the title and author/director, "
        "write a 2-3 sentence pitch explaining specifically why this person will love it "
        "(referencing their stated preferences), and note the mood/tone. "
        "Include a mix of well-known classics and hidden gems. "
        "Use markdown formatting with numbered recommendations."
    )

    liked_note = f"I loved: {args.liked}." if args.liked else ""
    genre_note = f"I enjoy the {args.genre} genre." if args.genre else ""
    mood_note = f" I'm in a {args.mood} mood." if args.mood else ""
    avoid_note = f" Please avoid: {args.avoid}." if args.avoid else ""
    time_note = f" I have about {args.time} to watch." if args.time and media_type == "movies" else ""
    count = args.count or 5

    user_msg = (
        f"{liked_note} {genre_note}{mood_note}{avoid_note}{time_note}\n"
        f"Recommend {count} {media_type} I'll probably love. "
        "For each, include: title, author/director/year, and a 2-3 sentence pitch "
        "explaining specifically why it matches my taste (reference what I told you I love). "
        "Note the mood/tone for each. "
        "Include a mix of well-known and lesser-known titles."
    )
    print(f"\n=== {media_type.title()} Recommender ===\n")
    stream_chat(system, user_msg)


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Habits & Budget assistant powered by Hermes via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # budget
    p_budget = subparsers.add_parser("budget", help="Get personalized budget analysis and advice.")
    p_budget.add_argument("--income", type=float, required=True, help="Monthly take-home income in USD.")
    p_budget.add_argument(
        "--expenses",
        default="",
        help='Expense breakdown as "category:amount,..." e.g. "rent:1400,food:600,transport:200".',
    )
    p_budget.add_argument("--goal", default="", help='Financial goal e.g. "save $500/month for emergency fund".')
    p_budget.add_argument("--savings", type=float, default=0, help="Current monthly savings amount.")

    # habits
    p_habits = subparsers.add_parser("habits", help="Build a science-based habit formation plan.")
    habits_group = p_habits.add_mutually_exclusive_group(required=True)
    habits_group.add_argument("--habits", default="", help="Comma-separated list of habits to build (multiple).")
    habits_group.add_argument("--habit", default="", help="Single habit to build.")
    p_habits.add_argument("--duration", type=int, default=30, help="Plan duration in days (default: 30).")
    p_habits.add_argument("--obstacle", default="", help="Main obstacle or reason past attempts failed.")

    # recommend
    p_rec = subparsers.add_parser("recommend", help="Get personalized book or movie recommendations.")
    p_rec.add_argument("media_type", choices=["books", "movies"], help="Type of media to recommend.")
    p_rec.add_argument("--liked", default="", help="Titles you loved e.g. 'The Martian, Project Hail Mary'.")
    p_rec.add_argument("--genre", default="", help="Preferred genre e.g. 'historical fiction', 'sci-fi'.")
    p_rec.add_argument("--mood", default="", help="Current mood e.g. 'uplifting', 'thought-provoking', 'light'.")
    p_rec.add_argument("--avoid", default="", help="Things to avoid e.g. 'slow pacing, sad endings'.")
    p_rec.add_argument("--time", default="", help="(Movies only) Available watch time e.g. '2h', '90 min'.")
    p_rec.add_argument("--count", type=int, default=5, help="Number of recommendations (default: 5).")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "budget": cmd_budget,
        "habits": cmd_habits,
        "recommend": cmd_recommend,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
