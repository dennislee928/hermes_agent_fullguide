#!/usr/bin/env python3
"""
business_tools.py — Business and financial tools using Hermes via Ollama

Usage:
  python business_tools.py summarize-contract --file contract.txt
  python business_tools.py summarize-contract --file contract.txt --focus "payment terms, termination, IP"
  python business_tools.py invoice --client "Acme Corp" --items "Design:40hrs:$150,PM:10hrs:$120" --due-days 30
  python business_tools.py categorize-expenses --file expenses.txt
  python business_tools.py categorize-expenses --file expenses.txt --categories "Travel,Software,Meals,Marketing"
  python business_tools.py validate-idea --idea "A subscription app for remote workers" --market B2C
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


def cmd_summarize_contract(args: argparse.Namespace) -> None:
    """Summarize a contract in plain language with red flag analysis."""
    system_prompt = (
        "You are a business contract analyst with expertise in commercial and SaaS agreements. "
        "Translate dense legal language into clear, plain-English summaries. "
        "Always identify: key commercial terms, obligations, termination conditions, "
        "liability limitations, and data/IP provisions. "
        "Flag unfavorable or unusual clauses explicitly as RED FLAGS with severity (High/Medium). "
        "Provide a negotiation recommendation for each red flag. "
        "Important disclaimer: always note this is an initial review, not legal advice."
    )

    contract_text = read_file(args.file)

    user_message = (
        f"Summarize this contract in plain English:\n\n"
        f"Contract text:\n---\n{contract_text}\n---\n\n"
    )

    if args.focus:
        user_message += f"Pay special attention to these areas: {args.focus}\n\n"

    user_message += (
        "Format the output as:\n"
        "1. QUICK OVERVIEW (contract type, parties, term, risk level)\n"
        "2. KEY TERMS (table: Term | Detail)\n"
        "3. RED FLAGS (numbered list with severity, explanation, and negotiation tip)\n"
        "4. OBLIGATIONS SUMMARY (what you must do / what they must do)\n"
        "5. DISCLAIMER (note this is for initial review only)\n"
    )

    print("\n--- Contract Summary ---\n")
    stream_chat(system_prompt, user_message)


def cmd_invoice(args: argparse.Namespace) -> None:
    """Generate a professional invoice."""
    system_prompt = (
        "You are a professional invoicing assistant. "
        "Generate clear, complete invoice text with correct arithmetic. "
        "Always include: invoice number, dates, line items table, subtotal, tax (if applicable), "
        "total due, payment terms, and payment instructions. "
        "Calculate all totals correctly. "
        "Flag any items where the input format was unclear."
    )

    # Parse items: each item is "Description:qty_or_hrs:unit_price"
    items_formatted = []
    if args.items:
        for item in args.items.split(","):
            item = item.strip()
            parts = item.split(":")
            if len(parts) == 3:
                items_formatted.append(
                    f"  - {parts[0].strip()} | Qty/Hrs: {parts[1].strip()} | Unit Price: {parts[2].strip()}"
                )
            else:
                items_formatted.append(f"  - {item}")

    items_text = "\n".join(items_formatted) if items_formatted else args.items

    user_message = (
        f"Generate a professional invoice with these details:\n"
        f"- Client: {args.client}\n"
        f"- Payment terms: Net {args.due_days} days\n"
    )

    if args.invoice_num:
        user_message += f"- Invoice number: {args.invoice_num}\n"

    if args.sender:
        user_message += f"- Sender/Freelancer: {args.sender}\n"

    user_message += f"\nLine items:\n{items_text}\n"

    if args.tax:
        user_message += f"\nApply {args.tax}% sales tax to the subtotal.\n"

    if args.currency:
        user_message += f"\nCurrency: {args.currency}\n"

    if args.notes:
        user_message += f"\nAdditional notes: {args.notes}\n"

    user_message += (
        "\nFormat as a complete invoice with:\n"
        "1. Header (From, To, Invoice #, Date, Due Date)\n"
        "2. Line items table: | Description | Qty/Hrs | Unit Price | Amount |\n"
        "3. Subtotal, Tax (if applicable), TOTAL DUE\n"
        "4. Payment instructions section\n"
        "5. Thank you note"
    )

    print(f"\n--- Invoice: {args.client} ---\n")
    stream_chat(system_prompt, user_message)


def cmd_categorize_expenses(args: argparse.Namespace) -> None:
    """Categorize a list of expenses."""
    system_prompt = (
        "You are a business expense categorization expert with knowledge of accounting categories "
        "and IRS/business expense rules. "
        "Categorize each expense accurately based on merchant name, description, and amount. "
        "Flag personal expenses explicitly — never categorize personal spending as business. "
        "Flag ambiguous items for review. "
        "Produce a clean categorized table, a flagged items table, and a summary by category. "
        "Use standard business expense categories unless specific categories are provided."
    )

    expenses_text = read_file(args.file)

    default_categories = (
        "Travel (Airfare, Hotel, Ground), Meals & Entertainment, Software/SaaS, "
        "Cloud Infrastructure, Office Supplies, Marketing/Advertising, "
        "Professional Services, Equipment, Other"
    )
    categories = args.categories or default_categories

    user_message = (
        f"Categorize these business expenses.\n"
        f"Use these categories: {categories}\n\n"
        f"Expense list:\n---\n{expenses_text}\n---\n\n"
        f"Format the output as:\n"
        f"1. CATEGORIZED EXPENSES table: | Date | Merchant | Amount | Category |\n"
        f"2. FLAGGED ITEMS table (personal expenses, ambiguous items): | Date | Merchant | Amount | Flag Reason |\n"
        f"3. SUMMARY BY CATEGORY table: | Category | Total |\n"
        f"4. GRAND TOTAL (business expenses only)"
    )

    print("\n--- Expense Categorization ---\n")
    stream_chat(system_prompt, user_message)


def cmd_validate_idea(args: argparse.Namespace) -> None:
    """Validate a business idea with structured analysis."""
    system_prompt = (
        "You are a veteran startup advisor and business strategist. "
        "Provide honest, rigorous business idea validation — not cheerleading. "
        "Apply frameworks: problem/solution fit, market sizing (TAM/SAM/SOM), "
        "competitive landscape, key assumptions, and risk analysis. "
        "Identify the most critical assumptions to test before building. "
        "Be direct about weaknesses while acknowledging genuine strengths. "
        "Give a concrete recommended next step that is low-cost and fast."
    )

    user_message = (
        f"Validate this business idea:\n"
        f"- Idea: {args.idea}\n"
        f"- Target market type: {args.market}\n"
        f"- Stage: {args.stage}\n"
    )

    if args.founder_background:
        user_message += f"- Founder background: {args.founder_background}\n"

    if args.devil_advocate:
        user_message += "\nBe especially rigorous in identifying failure modes and weaknesses.\n"

    user_message += (
        "\nStructure your analysis as:\n"
        "1. PROBLEM CLARITY (is the problem real and significant?)\n"
        "2. MARKET OPPORTUNITY (rough TAM/SAM estimate, comparable markets)\n"
        "3. KEY ASSUMPTIONS TO TEST (ranked by importance, with validation approach)\n"
        "4. RISKS & RED FLAGS (numbered, with mitigation suggestions)\n"
        "5. OVERALL VERDICT (1-2 sentences + recommended immediate next step)"
    )

    print(f"\n--- Business Idea Validation ---\n")
    stream_chat(system_prompt, user_message)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Business and financial tools with Hermes",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- summarize-contract ---
    contract_p = subparsers.add_parser(
        "summarize-contract", help="Summarize a contract in plain language"
    )
    contract_p.add_argument("--file", required=True, help="Path to contract file")
    contract_p.add_argument(
        "--focus", default="", help='Specific areas to focus on, e.g. "IP, payment, termination"'
    )
    contract_p.set_defaults(func=cmd_summarize_contract)

    # --- invoice ---
    invoice_p = subparsers.add_parser("invoice", help="Generate a professional invoice")
    invoice_p.add_argument("--client", required=True, help="Client name")
    invoice_p.add_argument(
        "--items",
        required=True,
        help='Line items as "Description:qty:price" comma-separated, e.g. "Design:40hrs:$150,PM:10hrs:$120"',
    )
    invoice_p.add_argument("--due-days", type=int, default=30, help="Payment due in N days")
    invoice_p.add_argument("--invoice-num", default="", help="Invoice number")
    invoice_p.add_argument("--sender", default="", help="Your name/company")
    invoice_p.add_argument("--tax", type=float, default=0.0, help="Tax percentage to apply")
    invoice_p.add_argument("--currency", default="USD", help="Currency code")
    invoice_p.add_argument("--notes", default="", help="Additional notes for the invoice")
    invoice_p.set_defaults(func=cmd_invoice)

    # --- categorize-expenses ---
    exp_p = subparsers.add_parser("categorize-expenses", help="Categorize business expenses")
    exp_p.add_argument("--file", required=True, help="Path to expense list file (CSV, text, etc.)")
    exp_p.add_argument(
        "--categories",
        default="",
        help="Custom category list (comma-separated)",
    )
    exp_p.set_defaults(func=cmd_categorize_expenses)

    # --- validate-idea ---
    idea_p = subparsers.add_parser("validate-idea", help="Validate a business idea")
    idea_p.add_argument("--idea", required=True, help="Business idea description")
    idea_p.add_argument(
        "--market",
        default="B2C",
        choices=["B2C", "B2B", "B2B2C", "marketplace", "other"],
        help="Target market type",
    )
    idea_p.add_argument(
        "--stage",
        default="idea stage",
        choices=["idea stage", "pre-revenue", "revenue", "scaling"],
        help="Current stage of the idea",
    )
    idea_p.add_argument("--founder-background", default="", help="Relevant founder background")
    idea_p.add_argument(
        "--devil-advocate",
        action="store_true",
        help="Request extra-critical analysis",
    )
    idea_p.set_defaults(func=cmd_validate_idea)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
