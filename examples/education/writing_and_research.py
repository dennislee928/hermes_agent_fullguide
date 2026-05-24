#!/usr/bin/env python3
"""
writing_and_research.py — Hermes-powered writing and research tools:
essay feedback, research paper summarizer, citation formatter, and
debate argument generator.

Usage:
  python writing_and_research.py essay-feedback --file essay.txt
  python writing_and_research.py essay-feedback --file essay.txt --level college
  python writing_and_research.py summarize --file paper.txt
  python writing_and_research.py summarize --file paper.txt --audience general
  python writing_and_research.py cite --style APA --source "Author: Chen J, Title: Sleep, Journal: Nature, Year: 2023"
  python writing_and_research.py debate --topic "AI in education" --side for
  python writing_and_research.py debate --topic "Universal Basic Income" --side against
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
    """Read a file and return its contents, or exit with an error."""
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
# ESSAY FEEDBACK
# ---------------------------------------------------------------------------

def cmd_essay_feedback(args: argparse.Namespace) -> None:
    system = (
        "You are an experienced writing instructor and academic editor. Your feedback is "
        "specific, constructive, and actionable — not vague praise or generic criticism. "
        "You evaluate essays at multiple levels: thesis quality, argument structure and logic, "
        "evidence quality, paragraph organization, transitions, tone/register, and grammar/style. "
        "For each issue you identify, you explain WHY it is an issue and suggest a specific fix. "
        "You balance criticism with genuine acknowledgment of strengths. "
        "You provide an approximate grade estimate with a score breakdown."
    )

    if args.file:
        essay_text = read_file(args.file)
        source_label = f"from file: {args.file}"
    elif args.text:
        essay_text = args.text
        source_label = "from inline input"
    else:
        print("Error: Provide either --file or --text with the essay content.", file=sys.stderr)
        sys.exit(1)

    level_guidance = {
        "highschool": "Evaluate to high school standards. Focus on clear thesis, basic argument structure, and grammar.",
        "college": "Evaluate to undergraduate college standards. Expect sophisticated argument development and evidence integration.",
        "graduate": "Evaluate to graduate-level standards. Expect nuanced argumentation, awareness of scholarly debate, and precise academic prose.",
    }.get(args.level, "Evaluate to undergraduate college standards.")

    focus_guidance = ""
    if args.focus:
        focus_map = {
            "structure": "Focus ONLY on essay structure: thesis, argument flow, paragraph organization, transitions.",
            "argument": "Focus ONLY on argument quality: claim strength, evidence, logical reasoning, counterarguments.",
            "language": "Focus ONLY on language: grammar, style, word choice, sentence variety, tone.",
        }
        focus_guidance = f"\nFocus area: {focus_map.get(args.focus, '')}"

    user_message = (
        f"Please provide detailed feedback on the following essay ({source_label}).\n"
        f"Level: {args.level}\n"
        f"{level_guidance}"
        f"{focus_guidance}\n\n"
        f"Structure your feedback as:\n"
        f"1. Overall Grade Estimate (score/100 and letter grade)\n"
        f"2. Thesis Assessment (score/10, specific feedback)\n"
        f"3. Argument Structure (score/10, specific feedback)\n"
        f"4. Evidence Quality (score/10, specific feedback)\n"
        f"5. Grammar & Style (list specific issues with line/location if possible)\n"
        f"6. Strengths (genuine strengths worth preserving)\n"
        f"7. Priority Revision List (top 3-5 changes that would most improve the essay)\n\n"
        f"ESSAY:\n{'-'*60}\n{essay_text}\n{'-'*60}"
    )

    print(f"\n{'='*60}")
    print(f"ESSAY FEEDBACK ({args.level.upper()} level)")
    if args.focus:
        print(f"Focus: {args.focus}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# RESEARCH PAPER SUMMARIZER
# ---------------------------------------------------------------------------

def cmd_summarize(args: argparse.Namespace) -> None:
    system = (
        "You are a research analyst and science communicator with expertise across academic "
        "disciplines. Your summaries are structured, accurate, and capture the paper's core "
        "contribution — not just a section-by-section synopsis. You identify what makes the "
        "research novel, assess the methodology critically, and translate findings into "
        "plain language without losing precision. Always note important limitations."
    )

    if args.file:
        paper_text = read_file(args.file)
        source_label = f"from file: {args.file}"
    elif args.text:
        paper_text = args.text
        source_label = "from inline input"
    else:
        print("Error: Provide either --file or --text with the paper content.", file=sys.stderr)
        sys.exit(1)

    audience_guidance = {
        "researcher": "Write for a researcher in a related field — assume scientific literacy but not domain expertise.",
        "general": "Write for an intelligent general audience — no jargon, analogies where helpful.",
        "student": "Write for an upper-division undergraduate student — explain technical terms briefly.",
    }.get(args.audience, "Write for a researcher in a related field.")

    focus_guidance = ""
    if args.focus:
        focus_map = {
            "methodology": "Focus especially on the methodology: study design, sample, measures, analysis approach, and validity.",
            "findings": "Focus especially on the key findings: what was found, effect sizes, statistical significance.",
            "implications": "Focus especially on implications: what this means for the field, practice, and future research.",
        }
        focus_guidance = f"\nFocus: {focus_map.get(args.focus, '')}"

    user_message = (
        f"Summarize the following research paper ({source_label}).\n"
        f"Audience: {args.audience} — {audience_guidance}"
        f"{focus_guidance}\n\n"
        f"Structure the summary as:\n"
        f"1. Paper identification (title, authors, journal, year — if present in the text)\n"
        f"2. Research Question / Objective\n"
        f"3. Methodology (brief but specific)\n"
        f"4. Key Findings (numbered, with any effect sizes or statistics)\n"
        f"5. Limitations\n"
        f"6. Implications and Significance\n"
        f"7. Key Terms Glossary (define 3-5 technical terms)\n"
        f"8. Plain-Language Summary (2-3 sentences for a general audience)\n\n"
        f"PAPER:\n{'-'*60}\n{paper_text}\n{'-'*60}"
    )

    print(f"\n{'='*60}")
    print(f"RESEARCH PAPER SUMMARY (audience: {args.audience})")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CITATION FORMATTER
# ---------------------------------------------------------------------------

def cmd_cite(args: argparse.Namespace) -> None:
    system = (
        "You are a citation and reference expert with deep knowledge of APA (7th edition), "
        "MLA (9th edition), Chicago (17th edition, author-date and notes-bibliography), "
        "Harvard, Vancouver, and IEEE citation styles. You apply citation rules precisely, "
        "including edge cases: multiple authors, no-date sources, DOI formatting, electronic "
        "sources, corporate authors, and edited volumes. For each citation you provide: "
        "the reference list entry, the in-text citation, a narrative in-text form, and "
        "specific formatting notes explaining key decisions."
    )

    source_text = args.source
    if args.file:
        source_text = read_file(args.file)

    if not source_text:
        print("Error: Provide source information via --source or --file.", file=sys.stderr)
        sys.exit(1)

    source_type_guidance = ""
    if args.source_type:
        source_type_guidance = f"\nSource type: {args.source_type}"

    user_message = (
        f"Format the following source as a citation in {args.style} style.\n"
        f"{source_type_guidance}\n\n"
        f"Source information:\n{source_text}\n\n"
        f"Provide:\n"
        f"1. Reference list / bibliography entry (exactly as it would appear in the reference list)\n"
        f"2. In-text parenthetical citation\n"
        f"3. Narrative in-text citation (e.g., 'Smith (2020) found...')\n"
        f"4. Formatting notes — explain key formatting decisions (italics, punctuation, DOI format, etc.)\n"
        f"5. Common mistakes to avoid for this source type in {args.style}\n"
    )

    print(f"\n{'='*60}")
    print(f"CITATION FORMATTER: {args.style}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# DEBATE ARGUMENT GENERATOR
# ---------------------------------------------------------------------------

def cmd_debate(args: argparse.Namespace) -> None:
    system = (
        "You are an expert debate coach and argumentation specialist with experience in "
        "competitive debate (Policy, LD, Parliamentary) and academic rhetoric. You construct "
        "arguments following the Claim-Warrant-Evidence-Impact structure. Your arguments are "
        "logically rigorous, use credible evidence types, anticipate the strongest objections, "
        "and provide specific rebuttal strategies. You avoid logical fallacies and straw-man "
        "representations of the opposing side."
    )

    side_label = args.side.upper()
    opposing_side = "AGAINST" if args.side.lower() == "for" else "FOR"

    evidence_guidance = ""
    if args.evidence_types:
        evidence_guidance = f"\nPrefer these evidence types: {args.evidence_types}"

    format_guidance = ""
    if args.format == "essay":
        format_guidance = "\nFormat the output as a written argumentative essay, not a debate brief."
    else:
        format_guidance = "\nFormat as a structured debate brief with labeled sections."

    user_message = (
        f"Generate a complete debate brief for the following:\n\n"
        f"Topic (resolution): {args.topic}\n"
        f"Side: {side_label} (arguing in favor of / supporting the resolution)\n"
        f"{evidence_guidance}"
        f"{format_guidance}\n\n"
        f"Include:\n"
        f"1. Main claim / thesis statement\n"
        f"2. Three distinct arguments (each with: sub-claim, warrant, evidence basis, impact/significance)\n"
        f"3. Two anticipated rebuttals from the {opposing_side} side with specific counter-responses\n"
        f"4. Closing strategy / key message\n"
        f"5. Key terms to define early in the debate\n"
    )

    print(f"\n{'='*60}")
    print(f"DEBATE BRIEF: {args.topic}")
    print(f"Side: {side_label}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered writing and research tools.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- essay-feedback ---
    ef = subparsers.add_parser("essay-feedback", help="Get detailed feedback on an essay")
    ef_source = ef.add_mutually_exclusive_group()
    ef_source.add_argument("--file", help="Path to essay text file")
    ef_source.add_argument("--text", help="Essay text inline")
    ef.add_argument(
        "--level",
        choices=["highschool", "college", "graduate"],
        default="college",
        help="Academic level for evaluation standards (default: college)",
    )
    ef.add_argument(
        "--focus",
        choices=["structure", "argument", "language"],
        help="Limit feedback to one area",
    )

    # --- summarize ---
    sm = subparsers.add_parser("summarize", help="Summarize a research paper")
    sm_source = sm.add_mutually_exclusive_group()
    sm_source.add_argument("--file", help="Path to paper text file")
    sm_source.add_argument("--text", help="Paper text inline")
    sm.add_argument(
        "--audience",
        choices=["researcher", "student", "general"],
        default="researcher",
        help="Target audience for the summary (default: researcher)",
    )
    sm.add_argument(
        "--focus",
        choices=["methodology", "findings", "implications"],
        help="Emphasize a particular aspect of the paper",
    )

    # --- cite ---
    ct = subparsers.add_parser("cite", help="Format a citation in any academic style")
    ct.add_argument(
        "--style",
        required=True,
        choices=["APA", "MLA", "Chicago", "Harvard", "Vancouver", "IEEE"],
        help="Citation style",
    )
    ct_source = ct.add_mutually_exclusive_group()
    ct_source.add_argument("--source", help="Source information as a string")
    ct_source.add_argument("--file", help="Path to file containing source information")
    ct.add_argument(
        "--source-type",
        help="Type of source (e.g. 'journal article', 'book', 'website', 'podcast')",
    )

    # --- debate ---
    db = subparsers.add_parser("debate", help="Generate a structured debate argument")
    db.add_argument("--topic", required=True, help="Debate topic / resolution")
    db.add_argument(
        "--side",
        required=True,
        choices=["for", "against"],
        help="Which side to argue",
    )
    db.add_argument(
        "--format",
        choices=["debate", "essay"],
        default="debate",
        help="Output format: debate brief or argumentative essay (default: debate)",
    )
    db.add_argument(
        "--evidence-types",
        help="Preferred evidence types (e.g. 'statistical, expert testimony')",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "essay-feedback": cmd_essay_feedback,
        "summarize": cmd_summarize,
        "cite": cmd_cite,
        "debate": cmd_debate,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
