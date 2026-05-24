#!/usr/bin/env python3
"""
health_and_fitness.py — Hermes Daily Life Examples
Covers: fitness-workout-planner, sleep-schedule-optimizer, morning-routine-planner

Usage:
    python health_and_fitness.py workout --goal "lose weight" --days 4
    python health_and_fitness.py workout --goal "build muscle" --days 5 --equipment "barbell,dumbbells"
    python health_and_fitness.py sleep --wake "7am" --bedtime-goal "8h"
    python health_and_fitness.py sleep --wake "6:30am" --bedtime-goal "7.5h" --issues "trouble falling asleep"
    python health_and_fitness.py morning-routine --duration 60
    python health_and_fitness.py morning-routine --duration 90 --goals "exercise,meditation,healthy breakfast"
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
# Sub-command handlers
# ---------------------------------------------------------------------------

def cmd_workout(args: argparse.Namespace) -> None:
    system = (
        "You are a certified personal trainer with expertise in evidence-based exercise programming. "
        "Create safe, effective workout plans that follow principles of progressive overload, "
        "adequate recovery, and exercise variety. "
        "Format each workout day with a header, warm-up, a markdown table of exercises "
        "(Exercise | Sets | Reps/Duration | Rest), and a cool-down note. "
        "End with a progressive overload strategy. Use markdown formatting throughout."
    )
    equipment_note = f" Available equipment: {args.equipment}." if args.equipment else " No equipment specified — assume bodyweight or common gym equipment."
    avoid_note = f" Avoid: {args.avoid}." if args.avoid else ""
    level_note = f" Fitness level: {args.level}." if args.level else " Assume intermediate fitness level."
    user_msg = (
        f"Create a {args.days}-day per week workout plan. Primary goal: {args.goal}.{equipment_note}{level_note}{avoid_note}\n"
        "Each session should be 45-60 minutes including warm-up and cool-down. "
        "Include a warm-up (5 min), main workout with sets/reps in a table, and cool-down (3 min). "
        "Name each day (e.g., Day 1 — Upper Body Push). "
        "End with a 'Progressive Overload Note' explaining how to advance week over week."
    )
    print(f"\n=== Fitness Workout Planner ===\nGoal: {args.goal} | Days: {args.days}/week\n")
    stream_chat(system, user_msg)


def cmd_sleep(args: argparse.Namespace) -> None:
    system = (
        "You are a sleep science specialist and behavioral health coach. "
        "Design evidence-based sleep schedules and wind-down routines using circadian rhythm principles, "
        "sleep hygiene research, and behavioral cue strategies. "
        "Be specific with times, not just durations. "
        "Format your response with: target schedule summary, a timed wind-down routine, "
        "and a numbered list of sleep hygiene tips. Use markdown formatting."
    )
    issues_note = f" Known sleep issues: {args.issues}." if args.issues else ""
    chronotype_note = f" Chronotype: {args.chronotype}." if args.chronotype else ""
    user_msg = (
        f"Design an optimized sleep schedule for someone who needs to wake up at {args.wake} "
        f"and wants {args.bedtime_goal} of quality sleep.{issues_note}{chronotype_note}\n"
        "Provide: (1) target bedtime and wake time, "
        "(2) a detailed wind-down routine starting 90 minutes before bed with specific times, "
        "(3) 5 evidence-based sleep hygiene tips tailored to the stated issues, "
        "(4) what to do if they can't fall asleep within 20 minutes."
    )
    print(f"\n=== Sleep Schedule Optimizer ===\nWake: {args.wake} | Sleep goal: {args.bedtime_goal}\n")
    stream_chat(system, user_msg)


def cmd_morning_routine(args: argparse.Namespace) -> None:
    system = (
        "You are a productivity coach and wellness expert specializing in morning routines. "
        "Design realistic, time-blocked morning routines that reduce friction and build momentum. "
        "Format the routine as a markdown table with columns: Time | Activity | Duration. "
        "After the table, include any relevant tips for reducing friction the night before, "
        "and 3 journal prompts if journaling is included. Use markdown formatting."
    )
    goals_note = f" Priority elements to include: {args.goals}." if args.goals else ""
    commute_note = f" Must be ready {args.commute} minutes before leaving." if args.commute else ""
    kids_note = " Include child-related tasks (school prep, packed lunches)." if args.kids else ""
    user_msg = (
        f"Create a {args.duration}-minute morning routine.{goals_note}{commute_note}{kids_note}\n"
        "Assume a wake time of 6:30 AM (adjust start times accordingly). "
        "Include a time-blocked table (Time | Activity | Duration). "
        "After the table, add: 'Night-Before Prep' tips to reduce morning friction, "
        "and 3 journal prompts if journaling is in the routine. "
        "Keep every activity specific and actionable."
    )
    print(f"\n=== Morning Routine Planner ===\nDuration: {args.duration} min\n")
    stream_chat(system, user_msg)


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Health & Fitness assistant powered by Hermes via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # workout
    p_workout = subparsers.add_parser("workout", help="Generate a personalized workout plan.")
    p_workout.add_argument("--goal", required=True, help='Fitness goal e.g. "lose weight", "build muscle", "improve endurance".')
    p_workout.add_argument("--days", type=int, default=4, help="Training days per week (default: 4).")
    p_workout.add_argument("--equipment", default="", help="Available equipment e.g. 'barbell,dumbbells,pull-up bar'.")
    p_workout.add_argument("--level", default="", help="Fitness level: beginner, intermediate, advanced.")
    p_workout.add_argument("--avoid", default="", help="Exercises or body parts to avoid e.g. 'lower back exercises'.")

    # sleep
    p_sleep = subparsers.add_parser("sleep", help="Optimize your sleep schedule.")
    p_sleep.add_argument("--wake", required=True, help="Required wake time e.g. '7am' or '6:30am'.")
    p_sleep.add_argument("--bedtime-goal", required=True, dest="bedtime_goal", help="Target sleep duration e.g. '8h' or '7.5h'.")
    p_sleep.add_argument("--issues", default="", help="Sleep issues e.g. 'trouble falling asleep', 'waking at 3am'.")
    p_sleep.add_argument("--chronotype", default="", help="Chronotype e.g. 'night-owl', 'early-bird'.")

    # morning-routine
    p_morning = subparsers.add_parser("morning-routine", help="Build a time-blocked morning routine.")
    p_morning.add_argument("--duration", type=int, default=60, help="Total routine duration in minutes (default: 60).")
    p_morning.add_argument("--goals", default="", help="Priority goals e.g. 'exercise,meditation,healthy breakfast'.")
    p_morning.add_argument("--commute", type=int, default=0, help="Minutes needed for commute/travel (optional).")
    p_morning.add_argument("--kids", action="store_true", help="Include child-related morning tasks.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "workout": cmd_workout,
        "sleep": cmd_sleep,
        "morning-routine": cmd_morning_routine,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
