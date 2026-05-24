#!/usr/bin/env python3
"""
financial_advisor.py — Hermes-powered financial advisory tools: investment explainer,
tax deduction finder, salary negotiation coach, loan comparison, credit card optimizer,
and retirement planner.

DISCLAIMER: This tool is for educational and informational purposes only.
It is NOT financial, tax, or legal advice. Consult licensed professionals
(CFP, CPA, attorney) for personalized guidance.

Usage:
  python financial_advisor.py invest "explain dollar-cost averaging vs lump sum investing"
  python financial_advisor.py tax-deductions --situation "freelancer, home office, student loan"
  python financial_advisor.py negotiate --role "Software Engineer" --offer 95000 --target 110000 --location "San Francisco"
  python financial_advisor.py loans --amount 25000 --term 60 --options "Bank A:6.5%,Credit Union:5.9%"
  python financial_advisor.py credit-cards --spending "groceries:600,dining:300,travel:200" --cards "Chase Sapphire,Citi Double Cash"
  python financial_advisor.py retirement --age 32 --savings 45000 --income 75000 --target-age 65
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"

FINANCE_DISCLAIMER = (
    "[DISCLAIMER: This output is for educational purposes only. It does not constitute "
    "financial, investment, tax, or legal advice. Consult a licensed financial advisor, "
    "CPA, or attorney for personalized professional guidance.]"
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


def parse_key_value_list(raw: str) -> str:
    """Convert 'key:value,key:value' into a formatted list string."""
    items = []
    for item in raw.split(","):
        item = item.strip()
        if ":" in item:
            k, v = item.split(":", 1)
            items.append(f"  {k.strip()}: {v.strip()}")
        else:
            items.append(f"  {item}")
    return "\n".join(items)


# ---------------------------------------------------------------------------
# INVESTMENT EXPLAINER
# ---------------------------------------------------------------------------

def cmd_invest(args: argparse.Namespace) -> None:
    system = (
        "You are a financial educator with deep knowledge of investment vehicles, markets, and "
        "personal finance strategy. You explain investment concepts accurately and clearly, "
        "always including both the mechanics (how it works) and the risk profile (what can go "
        "wrong). You use concrete numbers and historical examples to make concepts tangible. "
        "You are not a licensed advisor and you do not give personalized investment recommendations — "
        "you educate. You always distinguish between general principles and individual circumstances."
    )

    topic = args.topic
    if args.file:
        topic = read_file(args.file)

    level_note = f"\nExplanation level: {args.level}" if args.level else ""

    user_message = (
        f"Explain the following investment topic clearly and accurately:"
        f"{level_note}\n\n"
        f"{topic}\n\n"
        f"Structure your explanation as:\n"
        f"1. THE CORE CONCEPT (what this is, in plain language)\n"
        f"2. HOW IT WORKS (mechanics and process)\n"
        f"3. RISK PROFILE (what risks are involved; when can you lose money?)\n"
        f"4. REAL NUMBERS (historical returns, typical costs, or concrete examples)\n"
        f"5. COMPARED TO ALTERNATIVES (how does this compare to similar options?)\n"
        f"6. WHO IT'S BEST FOR (circumstances where this makes most sense)\n"
        f"7. COMMON MISCONCEPTIONS (what most people get wrong about this)\n"
        f"8. GETTING STARTED (practical first steps if relevant)\n"
        f"\n{FINANCE_DISCLAIMER}\n"
    )

    print(f"\n{'='*60}")
    print("INVESTMENT EXPLAINER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# TAX DEDUCTION FINDER
# ---------------------------------------------------------------------------

def cmd_tax_deductions(args: argparse.Namespace) -> None:
    system = (
        "You are a tax education specialist with comprehensive knowledge of US federal tax law, "
        "deductions, and credits. You help people identify deductions they may be eligible for "
        "based on their situation — not to prepare their taxes, but to ensure they arrive at a "
        "tax professional's office knowing what to ask about. You explain the eligibility "
        "criteria, estimated value, and documentation needed for each deduction. You are "
        "comprehensive and organized. You always recommend verification with a licensed CPA."
    )

    situation_text = args.situation
    if args.file:
        situation_text = read_file(args.file)

    year_note = f"\nTax year: {args.year}" if args.year else ""
    filing_note = f"\nFiling status: {args.filing_status}" if args.filing_status else ""

    user_message = (
        f"Based on the following situation, identify all potentially applicable tax "
        f"deductions and credits the person should discuss with their tax professional:"
        f"{year_note}"
        f"{filing_note}\n\n"
        f"SITUATION:\n{situation_text}\n\n"
        f"For each deduction/credit provide:\n"
        f"- Name and form/schedule\n"
        f"- Eligibility criteria (does this situation qualify?)\n"
        f"- Estimated value or limit\n"
        f"- Whether it requires itemizing or is above-the-line\n"
        f"- Documentation needed\n"
        f"- Any income phase-outs to be aware of\n\n"
        f"Also provide:\n"
        f"- TOTAL ESTIMATED ABOVE-THE-LINE DEDUCTIONS (those not requiring itemizing)\n"
        f"- ITEMIZING vs. STANDARD DEDUCTION analysis\n"
        f"- TOP 3 MOST VALUABLE DEDUCTIONS for this situation\n"
        f"\n{FINANCE_DISCLAIMER}\n"
    )

    print(f"\n{'='*60}")
    print("TAX DEDUCTION FINDER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SALARY NEGOTIATION COACH
# ---------------------------------------------------------------------------

def cmd_negotiate(args: argparse.Namespace) -> None:
    system = (
        "You are an expert salary negotiation coach who has helped thousands of professionals "
        "negotiate compensation. You provide specific, confident scripts — not vague advice. "
        "You know that 85%+ of employers expect negotiation and offers are almost never rescinded "
        "when negotiation is conducted professionally. You provide: opening scripts, counter-offer "
        "language, objection handling with specific responses, total compensation alternatives "
        "when base salary is immovable, and a closing strategy. You give an honest market context."
    )

    competing_note = f"\nCompeting offer: {args.competing_offer}" if args.competing_offer else ""
    experience_note = f"\nYears of experience: {args.experience}" if args.experience else ""
    context_note = ""
    if args.context:
        context = read_file(args.context) if args.context.endswith(".txt") else args.context
        context_note = f"\nAdditional context:\n{context}"

    user_message = (
        f"Create a comprehensive salary negotiation strategy for:\n\n"
        f"Role: {args.role}\n"
        f"Current offer: ${args.offer:,.0f}\n"
        f"Target compensation: ${args.target:,.0f}\n"
        f"Location: {args.location}"
        f"{experience_note}"
        f"{competing_note}"
        f"{context_note}\n\n"
        f"Provide:\n"
        f"1. MARKET CONTEXT (what the role pays in this market — be specific)\n"
        f"2. NEGOTIATION STRATEGY OVERVIEW (is the target realistic? what's the gap?)\n"
        f"3. RECOMMENDED COUNTER OFFER (specific number and why, leaving room to meet in middle)\n"
        f"4. STEP-BY-STEP SCRIPT (exact words for the negotiation conversation)\n"
        f"5. HANDLING COMMON OBJECTIONS (3-4 objections with specific response scripts)\n"
        f"6. TOTAL COMPENSATION ALTERNATIVES (signing bonus, PTO, remote work, review cycle)\n"
        f"7. MINDSET NOTES (reframe negotiation anxiety; what to remember)\n"
        f"8. WHAT TO DO AFTER THE CALL (follow-up email template)\n"
    )

    print(f"\n{'='*60}")
    print(f"SALARY NEGOTIATION: {args.role}")
    print(f"Offer: ${args.offer:,.0f} → Target: ${args.target:,.0f}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# LOAN COMPARISON
# ---------------------------------------------------------------------------

def cmd_loans(args: argparse.Namespace) -> None:
    system = (
        "You are a financial educator specializing in consumer lending and debt analysis. "
        "You compare loan options by calculating total cost of borrowing (not just monthly "
        "payment), present findings in clear tables, and make honest recommendations based on "
        "the person's stated priority. You explain the trade-offs between term length, rate, "
        "and monthly payment. You always warn about origination fees and prepayment penalties."
    )

    if args.options:
        options_text = parse_key_value_list(args.options)
    elif args.file:
        options_text = read_file(args.file)
    else:
        print("Error: Provide loan options via --options or --file.", file=sys.stderr)
        sys.exit(1)

    purpose_note = f"\nLoan purpose: {args.purpose}" if args.purpose else ""
    priority_note = f"\nPriority: {args.priority}" if args.priority else "\nPriority: lowest total cost"

    user_message = (
        f"Compare the following loan options:"
        f"{purpose_note}"
        f"{priority_note}\n\n"
        f"Loan amount: ${args.amount:,.0f}\n"
        f"Loan term: {args.term} months\n"
        f"Options (lender: APR):\n{options_text}\n\n"
        f"For each loan calculate:\n"
        f"- Monthly payment\n"
        f"- Total interest paid\n"
        f"- Total cost (principal + interest)\n\n"
        f"Also provide:\n"
        f"1. SIDE-BY-SIDE COMPARISON TABLE\n"
        f"2. INTEREST SPREAD ANALYSIS (dollar difference between best and worst option)\n"
        f"3. RECOMMENDATION based on stated priority\n"
        f"4. RATE SENSITIVITY (how much does 0.5% APR difference matter in dollars?)\n"
        f"5. QUESTIONS TO ASK EACH LENDER (origination fees, prepayment penalties, autopay discount)\n"
        f"6. CREDIT SCORE IMPACT NOTES (how to potentially qualify for better rates)\n"
        f"\n{FINANCE_DISCLAIMER}\n"
    )

    print(f"\n{'='*60}")
    print("LOAN COMPARISON")
    print(f"Amount: ${args.amount:,.0f} | Term: {args.term} months")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CREDIT CARD OPTIMIZER
# ---------------------------------------------------------------------------

def cmd_credit_cards(args: argparse.Namespace) -> None:
    system = (
        "You are a personal finance specialist in credit card strategy and rewards optimization. "
        "You analyze spending patterns against card reward structures to maximize return. "
        "You calculate actual dollar rewards per category, annual fee break-even analysis, "
        "and create a card-to-category assignment strategy. You are honest about when simpler "
        "strategies (one flat-rate card) outperform complex multi-card setups. You never "
        "recommend carrying a balance — interest eliminates all rewards value."
    )

    spending_text = parse_key_value_list(args.spending) if args.spending else ""
    cards_text = args.cards or "Not specified"

    if args.file:
        spending_text = read_file(args.file)

    user_message = (
        f"Optimize credit card strategy for the following:\n\n"
        f"Monthly spending by category:\n{spending_text}\n\n"
        f"Current cards: {cards_text}\n\n"
        f"Provide:\n"
        f"1. OPTIMIZED CARD ASSIGNMENT TABLE (category | monthly spend | best card | reward rate | monthly rewards)\n"
        f"2. ANNUAL REWARDS VALUE (before and after annual fees)\n"
        f"3. ANNUAL FEE BREAK-EVEN ANALYSIS (for any card with annual fees)\n"
        f"4. COMPARISON: optimized multi-card vs. simple flat-rate approach\n"
        f"5. CREDIT SCORE NOTES (utilization, account age considerations)\n"
        f"6. MISSING CARD OPPORTUNITIES (categories where a different card would earn significantly more)\n"
        f"7. IMPLEMENTATION GUIDE (which card to use for each category, week 1 actions)\n"
        f"\n{FINANCE_DISCLAIMER}\n"
    )

    print(f"\n{'='*60}")
    print("CREDIT CARD OPTIMIZER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# RETIREMENT PLANNER
# ---------------------------------------------------------------------------

def cmd_retirement(args: argparse.Namespace) -> None:
    system = (
        "You are a retirement planning educator with expertise in tax-advantaged accounts, "
        "investment strategy, and long-term financial planning. You project retirement outcomes "
        "using standard assumptions (7% real return, inflation-adjusted analysis), identify gaps "
        "between current trajectory and goals, and provide actionable contribution strategies. "
        "You explain account types (401k, Roth IRA, traditional IRA) with tax implications. "
        "You always note that projections are estimates and recommend working with a CFP."
    )

    employer_match_note = f"\nEmployer 401k match: {args.employer_match}" if args.employer_match else ""
    current_contribution_note = (
        f"\nCurrent retirement contribution: {args.current_contribution}" if args.current_contribution else ""
    )
    income_need_note = (
        f"\nTarget retirement income: ${args.retirement_income:,.0f}/year"
        if args.retirement_income
        else ""
    )

    user_message = (
        f"Create a retirement projection and action plan for:\n\n"
        f"Current age: {args.age}\n"
        f"Current retirement savings: ${args.savings:,.0f}\n"
        f"Annual income: ${args.income:,.0f}\n"
        f"Target retirement age: {args.target_age}"
        f"{employer_match_note}"
        f"{current_contribution_note}"
        f"{income_need_note}\n\n"
        f"Provide:\n"
        f"1. RETIREMENT TARGET (nest egg needed based on the 4% withdrawal rule, inflation-adjusted)\n"
        f"2. CURRENT TRAJECTORY (projection at current contribution rate)\n"
        f"3. GAP ANALYSIS (shortfall or surplus; percentage gap)\n"
        f"4. CONTRIBUTION SCENARIOS (what happens at 6%, 10%, 15% contribution rate)\n"
        f"5. ACCOUNT PRIORITY STRATEGY (401k match → Roth IRA → max 401k → taxable)\n"
        f"6. TAX CONSIDERATION (traditional vs. Roth analysis for this income level)\n"
        f"7. SAVINGS MILESTONES (target balance at 40, 45, 50, 55, 60, retirement age)\n"
        f"8. SINGLE BEST ACTION (most impactful change to make right now)\n"
        f"\nAssume 7% average annual investment return. Show key calculations.\n"
        f"\n{FINANCE_DISCLAIMER}\n"
    )

    print(f"\n{'='*60}")
    print("RETIREMENT PLANNER")
    print(f"Age: {args.age} | Savings: ${args.savings:,.0f} | Income: ${args.income:,.0f}")
    print(f"Target retirement age: {args.target_age}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered financial advisory tools (educational use only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- invest ---
    iv = subparsers.add_parser("invest", help="Explain an investment concept or strategy")
    iv_source = iv.add_mutually_exclusive_group()
    iv_source.add_argument("topic", nargs="?", help="Investment topic or question")
    iv_source.add_argument("--file", help="Path to file with topic/question")
    iv.add_argument(
        "--level",
        choices=["beginner", "intermediate", "advanced"],
        help="Explanation level",
    )

    # --- tax-deductions ---
    td = subparsers.add_parser("tax-deductions", help="Find applicable tax deductions for your situation")
    td_source = td.add_mutually_exclusive_group()
    td_source.add_argument("--situation", help="Description of your tax situation")
    td_source.add_argument("--file", help="Path to file describing your situation")
    td.add_argument("--year", help="Tax year (e.g. 2024)")
    td.add_argument(
        "--filing-status",
        choices=["single", "married-filing-jointly", "married-filing-separately", "head-of-household"],
        help="Filing status",
    )

    # --- negotiate ---
    ng = subparsers.add_parser("negotiate", help="Get a salary negotiation strategy and scripts")
    ng.add_argument("--role", required=True, help="Job title/role")
    ng.add_argument("--offer", type=float, required=True, help="Current salary offer")
    ng.add_argument("--target", type=float, required=True, help="Target salary")
    ng.add_argument("--location", required=True, help="City/region for market context")
    ng.add_argument("--experience", help="Years of relevant experience")
    ng.add_argument("--competing-offer", help="Competing offer amount and company (if any)")
    ng.add_argument("--context", help="Additional context as text or path to .txt file")

    # --- loans ---
    ln = subparsers.add_parser("loans", help="Compare loan options side-by-side")
    ln.add_argument("--amount", type=float, required=True, help="Loan amount")
    ln.add_argument("--term", type=int, required=True, help="Loan term in months")
    ln_source = ln.add_mutually_exclusive_group()
    ln_source.add_argument(
        "--options",
        help="Loan options as 'Lender:rate%,Lender:rate%' (e.g. 'Bank A:6.5%,Credit Union:5.9%')",
    )
    ln_source.add_argument("--file", help="Path to file with loan options")
    ln.add_argument("--purpose", help="Loan purpose (e.g. 'debt consolidation', 'auto')")
    ln.add_argument(
        "--priority",
        choices=["lowest-payment", "lowest-total-cost", "shortest-term"],
        default="lowest-total-cost",
        help="Optimization priority (default: lowest-total-cost)",
    )

    # --- credit-cards ---
    cc = subparsers.add_parser("credit-cards", help="Optimize your credit card rewards strategy")
    cc_source = cc.add_mutually_exclusive_group()
    cc_source.add_argument(
        "--spending",
        help="Monthly spending as 'category:amount,category:amount'",
    )
    cc_source.add_argument("--file", help="Path to file with spending data")
    cc.add_argument("--cards", help="Current cards as a comma-separated list")

    # --- retirement ---
    rt = subparsers.add_parser("retirement", help="Build a retirement projection and savings plan")
    rt.add_argument("--age", type=int, required=True, help="Current age")
    rt.add_argument("--savings", type=float, required=True, help="Current total retirement savings")
    rt.add_argument("--income", type=float, required=True, help="Annual income")
    rt.add_argument("--target-age", type=int, required=True, help="Target retirement age")
    rt.add_argument("--employer-match", help="Employer 401k match (e.g. '4% of salary')")
    rt.add_argument("--current-contribution", help="Current contribution rate or amount (e.g. '6% of salary')")
    rt.add_argument("--retirement-income", type=float, help="Desired annual income in retirement (today's dollars)")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "invest" and not args.topic and not args.file:
        print("Error: Provide a topic as a positional argument or via --file.", file=sys.stderr)
        sys.exit(1)

    if args.command == "tax-deductions" and not args.situation and not args.file:
        print("Error: Provide situation description via --situation or --file.", file=sys.stderr)
        sys.exit(1)

    dispatch = {
        "invest": cmd_invest,
        "tax-deductions": cmd_tax_deductions,
        "negotiate": cmd_negotiate,
        "loans": cmd_loans,
        "credit-cards": cmd_credit_cards,
        "retirement": cmd_retirement,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
