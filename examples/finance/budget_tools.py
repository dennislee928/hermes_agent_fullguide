#!/usr/bin/env python3
"""
budget_tools.py — Hermes-powered budget tools: personal budget analyzer,
subscription audit, emergency fund calculator, and side hustle tracker.

DISCLAIMER: This tool is for educational and informational purposes only.
It is not financial advice. Consult a licensed financial professional for
personalized financial guidance.

Usage:
  python budget_tools.py analyze --income 5000 --expenses "rent:1500,food:600,transport:200,subscriptions:150"
  python budget_tools.py analyze --income 5000 --file expenses.txt
  python budget_tools.py subscriptions --list "Netflix:15,Spotify:10,Gym:40,iCloud:3"
  python budget_tools.py subscriptions --file subscriptions.txt
  python budget_tools.py emergency-fund --monthly-expenses 3200 --months 6
  python budget_tools.py side-hustle --income 800 --expenses "tools:50,platform:15" --hours 20
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"

FINANCE_DISCLAIMER = (
    "[DISCLAIMER: This analysis is for educational purposes only and does not constitute "
    "financial advice. Consult a licensed financial advisor for personalized guidance.]"
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
    """Convert 'key:value,key:value' format to a formatted bullet list."""
    items = []
    for item in raw.split(","):
        item = item.strip()
        if ":" in item:
            k, v = item.split(":", 1)
            items.append(f"  {k.strip()}: ${v.strip()}")
        else:
            items.append(f"  {item}")
    return "\n".join(items)


# ---------------------------------------------------------------------------
# BUDGET ANALYZER
# ---------------------------------------------------------------------------

def cmd_analyze(args: argparse.Namespace) -> None:
    system = (
        "You are a personal finance coach and certified financial planner. You analyze personal "
        "budgets against established frameworks (50/30/20 rule, zero-based budgeting) and provide "
        "specific, actionable recommendations. You don't just report numbers — you interpret them "
        "and explain what they mean for the person's financial health. You identify the highest-"
        "leverage changes first. You are honest, direct, and encouraging without being dismissive "
        "of genuine financial challenges."
    )

    if args.file:
        expenses_text = f"Expenses from file:\n{read_file(args.file)}"
    elif args.expenses:
        expenses_text = f"Monthly expenses:\n{parse_key_value_list(args.expenses)}"
    else:
        print("Error: Provide expenses via --expenses or --file.", file=sys.stderr)
        sys.exit(1)

    goal_note = f"\nFinancial goals: {args.goals}" if args.goals else ""

    user_message = (
        f"Analyze the following monthly budget:\n\n"
        f"Monthly income (after tax): ${args.income}\n"
        f"{expenses_text}"
        f"{goal_note}\n\n"
        f"Provide:\n"
        f"1. BUDGET OVERVIEW (total tracked expenses, unaccounted amount)\n"
        f"2. 50/30/20 FRAMEWORK COMPARISON (table: category | your spending | target | status)\n"
        f"3. CATEGORIZATION (assign each expense to Needs/Wants/Savings)\n"
        f"4. PRIORITY ISSUES (ranked by financial impact — most important first)\n"
        f"5. ACTIONABLE RECOMMENDATIONS (specific, numbered, achievable changes)\n"
        f"6. POSITIVE OBSERVATIONS (what is going well)\n"
        f"7. 30-DAY QUICK WIN (one thing to do this month for the biggest impact)\n"
    )

    print(f"\n{'='*60}")
    print(f"BUDGET ANALYSIS")
    print(f"Monthly Income: ${args.income}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SUBSCRIPTION AUDIT
# ---------------------------------------------------------------------------

def cmd_subscriptions(args: argparse.Namespace) -> None:
    system = (
        "You are a personal finance coach specializing in recurring expense optimization. "
        "You conduct honest, direct subscription audits — identifying redundancies, calculating "
        "true annual costs, and providing a prioritized cancellation list with reasoning. "
        "You give opinionated recommendations, not just neutral observations. You calculate "
        "potential annual savings. You know common subscription categories (streaming, software, "
        "fitness, cloud storage, food) and their typical alternatives."
    )

    if args.file:
        sub_text = f"Subscription list from file:\n{read_file(args.file)}"
    elif args.list:
        sub_text = f"Monthly subscriptions:\n{parse_key_value_list(args.list)}"
    else:
        print("Error: Provide subscriptions via --list or --file.", file=sys.stderr)
        sys.exit(1)

    user_message = (
        f"Conduct a full subscription audit for:\n\n"
        f"{sub_text}\n\n"
        f"Provide:\n"
        f"1. TOTAL MONTHLY AND ANNUAL COST\n"
        f"2. IMMEDIATE CANCELLATIONS (clear redundancies or obviously unused services)\n"
        f"3. CONSOLIDATION OPPORTUNITIES (overlapping services in same category)\n"
        f"4. EVALUATE CAREFULLY (services with ambiguous value — include break-even analysis)\n"
        f"5. RETAIN AS-IS (well-justified subscriptions)\n"
        f"6. NEGOTIATION TIPS (services where retention offers are common)\n"
        f"7. SUMMARY: potential monthly and annual savings\n"
        f"8. ACTION PLAN (week-by-week steps to implement the audit)\n"
    )

    print(f"\n{'='*60}")
    print("SUBSCRIPTION AUDIT")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# EMERGENCY FUND CALCULATOR
# ---------------------------------------------------------------------------

def cmd_emergency_fund(args: argparse.Namespace) -> None:
    system = (
        "You are a personal finance educator specializing in financial resilience planning. "
        "You calculate personalized emergency fund targets based on individual risk profiles — "
        "employment stability, dependents, income variability, and specialization of field. "
        "You apply the standard 3-6 month rule as a baseline and adjust based on risk factors. "
        "You provide tiered targets, realistic contribution timelines, and specific guidance "
        "on where to keep the emergency fund for optimal yield and liquidity."
    )

    employment_note = f"\nEmployment type: {args.employment}" if args.employment else ""
    dependents_note = f"\nDependents: {args.dependents}" if args.dependents else ""
    current_savings_note = f"\nCurrent emergency savings: ${args.current_savings}" if args.current_savings else ""
    monthly_save_note = f"\nMonthly savings capacity: ${args.monthly_savings}" if args.monthly_savings else ""

    user_message = (
        f"Calculate a personalized emergency fund plan for:\n\n"
        f"Monthly essential expenses: ${args.monthly_expenses}\n"
        f"Standard target months: {args.months}"
        f"{employment_note}"
        f"{dependents_note}"
        f"{current_savings_note}"
        f"{monthly_save_note}\n\n"
        f"Provide:\n"
        f"1. RISK PROFILE ASSESSMENT (analyze each risk factor provided)\n"
        f"2. RECOMMENDED TARGET (adjusted months based on risk profile, with justification)\n"
        f"3. TIERED TARGETS (Tier 1: minimum safety / Tier 2: recommended / Tier 3: optimal)\n"
        f"4. TIMELINE TO REACH EACH TIER (based on monthly savings capacity)\n"
        f"5. ACCELERATED OPTIONS (ways to reach the target faster)\n"
        f"6. WHAT COUNTS AS EMERGENCY EXPENSES (what to include/exclude from the base calculation)\n"
        f"7. WHERE TO KEEP IT (high-yield savings account guidance, current rates)\n"
        f"8. FIRST STEP (the single most important thing to do right now)\n"
    )

    print(f"\n{'='*60}")
    print("EMERGENCY FUND CALCULATOR")
    print(f"Monthly Expenses: ${args.monthly_expenses} | Target: {args.months} months")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SIDE HUSTLE TRACKER
# ---------------------------------------------------------------------------

def cmd_side_hustle(args: argparse.Namespace) -> None:
    system = (
        "You are a small business financial coach who helps freelancers and side hustlers "
        "understand the true profitability of their work. You calculate true hourly rates "
        "after taxes and expenses, identify profit leaks, surface overlooked tax obligations, "
        "and provide specific scaling recommendations. You are honest about the real numbers — "
        "including self-employment tax, which many side hustlers underestimate. You identify "
        "the highest-leverage changes to increase profitability without just adding more hours."
    )

    if args.file:
        expense_text = f"Expenses from file:\n{read_file(args.file)}"
    elif args.expenses:
        expense_text = f"Monthly business expenses:\n{parse_key_value_list(args.expenses)}"
    else:
        expense_text = "Monthly business expenses: Not specified"

    hustle_type_note = f"\nSide hustle type: {args.type}" if args.type else ""
    main_income_note = f"\nMain job annual income: ${args.main_income}" if args.main_income else ""

    user_message = (
        f"Analyze the following side hustle financials:"
        f"{hustle_type_note}\n\n"
        f"Monthly revenue: ${args.income}\n"
        f"{expense_text}\n"
        f"Monthly hours worked: {args.hours}"
        f"{main_income_note}\n\n"
        f"Provide:\n"
        f"1. FINANCIAL OVERVIEW (revenue, all expenses, gross profit)\n"
        f"2. TAX OBLIGATIONS (self-employment tax, estimated federal income tax, quarterly payment schedule)\n"
        f"3. AFTER-TAX PROFIT (monthly and annual)\n"
        f"4. TRUE HOURLY RATE (after all expenses and taxes)\n"
        f"5. COMPARISON CONTEXT (vs. main job effective hourly rate if provided)\n"
        f"6. TOP PROFIT LEAKS (where money is being lost most — ranked)\n"
        f"7. SCALING ANALYSIS (increase rates vs. more hours — which has higher ROI?)\n"
        f"8. TAX ACTION ITEMS (quarterly payments, deductible items they may be missing)\n"
        f"9. GROWTH OPPORTUNITIES (3 specific ways to improve profitability)\n"
    )

    print(f"\n{'='*60}")
    print("SIDE HUSTLE TRACKER")
    print(f"Monthly Revenue: ${args.income} | Hours: {args.hours}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered budget and personal finance tools (educational use only).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- analyze ---
    an = subparsers.add_parser("analyze", help="Analyze monthly budget against 50/30/20 framework")
    an.add_argument("--income", type=float, required=True, help="Monthly after-tax income")
    an_source = an.add_mutually_exclusive_group()
    an_source.add_argument(
        "--expenses",
        help="Expenses as 'category:amount,category:amount' (e.g. 'rent:1500,food:600')",
    )
    an_source.add_argument("--file", help="Path to file listing expenses")
    an.add_argument("--goals", help="Financial goals (e.g. 'pay off debt, save for house')")

    # --- subscriptions ---
    sb = subparsers.add_parser("subscriptions", help="Audit your active subscriptions")
    sb_source = sb.add_mutually_exclusive_group()
    sb_source.add_argument(
        "--list",
        help="Subscriptions as 'Service:amount,Service:amount' (e.g. 'Netflix:15,Spotify:10')",
    )
    sb_source.add_argument("--file", help="Path to file listing subscriptions")

    # --- emergency-fund ---
    ef = subparsers.add_parser("emergency-fund", help="Calculate your emergency fund target")
    ef.add_argument("--monthly-expenses", type=float, required=True, help="Monthly essential expenses (not total spending)")
    ef.add_argument("--months", type=int, default=6, help="Target months of coverage (default: 6)")
    ef.add_argument(
        "--employment",
        help="Employment type (e.g. 'salaried employee', 'freelancer', 'contractor')",
    )
    ef.add_argument("--dependents", help="Number and type of dependents (e.g. '2 children')")
    ef.add_argument("--current-savings", type=float, help="Current emergency fund balance")
    ef.add_argument("--monthly-savings", type=float, help="Amount you can save per month toward this goal")

    # --- side-hustle ---
    sh = subparsers.add_parser("side-hustle", help="Analyze side hustle profitability")
    sh.add_argument("--income", type=float, required=True, help="Monthly gross revenue")
    sh.add_argument("--hours", type=float, required=True, help="Hours worked per month")
    sh_source = sh.add_mutually_exclusive_group()
    sh_source.add_argument(
        "--expenses",
        help="Business expenses as 'category:amount,category:amount'",
    )
    sh_source.add_argument("--file", help="Path to file listing business expenses")
    sh.add_argument("--type", help="Type of side hustle (e.g. 'freelance writing', 'Etsy shop')")
    sh.add_argument("--main-income", type=float, help="Annual main job income (for tax bracket context)")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "analyze": cmd_analyze,
        "subscriptions": cmd_subscriptions,
        "emergency-fund": cmd_emergency_fund,
        "side-hustle": cmd_side_hustle,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
