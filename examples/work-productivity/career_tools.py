#!/usr/bin/env python3
"""
career_tools.py — Career and HR tools using Hermes via Ollama

Usage:
  python career_tools.py cover-letter --role "Software Engineer" --company "Acme" --resume resume.txt
  python career_tools.py cover-letter --role "PM" --company "Stripe" --jd job_description.txt --resume resume.txt
  python career_tools.py review-resume --resume resume.txt --role "Data Scientist" --level mid
  python career_tools.py interview-prep --role "Product Manager" --level senior --focus behavioral
  python career_tools.py interview-prep --role "Staff Engineer" --company "Airbnb" --focus system-design
  python career_tools.py perf-review --role "Senior Engineer" --rating "exceeds expectations" --notes notes.txt
  python career_tools.py perf-review --role "Designer" --rating "meets expectations" --notes "Delivered projects on time, needs to take initiative" --pov employee
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


def cmd_cover_letter(args: argparse.Namespace) -> None:
    """Write a tailored cover letter."""
    system_prompt = (
        "You are an expert career coach and cover letter writer. "
        "Write compelling, personalized cover letters that stand out. "
        "Focus on specific value the candidate brings — not generic phrases. "
        "Match the company's tone and culture based on available signals. "
        "Structure: compelling opening hook, 2-3 paragraphs of specific relevant experience, "
        "company-specific paragraph showing genuine interest, concise close. "
        "Never fabricate experience or credentials not mentioned in the resume."
    )

    resume_text = ""
    jd_text = ""

    if args.resume:
        resume_text = read_file(args.resume)
    if args.jd:
        jd_text = read_file(args.jd)

    user_message = (
        f"Write a cover letter for the following application:\n"
        f"- Role: {args.role}\n"
        f"- Company: {args.company}\n"
    )

    if args.tone:
        user_message += f"- Tone: {args.tone}\n"

    if args.word_limit:
        user_message += f"- Word limit: approximately {args.word_limit} words\n"

    if resume_text:
        user_message += f"\nResume / Background:\n---\n{resume_text}\n---\n"

    if jd_text:
        user_message += f"\nJob Description:\n---\n{jd_text}\n---\n"

    if args.highlights:
        user_message += f"\nKey points to emphasize: {args.highlights}\n"

    user_message += (
        "\nWrite the complete cover letter. "
        "Use [Your Name], [Your Email], [Your Phone] as placeholders for contact info."
    )

    print(f"\n--- Cover Letter: {args.role} at {args.company} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_review_resume(args: argparse.Namespace) -> None:
    """Review a resume and provide actionable feedback."""
    system_prompt = (
        "You are a senior recruiter and career coach with expertise in resume optimization. "
        "Provide specific, actionable resume feedback — not generic advice. "
        "Identify: weak action verbs, missing quantification, ATS keyword gaps, "
        "formatting inconsistencies, and structural issues. "
        "For every issue you flag, provide a concrete rewrite or fix. "
        "Give an overall score out of 10 and a clear priority list for improvements."
    )

    resume_text = read_file(args.resume)
    jd_text = read_file(args.jd) if args.jd else ""

    user_message = (
        f"Review this resume for the target role:\n"
        f"- Target role: {args.role}\n"
        f"- Seniority level: {args.level}\n\n"
        f"Resume content:\n---\n{resume_text}\n---\n"
    )

    if jd_text:
        user_message += f"\nJob Description (for ATS keyword analysis):\n---\n{jd_text}\n---\n"

    user_message += (
        "\nProvide:\n"
        "1. Overall score (x/10) with brief justification\n"
        "2. Critical Issues (must fix before applying)\n"
        "3. High Priority improvements\n"
        "4. Rewritten bullet examples for the weakest experience section\n"
        "5. ATS keyword gaps (if JD was provided)\n"
        "6. Formatting notes"
    )

    print(f"\n--- Resume Review: {args.role} ({args.level}) ---\n")
    stream_chat(system_prompt, user_message)


def cmd_interview_prep(args: argparse.Namespace) -> None:
    """Generate interview preparation questions and answers."""
    system_prompt = (
        "You are a senior interview coach with expertise across engineering, product, and business roles. "
        "Generate realistic, role-appropriate interview questions with high-quality sample answers. "
        "For behavioral questions: use STAR format (Situation, Task, Action, Result). "
        "For technical questions: provide the core concepts the interviewer is testing. "
        "Include likely follow-up questions. "
        "Add company-specific coaching notes when a company is provided. "
        "Be honest about what interviewers at senior levels are really evaluating."
    )

    user_message = (
        f"Generate interview preparation for:\n"
        f"- Role: {args.role}\n"
        f"- Level: {args.level}\n"
        f"- Focus area: {args.focus}\n"
    )

    if args.company:
        user_message += f"- Company: {args.company}\n"

    if args.background:
        user_message += f"- My background: {args.background}\n"

    user_message += (
        f"\nGenerate 5-7 questions for the '{args.focus}' focus area.\n"
        f"For each question:\n"
        f"1. The question\n"
        f"2. What the interviewer is really evaluating\n"
        f"3. A sample strong answer (STAR format for behavioral, framework for technical)\n"
        f"4. One likely follow-up question\n\n"
        f"End with 3-5 coaching tips specific to this role/level/company combination."
    )

    print(f"\n--- Interview Prep: {args.role} ({args.level}) — {args.focus} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_perf_review(args: argparse.Namespace) -> None:
    """Write performance review text."""
    system_prompt = (
        "You are an expert in HR writing and performance management. "
        "Write balanced, professional performance review text that is: "
        "specific (references actual behaviors/outcomes), fair, growth-oriented, "
        "and appropriate for formal HR documentation. "
        "Avoid bias patterns, vague superlatives, and punitive framing. "
        "For 'exceeds expectations': lead with concrete strengths and impact. "
        "For 'meets expectations': acknowledge solid performance and name 1-2 clear growth areas. "
        "For 'needs improvement': use constructive, non-punitive language with specific examples. "
        "Manager POV: write about the employee in third person. "
        "Employee POV (self-review): write in first person."
    )

    # Notes can come from --notes as text or as a file path
    notes_text = ""
    if args.notes:
        import os
        if os.path.isfile(args.notes):
            notes_text = read_file(args.notes)
        else:
            notes_text = args.notes

    user_message = (
        f"Write a performance review with these details:\n"
        f"- Employee role: {args.role}\n"
        f"- Overall rating: {args.rating}\n"
        f"- Point of view: {args.pov}\n"
    )

    if notes_text:
        user_message += f"- Raw notes and observations:\n{notes_text}\n"

    if args.period:
        user_message += f"- Review period: {args.period}\n"

    user_message += (
        "\nStructure the review as:\n"
        "1. Achievements & Strengths (2-3 paragraphs of specific examples)\n"
        "2. Areas for Growth (constructive, with specific suggestions — not criticism)\n"
        "3. Goals for Next Period (3 measurable goals)\n\n"
        "Important: Only use information from the notes provided. "
        "Use [Employee] as a placeholder for the employee's name."
    )

    print(f"\n--- Performance Review: {args.role} ({args.rating}) ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Career and HR tools with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- cover-letter ---
    cl_p = subparsers.add_parser("cover-letter", help="Write a tailored cover letter")
    cl_p.add_argument("--role", required=True, help="Job title/role applying for")
    cl_p.add_argument("--company", required=True, help="Company name")
    cl_p.add_argument("--resume", default=None, help="Path to resume file")
    cl_p.add_argument("--jd", default=None, help="Path to job description file")
    cl_p.add_argument(
        "--tone",
        default="confident and professional",
        help="Desired tone (e.g., confident, humble, enthusiastic)",
    )
    cl_p.add_argument("--word-limit", type=int, default=0, help="Approximate word limit")
    cl_p.add_argument("--highlights", default="", help="Key points to emphasize")
    cl_p.set_defaults(func=cmd_cover_letter)

    # --- review-resume ---
    rr_p = subparsers.add_parser("review-resume", help="Get actionable resume feedback")
    rr_p.add_argument("--resume", required=True, help="Path to resume file")
    rr_p.add_argument("--role", required=True, help="Target role/job title")
    rr_p.add_argument(
        "--level",
        default="mid",
        choices=["entry", "mid", "senior", "staff", "executive"],
        help="Seniority level",
    )
    rr_p.add_argument("--jd", default=None, help="Path to job description for ATS gap analysis")
    rr_p.set_defaults(func=cmd_review_resume)

    # --- interview-prep ---
    ip_p = subparsers.add_parser("interview-prep", help="Generate interview preparation materials")
    ip_p.add_argument("--role", required=True, help="Role you are interviewing for")
    ip_p.add_argument(
        "--level",
        default="mid",
        choices=["entry", "mid", "senior", "staff", "executive"],
        help="Seniority level",
    )
    ip_p.add_argument(
        "--focus",
        default="behavioral",
        choices=["behavioral", "technical", "system-design", "case-study", "all"],
        help="Interview focus area",
    )
    ip_p.add_argument("--company", default="", help="Target company (for culture-specific tips)")
    ip_p.add_argument("--background", default="", help="Your relevant background to personalize answers")
    ip_p.set_defaults(func=cmd_interview_prep)

    # --- perf-review ---
    pr_p = subparsers.add_parser("perf-review", help="Write performance review text")
    pr_p.add_argument("--role", required=True, help="Employee's job role")
    pr_p.add_argument(
        "--rating",
        required=True,
        choices=["exceeds expectations", "meets expectations", "needs improvement"],
        help="Overall performance rating",
    )
    pr_p.add_argument(
        "--notes",
        default="",
        help="Raw notes, accomplishments, and observations (text or file path)",
    )
    pr_p.add_argument(
        "--pov",
        default="manager",
        choices=["manager", "employee"],
        help="Point of view: manager review or self-review",
    )
    pr_p.add_argument("--period", default="", help="Review period, e.g., 'H1 2024'")
    pr_p.set_defaults(func=cmd_perf_review)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
