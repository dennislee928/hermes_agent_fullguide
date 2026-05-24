#!/usr/bin/env python3
"""
learning_assistant.py — Hermes-powered learning assistant: language tutor,
math problem solver, science simplifier, history explainer, vocabulary builder,
reading comprehension, and concept map creator.

Usage:
  python learning_assistant.py translate --text "Hello world" --to Spanish --explain
  python learning_assistant.py math "integral of x^2 from 0 to 3"
  python learning_assistant.py science "explain CRISPR gene editing for a 15-year-old"
  python learning_assistant.py history "explain the causes of World War I"
  python learning_assistant.py vocab --word "ephemeral" --examples 5
  python learning_assistant.py comprehension --file article.txt
  python learning_assistant.py concept-map --topic "Photosynthesis" --depth 3
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
            print()
            break


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except PermissionError:
        print(f"Error: Cannot read file (permission denied): {path}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# LANGUAGE TUTOR
# ---------------------------------------------------------------------------

def cmd_translate(args: argparse.Namespace) -> None:
    system = (
        "You are an expert language tutor fluent in all major world languages. "
        "Your translations are accurate and natural — not word-for-word machine translations. "
        "When explaining grammar, you focus on the key structural differences that help learners "
        "understand WHY the target language works the way it does. You highlight common learner "
        "mistakes and provide memory hooks. You adjust your explanations to the learner's level."
    )

    source_lang = f" from {args.from_lang}" if args.from_lang else ""
    level_note = f"\nLearner level: {args.level}" if args.level else ""

    explain_section = ""
    if args.explain:
        explain_section = (
            "\n\nAfter the translation, provide:\n"
            "1. GRAMMAR NOTES: Key structural differences between the source and target language for this sentence\n"
            "2. COMMON MISTAKES: What learners typically get wrong with this type of sentence\n"
            "3. PRONUNCIATION TIP: How to pronounce any difficult words in the translation\n"
            "4. ALTERNATIVE PHRASINGS: 1-2 other natural ways to express the same idea\n"
        )

    practice_section = ""
    if args.practice and args.practice > 0:
        practice_section = (
            f"\n\nAlso generate {args.practice} practice sentences in {args.to} "
            f"that use the same grammatical structure, with English translations."
        )

    user_message = (
        f"Translate the following text{source_lang} to {args.to}:"
        f"{level_note}\n\n"
        f'"{args.text}"\n'
        f"{explain_section}"
        f"{practice_section}"
    )

    print(f"\n{'='*60}")
    print(f"LANGUAGE TUTOR: Translating to {args.to}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# MATH PROBLEM SOLVER
# ---------------------------------------------------------------------------

def cmd_math(args: argparse.Namespace) -> None:
    system = (
        "You are a patient and precise mathematics tutor who specializes in step-by-step "
        "problem solving. You show every step of the solution clearly, label each step with "
        "a brief description of what you are doing and why, and present intermediate results "
        "before moving to the next step. You use standard mathematical notation. "
        "After solving, you verify the answer by checking it (substituting back in, checking "
        "units, etc.). You also note any important assumptions or domain restrictions."
    )

    problem = args.problem
    if args.file:
        problem = read_file(args.file)

    user_message = (
        f"Solve the following math problem step-by-step:\n\n"
        f"{problem}\n\n"
        f"Format your solution as:\n"
        f"PROBLEM: [restate the problem clearly]\n"
        f"STEP 1 — [step name]: [work and explanation]\n"
        f"STEP 2 — [step name]: [work and explanation]\n"
        f"...\n"
        f"ANSWER: [final answer clearly stated]\n"
        f"VERIFICATION: [check that the answer is correct]\n"
        f"NOTE: [any important assumptions, domain restrictions, or alternative methods]\n"
    )

    print(f"\n{'='*60}")
    print("MATH PROBLEM SOLVER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SCIENCE SIMPLIFIER
# ---------------------------------------------------------------------------

def cmd_science(args: argparse.Namespace) -> None:
    system = (
        "You are a gifted science communicator — like a great science teacher who can explain "
        "anything to anyone at the right level. You build explanations from the ground up: "
        "starting with an intuitive analogy, then layering in the actual mechanism, then "
        "connecting to real-world applications. You are scientifically accurate and never "
        "mislead through oversimplification. You include surprising or counterintuitive aspects "
        "that make science memorable. Always end with 'Going Deeper' for those who want more."
    )

    concept = args.concept
    if args.file:
        concept = read_file(args.file)

    audience_note = f"\nTarget audience: {args.audience}" if args.audience else ""

    user_message = (
        f"Explain the following scientific concept:\n"
        f"{concept}"
        f"{audience_note}\n\n"
        f"Structure your explanation as:\n"
        f"1. THE BIG IDEA (1-2 sentences: the core of what this is)\n"
        f"2. INTUITIVE ANALOGY (explain using something everyday)\n"
        f"3. HOW IT ACTUALLY WORKS (the real mechanism, accurately but accessibly)\n"
        f"4. WHY IT'S INTERESTING/SURPRISING (the part most people don't know)\n"
        f"5. REAL-WORLD APPLICATIONS (how this affects everyday life or technology)\n"
        f"6. COMMON MISCONCEPTIONS (what most people get wrong)\n"
        f"7. GOING DEEPER (what to explore next for more detail)\n"
    )

    print(f"\n{'='*60}")
    print("SCIENCE SIMPLIFIER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# HISTORY EXPLAINER
# ---------------------------------------------------------------------------

def cmd_history(args: argparse.Namespace) -> None:
    system = (
        "You are a historian and master teacher with expertise across world history. "
        "You explain historical events by establishing context first, then tracing causes and "
        "effects with specific people, dates, and places. You present multiple perspectives "
        "when historical interpretation is contested. You connect history to present-day "
        "relevance. Your explanations are engaging, not just encyclopedic — you highlight the "
        "human drama and the moments where history could have gone differently."
    )

    topic = args.topic
    if args.file:
        topic = read_file(args.file)

    audience_note = f"\nAudience: {args.audience}" if args.audience else ""
    perspectives_note = (
        "\nInclude multiple historical perspectives and interpretations of this event."
        if args.perspectives
        else ""
    )

    user_message = (
        f"Explain the following historical topic:"
        f"{audience_note}"
        f"{perspectives_note}\n\n"
        f"Topic: {topic}\n\n"
        f"Structure your explanation as:\n"
        f"1. CONTEXT (background needed to understand the event)\n"
        f"2. KEY CAUSES or KEY EVENTS (numbered, specific)\n"
        f"3. KEY FIGURES (who were the most important actors and why)\n"
        f"4. CONSEQUENCES (short-term and long-term)\n"
        f"5. HISTORICAL SIGNIFICANCE (why does this matter?)\n"
        f"6. MODERN CONNECTIONS (how does this connect to the present?)\n"
        f"7. FURTHER EXPLORATION (key books, primary sources, documentaries)\n"
    )

    print(f"\n{'='*60}")
    print("HISTORY EXPLAINER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# VOCABULARY BUILDER
# ---------------------------------------------------------------------------

def cmd_vocab(args: argparse.Namespace) -> None:
    system = (
        "You are a lexicographer and vocabulary expert who helps people deeply understand and "
        "remember words. You go far beyond a dictionary definition: you provide etymology "
        "(word origins) as a memory hook, usage examples across multiple registers and contexts, "
        "the full word family, common collocations, subtle usage notes, and warnings about "
        "commonly confused words. Your examples are vivid and contextually accurate — not generic."
    )

    context_note = f"\nPrefer examples from the {args.context} context." if args.context else ""

    user_message = (
        f"Provide a comprehensive vocabulary entry for the word: '{args.word}'\n"
        f"Number of examples: {args.examples}"
        f"{context_note}\n\n"
        f"Include:\n"
        f"1. PRONUNCIATION (phonetic)\n"
        f"2. PART OF SPEECH and REGISTER (formal/informal/literary/technical)\n"
        f"3. DEFINITION (precise and complete)\n"
        f"4. ETYMOLOGY (word origin as a memory hook)\n"
        f"5. EXAMPLES IN CONTEXT ({args.examples} sentences across different contexts/registers)\n"
        f"6. SYNONYMS (with brief notes on how each differs in nuance)\n"
        f"7. ANTONYMS\n"
        f"8. COMMON COLLOCATIONS (frequent word pairings)\n"
        f"9. WORD FAMILY (noun, verb, adjective, adverb forms if they exist)\n"
        f"10. MEMORY HOOK (a technique or image to remember the word)\n"
        f"11. USAGE WARNING (common confusion or misuse to avoid)\n"
    )

    print(f"\n{'='*60}")
    print(f"VOCABULARY BUILDER: {args.word}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# READING COMPREHENSION
# ---------------------------------------------------------------------------

def cmd_comprehension(args: argparse.Namespace) -> None:
    system = (
        "You are an expert reading instructor and curriculum developer. You analyze texts at "
        "multiple levels: literal comprehension, inferential understanding, and critical "
        "evaluation. Your comprehension questions are pedagogically sound — they target specific "
        "cognitive levels (Bloom's taxonomy) and avoid questions with trivially obvious answers. "
        "You identify vocabulary words that are worth teaching, locate the main idea precisely, "
        "and suggest annotation strategies that build reading skills."
    )

    if args.file:
        passage_text = read_file(args.file)
        source_label = f"from file: {args.file}"
    elif args.text:
        passage_text = args.text
        source_label = "inline text"
    else:
        print("Error: Provide either --file or --text with the passage.", file=sys.stderr)
        sys.exit(1)

    level_note = f"\nStudent level: {args.level}" if args.level else ""
    focus_note = (
        f"\nFocus question type: {args.focus} questions only."
        if args.focus
        else ""
    )

    user_message = (
        f"Analyze the following passage for reading comprehension work ({source_label})."
        f"{level_note}"
        f"{focus_note}\n\n"
        f"Provide:\n"
        f"1. MAIN IDEA (1-2 sentences: what is the central argument or message?)\n"
        f"2. KEY DETAILS (3-5 most important supporting details)\n"
        f"3. VOCABULARY SPOTLIGHT (3-5 words worth teaching, with definitions)\n"
        f"4. COMPREHENSION QUESTIONS:\n"
        f"   - 2-3 Literal questions (directly stated in the text)\n"
        f"   - 2-3 Inferential questions (requires reading between the lines)\n"
        f"   - 2 Evaluative questions (requires judgment or connection beyond the text)\n"
        f"5. ANNOTATION SUGGESTIONS (3-4 specific things to mark/note while re-reading)\n"
        f"6. DISCUSSION QUESTIONS (1-2 open-ended questions for group discussion)\n\n"
        f"PASSAGE:\n{'-'*60}\n{passage_text}\n{'-'*60}"
    )

    print(f"\n{'='*60}")
    print("READING COMPREHENSION ANALYSIS")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CONCEPT MAP CREATOR
# ---------------------------------------------------------------------------

def cmd_concept_map(args: argparse.Namespace) -> None:
    system = (
        "You are an expert educator and knowledge architect who specializes in creating "
        "concept maps. Your maps reveal the relational structure of knowledge — not just "
        "hierarchies, but the meaningful connections between ideas, with relationship labels "
        "that are specific and informative ('is caused by', 'requires understanding of', "
        "'is an example of') rather than generic ('relates to', 'connects to'). "
        "You output both a text-tree and a Mermaid diagram for visual rendering."
    )

    topic = args.topic
    if args.file:
        topic = f"the following content:\n{read_file(args.file)}"

    user_message = (
        f"Create a concept map for: {topic}\n"
        f"Depth: {args.depth} levels\n\n"
        f"Provide:\n"
        f"1. TEXT TREE FORMAT:\n"
        f"   Use indentation and └──/├── characters. Label each relationship in [brackets].\n"
        f"   Example:\n"
        f"   Central Concept\n"
        f"   ├── [is divided into] Sub-concept A\n"
        f"   │   └── [example of] Specific Example\n"
        f"   └── [is related to] Sub-concept B\n\n"
        f"2. MERMAID DIAGRAM:\n"
        f"   Provide a valid Mermaid 'graph TD' diagram that can be pasted into any Markdown viewer.\n\n"
        f"3. KEY RELATIONSHIPS SUMMARY:\n"
        f"   3-5 sentences explaining the most important relationships in the map.\n"
    )

    print(f"\n{'='*60}")
    print(f"CONCEPT MAP: {args.topic}")
    print(f"Depth: {args.depth} levels")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered learning assistant.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- translate ---
    tr = subparsers.add_parser("translate", help="Translate text with grammar explanation")
    tr.add_argument("--text", required=True, help="Text to translate")
    tr.add_argument("--to", required=True, help="Target language (e.g. Spanish, French, Japanese)")
    tr.add_argument("--from", dest="from_lang", help="Source language (auto-detected if omitted)")
    tr.add_argument("--explain", action="store_true", help="Include grammar notes and explanation")
    tr.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        help="Learner proficiency level for explanation depth",
    )
    tr.add_argument("--practice", type=int, default=0, help="Number of practice sentences to generate (default: 0)")

    # --- math ---
    mt = subparsers.add_parser("math", help="Solve a math problem step-by-step")
    mt.add_argument("problem", nargs="?", help="Math problem as a string")
    mt.add_argument("--file", help="Path to file containing the math problem")

    # --- science ---
    sc = subparsers.add_parser("science", help="Simplify a scientific concept")
    sc.add_argument("concept", nargs="?", help="Scientific concept or question to explain")
    sc.add_argument("--file", help="Path to file containing the concept/text")
    sc.add_argument("--audience", help="Target audience (e.g. '15-year-old', 'curious adult', 'college student')")

    # --- history ---
    hs = subparsers.add_parser("history", help="Explain a historical event or topic")
    hs.add_argument("topic", nargs="?", help="Historical topic to explain")
    hs.add_argument("--file", help="Path to file containing the topic/text")
    hs.add_argument("--audience", help="Target audience (e.g. '10th grade', 'general adult')")
    hs.add_argument("--perspectives", action="store_true", help="Include multiple historical perspectives")

    # --- vocab ---
    vc = subparsers.add_parser("vocab", help="Build vocabulary with deep word analysis")
    vc.add_argument("--word", required=True, help="Word to analyze")
    vc.add_argument("--examples", type=int, default=5, help="Number of example sentences (default: 5)")
    vc.add_argument(
        "--context",
        choices=["academic", "business", "literary", "everyday"],
        help="Preferred context for examples",
    )

    # --- comprehension ---
    cp = subparsers.add_parser("comprehension", help="Generate reading comprehension questions")
    cp_source = cp.add_mutually_exclusive_group()
    cp_source.add_argument("--file", help="Path to passage text file")
    cp_source.add_argument("--text", help="Passage text inline")
    cp.add_argument(
        "--level",
        choices=["elementary", "middle", "high", "college"],
        help="Student level for question calibration",
    )
    cp.add_argument(
        "--focus",
        choices=["literal", "inferential", "evaluative"],
        help="Focus on one question type only",
    )

    # --- concept-map ---
    cm = subparsers.add_parser("concept-map", help="Create a concept map for a topic")
    cm.add_argument("--topic", help="Topic for the concept map")
    cm.add_argument("--file", help="Path to file with content to map")
    cm.add_argument("--depth", type=int, default=3, choices=[2, 3, 4], help="Map depth in levels (default: 3)")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Validate that at least a topic or file is provided for concept-map
    if args.command == "concept-map" and not args.topic and not args.file:
        print("Error: Provide either --topic or --file for concept-map.", file=sys.stderr)
        sys.exit(1)

    # Validate math and science positional args
    if args.command == "math" and not args.problem and not args.file:
        print("Error: Provide a problem as a positional argument or via --file.", file=sys.stderr)
        sys.exit(1)

    if args.command == "science" and not args.concept and not args.file:
        print("Error: Provide a concept as a positional argument or via --file.", file=sys.stderr)
        sys.exit(1)

    if args.command == "history" and not args.topic and not args.file:
        print("Error: Provide a topic as a positional argument or via --file.", file=sys.stderr)
        sys.exit(1)

    dispatch = {
        "translate": cmd_translate,
        "math": cmd_math,
        "science": cmd_science,
        "history": cmd_history,
        "vocab": cmd_vocab,
        "comprehension": cmd_comprehension,
        "concept-map": cmd_concept_map,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
