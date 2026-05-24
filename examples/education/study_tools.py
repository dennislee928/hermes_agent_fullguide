#!/usr/bin/env python3
"""
study_tools.py — Hermes-powered study tools: flashcards, quiz creator,
study plan maker, and exam strategy advisor.

Usage:
  python study_tools.py flashcards --topic "French Revolution" --count 20
  python study_tools.py quiz --topic "Python basics" --count 10 --difficulty medium
  python study_tools.py study-plan --subject "Calculus" --exam-date "2024-03-15" --hours-per-day 2
  python study_tools.py exam-strategy --exam "AP Calculus AB" --time "3 hours" --format "multiple choice + free response"
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
            print()  # final newline
            break


# ---------------------------------------------------------------------------
# FLASHCARDS
# ---------------------------------------------------------------------------

def cmd_flashcards(args: argparse.Namespace) -> None:
    system = (
        "You are an expert educator and spaced-repetition specialist. "
        "Your job is to create high-quality study flashcards that test conceptual understanding, "
        "not just rote memorization. Each flashcard must be clearly formatted with 'Q:' and 'A:' "
        "labels. Make questions specific and testable. Answers should be complete but concise. "
        "Number each flashcard starting from FLASHCARD 1."
    )

    parts = [f"Generate {args.count} study flashcards on the topic: {args.topic}."]

    if args.difficulty:
        difficulty_guidance = {
            "easy": "Focus on definitions, basic facts, and key dates.",
            "medium": "Mix definitions with conceptual questions requiring brief explanation.",
            "hard": "Focus on analysis, comparison, cause-and-effect, and application questions.",
        }
        parts.append(difficulty_guidance.get(args.difficulty, ""))

    if args.text:
        parts.append(f"\nBase the flashcards strictly on this source text:\n\n{args.text}")
    elif hasattr(args, "file") and args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                source_text = f.read()
            parts.append(f"\nBase the flashcards strictly on this source text:\n\n{source_text}")
        except FileNotFoundError:
            print(f"Error: File not found: {args.file}", file=sys.stderr)
            sys.exit(1)

    parts.append(
        "\nFormat each flashcard exactly as:\n"
        "FLASHCARD N\n"
        "Q: [question]\n"
        "A: [answer]\n"
    )

    user_message = "\n".join(parts)
    print(f"\n{'='*60}")
    print(f"FLASHCARDS: {args.topic} ({args.count} cards)")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# QUIZ
# ---------------------------------------------------------------------------

def cmd_quiz(args: argparse.Namespace) -> None:
    system = (
        "You are a professional test designer with expertise in educational assessment. "
        "Create well-crafted quiz questions that accurately measure student understanding. "
        "For multiple-choice questions, write plausible distractors that represent common "
        "misconceptions — not obviously wrong answers. Always include the correct answer "
        "marked with [CORRECT] and a brief explanation of why each wrong answer is incorrect. "
        "Number questions starting from QUESTION 1."
    )

    fmt = args.format if args.format else "multiple-choice"
    difficulty_desc = {
        "easy": "introductory recall and basic comprehension",
        "medium": "application and analysis requiring some depth",
        "hard": "synthesis, evaluation, and nuanced understanding",
    }.get(args.difficulty, "mixed difficulty")

    user_message = (
        f"Create a {fmt} quiz on the topic: '{args.topic}'.\n"
        f"Number of questions: {args.count}\n"
        f"Difficulty level: {args.difficulty} ({difficulty_desc})\n\n"
        f"For each question include:\n"
        f"- The question stem\n"
        f"- Answer choices A-D (for multiple choice)\n"
        f"- Mark the correct answer with [CORRECT]\n"
        f"- A 1-2 sentence explanation of why the correct answer is right "
        f"and briefly why the wrong answers are incorrect\n"
    )

    print(f"\n{'='*60}")
    print(f"QUIZ: {args.topic}")
    print(f"Questions: {args.count} | Difficulty: {args.difficulty} | Format: {fmt}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# STUDY PLAN
# ---------------------------------------------------------------------------

def cmd_study_plan(args: argparse.Namespace) -> None:
    system = (
        "You are an academic coach and study strategist. Create detailed, realistic study plans "
        "that apply spaced repetition and interleaving principles. Plans should break subjects "
        "into manageable daily chunks, include review sessions, and build in buffer time. "
        "Always sequence topics from foundational to advanced within each subject. "
        "Be specific about what to study each day — not just 'study Chapter 3' but 'Chapter 3: "
        "Newton's laws of motion, focus on free-body diagrams and Newton's second law problems'."
    )

    topics_section = ""
    if args.topics:
        topics_section = f"\nSubject areas to cover: {args.topics}"

    breaks_section = (
        "\nIncorporate rest days (at least 1 per week) and buffer days before the exam."
        if args.include_breaks
        else ""
    )

    user_message = (
        f"Create a detailed day-by-day study plan for:\n"
        f"Subject: {args.subject}\n"
        f"Exam date: {args.exam_date}\n"
        f"Available study time: {args.hours_per_day} hours per day\n"
        f"{topics_section}"
        f"{breaks_section}\n\n"
        f"Include:\n"
        f"1. Total days and hours available\n"
        f"2. Week-by-week topic breakdown\n"
        f"3. Specific daily tasks (day, date, topic, activity)\n"
        f"4. Review sessions (spaced repetition)\n"
        f"5. Final week strategy\n"
        f"6. Exam day preparation advice\n"
    )

    print(f"\n{'='*60}")
    print(f"STUDY PLAN: {args.subject}")
    print(f"Exam: {args.exam_date} | {args.hours_per_day} hrs/day")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# EXAM STRATEGY
# ---------------------------------------------------------------------------

def cmd_exam_strategy(args: argparse.Namespace) -> None:
    system = (
        "You are a high-performance academic coach who has helped students excel on standardized "
        "tests, university exams, and professional certifications. You provide specific, tactical "
        "exam strategies tailored to the exact exam format and subject matter. Your advice is "
        "concrete and actionable — not generic. You address time management with specific numbers, "
        "question-attack strategies, stress management techniques, and last-minute preparation."
    )

    weak_areas_section = ""
    if args.weak_areas:
        weak_areas_section = f"\nStudent's identified weak areas: {args.weak_areas}"

    user_message = (
        f"Create a comprehensive exam strategy for:\n"
        f"Exam: {args.exam}\n"
        f"Duration: {args.time}\n"
        f"Format: {args.format}\n"
        f"{weak_areas_section}\n\n"
        f"Include:\n"
        f"1. Time management strategy with specific time allocations per section/question type\n"
        f"2. Question-attack order and triage strategy\n"
        f"3. Format-specific tactics for {args.format}\n"
        f"4. Handling of weak areas (if specified) with specific techniques\n"
        f"5. Stress management for during the exam\n"
        f"6. Night-before preparation checklist\n"
        f"7. Morning-of routine\n"
    )

    print(f"\n{'='*60}")
    print(f"EXAM STRATEGY: {args.exam}")
    print(f"Duration: {args.time} | Format: {args.format}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered study tools: flashcards, quizzes, study plans, exam strategy.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- flashcards ---
    fc = subparsers.add_parser("flashcards", help="Generate study flashcards")
    fc.add_argument("--topic", required=True, help="Topic for the flashcards")
    fc.add_argument("--count", type=int, default=10, help="Number of flashcards to generate (default: 10)")
    fc.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="medium",
        help="Question difficulty level (default: medium)",
    )
    fc.add_argument("--text", help="Source text to base flashcards on (inline)")
    fc.add_argument("--file", help="Path to a text file to base flashcards on")

    # --- quiz ---
    qz = subparsers.add_parser("quiz", help="Create a quiz")
    qz.add_argument("--topic", required=True, help="Topic for the quiz")
    qz.add_argument("--count", type=int, default=5, help="Number of questions (default: 5)")
    qz.add_argument(
        "--difficulty",
        choices=["easy", "medium", "hard"],
        default="medium",
        help="Difficulty level (default: medium)",
    )
    qz.add_argument(
        "--format",
        choices=["multiple-choice", "true-false", "short-answer"],
        default="multiple-choice",
        help="Question format (default: multiple-choice)",
    )

    # --- study-plan ---
    sp = subparsers.add_parser("study-plan", help="Generate a study plan")
    sp.add_argument("--subject", required=True, help="Subject to study")
    sp.add_argument("--exam-date", required=True, help="Exam date (e.g. 2024-03-15)")
    sp.add_argument("--hours-per-day", type=float, default=2.0, help="Study hours available per day (default: 2)")
    sp.add_argument("--topics", help="Comma-separated list of topics to cover")
    sp.add_argument(
        "--include-breaks",
        action="store_true",
        help="Include rest days and buffer days in the plan",
    )

    # --- exam-strategy ---
    es = subparsers.add_parser("exam-strategy", help="Get a tailored exam strategy")
    es.add_argument("--exam", required=True, help="Name of the exam (e.g. 'AP Calculus AB')")
    es.add_argument("--time", required=True, help="Total exam duration (e.g. '3 hours')")
    es.add_argument("--format", required=True, help="Exam format (e.g. 'multiple choice + free response')")
    es.add_argument("--weak-areas", help="Comma-separated list of weak areas to address")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "flashcards": cmd_flashcards,
        "quiz": cmd_quiz,
        "study-plan": cmd_study_plan,
        "exam-strategy": cmd_exam_strategy,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
