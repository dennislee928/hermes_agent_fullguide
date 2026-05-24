#!/usr/bin/env python3
"""
mindfulness_tools.py — Hermes-powered mindfulness and wellness tools:
mental health journaling, guided meditation, hydration reminder,
ergonomics advisor, first aid guide, and workout form explainer.

IMPORTANT: All output is for informational and educational purposes only.
This is NOT medical advice. Always consult qualified healthcare professionals.

Usage:
  python mindfulness_tools.py journal --mood "anxious about upcoming job interview"
  python mindfulness_tools.py meditate --duration 10 --goal "reduce anxiety" --level beginner
  python mindfulness_tools.py hydration --weight 70 --unit kg --activity moderate
  python mindfulness_tools.py ergonomics --height "5ft 9in" --pain "lower back, neck"
  python mindfulness_tools.py first-aid "deep cut on hand"
  python mindfulness_tools.py form "barbell squat"
  python mindfulness_tools.py form "Romanian Deadlift" --level intermediate
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"

WELLNESS_DISCLAIMER = (
    "[Note: This content is for wellness and educational purposes only. "
    "It is not a substitute for professional medical, psychological, or therapeutic care. "
    "If you are experiencing a medical emergency, call your local emergency number immediately.]"
)


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
            "Error: Cannot connect to Ollama at http://localhost:11434. "
            "Make sure Ollama is running (`ollama serve`) and the model is pulled.",
            file=sys.stderr,
        )
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"Error: Ollama returned HTTP {e.response.status_code}: {e}", file=sys.stderr)
        sys.exit(1)

    for line in response.iter_lines():
        if not line:
            continue
        try:
            chunk = json.loads(line.decode("utf-8"))
        except json.JSONDecodeError:
            continue

        content = chunk.get("message", {}).get("content", "")
        if content:
            print(content, end="", flush=True)

        if chunk.get("done"):
            print()
            break


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# MENTAL HEALTH JOURNALING
# ---------------------------------------------------------------------------

def cmd_journal(args: argparse.Namespace) -> None:
    system = (
        "You are a compassionate journaling coach trained in evidence-based journaling practices "
        "drawn from cognitive behavioral therapy, mindfulness, gratitude research, and narrative "
        "therapy. You are NOT a therapist. You create supportive, non-judgmental journaling "
        "prompts tailored to the person's current emotional state. You match the emotional "
        "register of your prompts to the person's mood — prompts for anxiety differ from those "
        "for grief, frustration, or low motivation. You provide structure (timed prompts) without "
        "being prescriptive. You always encourage professional support for persistent distress."
    )

    goal_note = f"\nJournaling goal: {args.goal}" if args.goal else ""

    user_message = (
        f"Create a guided journaling session for someone who is currently: {args.mood}\n"
        f"{goal_note}\n\n"
        f"Provide:\n"
        f"1. A brief compassionate opening (2-3 sentences acknowledging the emotion)\n"
        f"2. A GROUNDING PROMPT (5 minutes) — help them arrive in the present moment\n"
        f"3. An EXPLORATION PROMPT (10 minutes) — help them examine specific situations, not just feelings\n"
        f"4. A REFRAME PROMPT (10 minutes) — introduce a perspective shift or self-compassion element\n"
        f"5. A PERSPECTIVE PROMPT (5 minutes) — find one small positive or anchor\n"
        f"6. A CLOSING REFLECTION (5 minutes) — set down the weight; transition forward\n"
        f"7. AFTER YOUR SESSION note (brief, warm)\n"
        f"8. A reminder that persistent distress warrants professional support\n"
    )

    print(f"\n{'='*60}")
    print("GUIDED JOURNALING SESSION")
    print(f"{'='*60}\n")
    print(WELLNESS_DISCLAIMER)
    print()
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# MINDFULNESS MEDITATION GUIDE
# ---------------------------------------------------------------------------

def cmd_meditate(args: argparse.Namespace) -> None:
    system = (
        "You are a meditation teacher trained in mindfulness-based stress reduction (MBSR), "
        "loving-kindness meditation, breath awareness, body scan, and visualization practices. "
        "You write guided meditation scripts that are read aloud. Your language is calm, paced, "
        "and non-prescriptive — you guide without commanding. You use '...' to indicate natural "
        "pauses (2-3 seconds each). You adjust depth and complexity to the practitioner's level. "
        "Scripts should feel natural and human when read aloud, not stilted or overly spiritual."
    )

    technique_note = ""
    if args.technique:
        technique_note = f"\nSpecific technique to use: {args.technique}"

    user_message = (
        f"Write a guided meditation script with these parameters:\n"
        f"Duration: {args.duration} minutes\n"
        f"Goal: {args.goal}\n"
        f"Level: {args.level}"
        f"{technique_note}\n\n"
        f"The script should:\n"
        f"- Be timed to approximately {args.duration} minutes when read at a slow, calm pace\n"
        f"- Include clear phase labels (e.g., [SETTLING — 1 min], [MAIN PRACTICE — 7 min])\n"
        f"- Use '...' for pause cues\n"
        f"- End with a gradual return to alertness and a brief intention-setting moment\n"
        f"- Be appropriate for {args.level} practitioners\n"
        f"- Include a brief note at the end about best practices for using this meditation\n"
    )

    print(f"\n{'='*60}")
    print(f"GUIDED MEDITATION: {args.goal}")
    print(f"Duration: {args.duration} min | Level: {args.level}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# HYDRATION REMINDER
# ---------------------------------------------------------------------------

def cmd_hydration(args: argparse.Namespace) -> None:
    system = (
        "You are a sports dietitian and hydration specialist. You create personalized daily "
        "hydration plans based on body weight, activity level, and climate. You calculate "
        "daily water intake targets using evidence-based formulas, provide a realistic hourly "
        "schedule linked to existing daily habits, and include practical tips for building "
        "consistent hydration habits. All recommendations align with current sports nutrition "
        "and health guidelines."
    )

    # Convert to kg if needed
    weight_in_unit = f"{args.weight} {args.unit}"
    climate_note = f"\nClimate: {args.climate}" if args.climate else ""
    medical_note = f"\nRelevant medical context: {args.medical}" if args.medical else ""
    goal_note = f"\nHydration goal: {args.goal}" if args.goal else ""

    activity_descriptions = {
        "sedentary": "little or no exercise, desk job",
        "light": "light exercise 1-3 days/week",
        "moderate": "moderate exercise 3-5 days/week",
        "active": "hard exercise 6-7 days/week",
        "very-active": "very hard exercise, physical job, or training twice per day",
    }
    activity_desc = activity_descriptions.get(args.activity, args.activity)

    user_message = (
        f"Create a personalized daily hydration plan for:\n"
        f"Body weight: {weight_in_unit}\n"
        f"Activity level: {args.activity} ({activity_desc})"
        f"{climate_note}"
        f"{goal_note}"
        f"{medical_note}\n\n"
        f"Provide:\n"
        f"1. DAILY TARGET (total liters, ounces, and cups) with calculation shown\n"
        f"2. DAILY SCHEDULE (time-anchored to typical daily routine: wake, meals, exercise, bedtime)\n"
        f"3. EXERCISE HYDRATION (before, during, and after workout amounts)\n"
        f"4. CLIMATE/SEASON ADJUSTMENTS (if applicable)\n"
        f"5. ELECTROLYTE GUIDANCE (when and why for this person's profile)\n"
        f"6. URINE COLOR CHECK (practical real-time indicator)\n"
        f"7. HABIT BUILDING TIPS (3-4 practical strategies to stay consistent)\n"
    )

    print(f"\n{'='*60}")
    print(f"PERSONALIZED HYDRATION PLAN")
    print(f"Weight: {weight_in_unit} | Activity: {args.activity}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# ERGONOMICS ADVISOR
# ---------------------------------------------------------------------------

def cmd_ergonomics(args: argparse.Namespace) -> None:
    system = (
        "You are a certified ergonomist and occupational health specialist. You assess workstation "
        "setups based on the user's physical profile, equipment, pain areas, and work duration. "
        "Your recommendations are specific and actionable — not 'adjust your chair' but 'set "
        "your chair so your elbows are at 90-110 degrees, which for your height means approximately "
        "X inches from the floor.' You always explain WHY each adjustment matters (which injury "
        "it prevents). You provide targeted stretches and micro-exercises for reported pain areas."
    )

    pain_note = f"\nReported pain areas: {args.pain}" if args.pain else ""
    duration_note = f"\nDaily work duration: {args.duration}" if args.duration else ""

    user_message = (
        f"Provide a comprehensive ergonomics assessment and setup guide for:\n"
        f"Height: {args.height}\n"
        f"Equipment/setup: {args.setup}"
        f"{pain_note}"
        f"{duration_note}\n\n"
        f"Provide:\n"
        f"1. PRIORITY ISSUES IDENTIFIED (what the setup/pain data suggests)\n"
        f"2. IMMEDIATE FIXES — HIGH IMPACT (most important changes, with specific measurements)\n"
        f"3. CHAIR & DESK SETUP (height, lumbar, monitor distance — specific to this person's height)\n"
        f"4. KEYBOARD & MOUSE PLACEMENT (angle, distance, wrist position)\n"
        f"5. TARGETED STRETCHES for each reported pain area (with frequency and technique)\n"
        f"6. BREAK SCHEDULE (specific timing and activity for each break type)\n"
        f"7. EQUIPMENT RECOMMENDATIONS (prioritized by impact and cost-effectiveness)\n"
    )

    print(f"\n{'='*60}")
    print("ERGONOMICS ADVISOR")
    print(f"Height: {args.height} | Setup: {args.setup}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# FIRST AID GUIDE
# ---------------------------------------------------------------------------

def cmd_first_aid(args: argparse.Namespace) -> None:
    system = (
        "You are a first aid instructor certified in advanced first aid and emergency response. "
        "You provide clear, correctly sequenced first aid instructions for injuries and medical "
        "situations. You ALWAYS state when to call emergency services FIRST (before any other "
        "action). You include 'WHAT NOT TO DO' for every situation because common first aid myths "
        "can cause serious harm. Your instructions are numbered and direct — written for someone "
        "who is stressed and needs to act quickly. You end with a clear disclaimer that first aid "
        "training from certified instructors is recommended."
    )

    situation = args.situation
    if args.file:
        situation = read_file(args.file)

    user_message = (
        f"Provide step-by-step first aid instructions for: {situation}\n\n"
        f"Structure your response as:\n"
        f"1. CALL EMERGENCY SERVICES IF (list conditions requiring immediate 911/999/112)\n"
        f"2. IMMEDIATE STEPS (numbered, start with the most critical action)\n"
        f"3. WHAT NOT TO DO (common harmful myths or mistakes for this situation)\n"
        f"4. MONITORING (what to watch for while waiting for help / during recovery)\n"
        f"5. WHEN TO SEEK MEDICAL ATTENTION (if not already an emergency)\n"
        f"6. DISCLAIMER (not a substitute for professional training; recommend first aid course)\n"
    )

    print(f"\n{'='*60}")
    print("FIRST AID GUIDE")
    print(f"Situation: {situation[:60]}{'...' if len(situation) > 60 else ''}")
    print(f"{'='*60}\n")
    print(WELLNESS_DISCLAIMER)
    print()
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# WORKOUT FORM EXPLAINER
# ---------------------------------------------------------------------------

def cmd_form(args: argparse.Namespace) -> None:
    system = (
        "You are an expert personal trainer and movement specialist with certifications in "
        "strength and conditioning (CSCS), corrective exercise, and sports performance. "
        "You explain exercise technique at multiple levels: the setup, the movement cues "
        "(what to focus on WHILE moving), common mistakes and how to feel correct technique "
        "in the body, the muscles worked and why proper form maximizes their engagement, "
        "beginner modifications, and progressions for advanced practitioners. "
        "Your coaching cues are specific and actionable — the phrases a great trainer would "
        "say during a set, not just anatomical descriptions."
    )

    exercise = args.exercise
    if args.file:
        exercise = read_file(args.file)

    level_note = f"\nExperience level: {args.level}" if args.level else ""
    injury_note = f"\nInjury history / notes: {args.note}" if args.note else ""
    equipment_note = f"\nAvailable equipment: {args.equipment}" if args.equipment else ""

    user_message = (
        f"Provide a comprehensive exercise form guide for: {exercise}"
        f"{level_note}"
        f"{equipment_note}"
        f"{injury_note}\n\n"
        f"Include:\n"
        f"1. PRIMARY MUSCLES and SECONDARY MUSCLES worked\n"
        f"2. SETUP (starting position, foot placement, grip, equipment setup)\n"
        f"3. THE MOVEMENT (phase by phase: eccentric/lowering and concentric/lifting)\n"
        f"4. KEY COACHING CUES (3-5 specific phrases that produce correct technique)\n"
        f"5. COMMON MISTAKES (3-4 mistakes with 'what it looks like' and 'how to fix it')\n"
        f"6. BREATHING PATTERN\n"
        f"7. BEGINNER MODIFICATION (simpler version to learn the pattern)\n"
        f"8. PROGRESSION (harder variation once the basics are mastered)\n"
        f"9. INJURY PREVENTION NOTE (joint(s) most at risk if form breaks down)\n"
    )

    print(f"\n{'='*60}")
    print(f"WORKOUT FORM GUIDE: {exercise}")
    if args.level:
        print(f"Level: {args.level}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered mindfulness and wellness tools (educational use only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- journal ---
    jn = subparsers.add_parser("journal", help="Generate guided journaling prompts")
    jn.add_argument("--mood", required=True, help="Current emotional state or situation")
    jn.add_argument("--goal", help="What you want to get out of the session (e.g. 'find clarity')")

    # --- meditate ---
    md = subparsers.add_parser("meditate", help="Generate a guided meditation script")
    md.add_argument("--duration", type=int, default=10, help="Duration in minutes (default: 10)")
    md.add_argument("--goal", default="reduce stress", help="Meditation goal (default: reduce stress)")
    md.add_argument(
        "--level",
        choices=["beginner", "intermediate", "experienced"],
        default="beginner",
        help="Practitioner level (default: beginner)",
    )
    md.add_argument("--technique", help="Specific technique (e.g. '4-7-8 breathing', 'body scan', 'loving-kindness')")

    # --- hydration ---
    hy = subparsers.add_parser("hydration", help="Create a personalized hydration plan")
    hy.add_argument("--weight", type=float, required=True, help="Body weight (number)")
    hy.add_argument("--unit", choices=["kg", "lbs"], default="kg", help="Weight unit (default: kg)")
    hy.add_argument(
        "--activity",
        choices=["sedentary", "light", "moderate", "active", "very-active"],
        default="moderate",
        help="Activity level (default: moderate)",
    )
    hy.add_argument(
        "--climate",
        choices=["cool", "temperate", "warm", "hot", "hot-humid"],
        help="Climate/environment",
    )
    hy.add_argument("--goal", help="Specific hydration goal (e.g. 'improve energy', 'support training')")
    hy.add_argument("--medical", help="Any relevant medical context (e.g. 'kidney stones history') — consult your doctor")

    # --- ergonomics ---
    eg = subparsers.add_parser("ergonomics", help="Get a personalized workstation ergonomics guide")
    eg.add_argument("--height", required=True, help="Your height (e.g. '5ft 9in' or '175cm')")
    eg.add_argument("--setup", required=True, help="Your workstation setup (e.g. 'laptop, external monitor, office chair')")
    eg.add_argument("--pain", help="Current pain areas (e.g. 'lower back, neck, wrist')")
    eg.add_argument("--duration", help="Daily work duration (e.g. '8 hours')")

    # --- first-aid ---
    fa = subparsers.add_parser("first-aid", help="Get step-by-step first aid instructions")
    fa_source = fa.add_mutually_exclusive_group()
    fa_source.add_argument("situation", nargs="?", help="Emergency or injury description")
    fa_source.add_argument("--file", help="Path to file describing the situation")

    # --- form ---
    fm = subparsers.add_parser("form", help="Get detailed workout form guidance")
    fm_source = fm.add_mutually_exclusive_group()
    fm_source.add_argument("exercise", nargs="?", help="Exercise name (e.g. 'barbell squat')")
    fm_source.add_argument("--file", help="Path to file with exercise description")
    fm.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        help="Experience level",
    )
    fm.add_argument("--equipment", help="Available equipment")
    fm.add_argument("--note", help="Any injury history or special notes")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "first-aid":
        if not hasattr(args, "situation") or (args.situation is None and not hasattr(args, "file")):
            print("Error: Provide situation description or use --file.", file=sys.stderr)
            sys.exit(1)

    if args.command == "form":
        if not hasattr(args, "exercise") or (args.exercise is None and not hasattr(args, "file")):
            print("Error: Provide exercise name or use --file.", file=sys.stderr)
            sys.exit(1)

    dispatch = {
        "journal": cmd_journal,
        "meditate": cmd_meditate,
        "hydration": cmd_hydration,
        "ergonomics": cmd_ergonomics,
        "first-aid": cmd_first_aid,
        "form": cmd_form,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
