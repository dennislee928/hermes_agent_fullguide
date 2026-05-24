#!/usr/bin/env python3
"""
wellness_tools.py — Hermes-powered wellness tools: symptom diary analyzer,
medication interaction checker, nutrition label decoder, and allergy recipe adapter.

IMPORTANT: All output is for informational and educational purposes only.
This is NOT medical advice. Always consult qualified healthcare professionals.

Usage:
  python wellness_tools.py symptoms "headache for 3 days, mild fever, fatigue"
  python wellness_tools.py symptoms --file symptom_diary.txt
  python wellness_tools.py medications "ibuprofen, warfarin"
  python wellness_tools.py nutrition --label "Calories 250, Fat 12g, Sodium 480mg, Sugar 8g"
  python wellness_tools.py nutrition --file nutrition_label.txt
  python wellness_tools.py adapt-recipe --file pasta.txt --avoid "gluten, dairy"
  python wellness_tools.py adapt-recipe --recipe "Chicken Alfredo" --avoid "dairy"
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"

MEDICAL_DISCLAIMER = (
    "\n\n[DISCLAIMER: This output is for educational and informational purposes only. "
    "It is NOT medical advice, diagnosis, or treatment. Always consult a qualified "
    "healthcare provider, pharmacist, or medical professional for personal health decisions.]"
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
    except PermissionError:
        print(f"Error: Cannot read file (permission denied): {path}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# SYMPTOM DIARY ANALYZER
# ---------------------------------------------------------------------------

def cmd_symptoms(args: argparse.Namespace) -> None:
    system = (
        "You are a health information assistant trained to help people identify patterns in "
        "their symptom data and communicate more effectively with their healthcare providers. "
        "You are NOT a doctor and do NOT diagnose conditions. You analyze symptom entries for "
        "patterns, trends, timing, and correlations with lifestyle factors. You always recommend "
        "appropriate medical consultation, and you clearly flag any symptom combinations that "
        "warrant prompt medical attention. You present findings in a structured format suitable "
        "for sharing with a healthcare provider."
    )

    if args.file:
        symptom_data = read_file(args.file)
        source_label = f"from file: {args.file}"
    else:
        symptom_data = args.symptoms
        source_label = "inline input"

    period_note = f"\nTracking period: {args.period}" if args.period else ""

    user_message = (
        f"Analyze the following symptom diary data ({source_label}) for patterns and insights."
        f"{period_note}\n\n"
        f"SYMPTOM DATA:\n{symptom_data}\n\n"
        f"Provide:\n"
        f"1. SYMPTOM OVERVIEW (list all symptoms noted with frequency/severity pattern)\n"
        f"2. PATTERN OBSERVATIONS (timing, progression, clusters, triggers noted)\n"
        f"3. SYMPTOM FLAGS (any combinations that warrant prompt medical attention — be specific)\n"
        f"4. WHAT TO TELL YOUR DOCTOR (concise summary for a medical appointment)\n"
        f"5. TRACKING RECOMMENDATIONS (what additional data would be helpful to log)\n"
        f"6. IMPORTANT DISCLAIMER (remind user this is informational, not medical advice)\n"
    )

    print(f"\n{'='*60}")
    print("SYMPTOM DIARY ANALYSIS")
    print(f"{'='*60}\n")
    print(MEDICAL_DISCLAIMER.strip())
    print()
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# MEDICATION INTERACTION CHECKER
# ---------------------------------------------------------------------------

def cmd_medications(args: argparse.Namespace) -> None:
    system = (
        "You are a health information assistant providing educational information about "
        "medication interactions. You draw on pharmacological knowledge to explain known or "
        "potential interactions between medications, including prescription drugs, OTC medications, "
        "and supplements. You classify interaction severity (mild/moderate/severe), explain the "
        "mechanism in plain language, and state the recommended action. You ALWAYS direct users "
        "to consult their pharmacist for a comprehensive review, as pharmacists are the "
        "appropriate professionals for drug interaction counseling. You are cautious: if in doubt, "
        "you note the uncertainty and recommend professional verification."
    )

    if args.file:
        med_list = read_file(args.file)
        source_label = f"from file: {args.file}"
    else:
        med_list = args.medications
        source_label = "inline input"

    user_message = (
        f"Provide an educational overview of potential interactions between the following "
        f"medications/supplements ({source_label}):\n\n"
        f"{med_list}\n\n"
        f"Structure the response as:\n"
        f"1. MEDICATIONS REVIEWED (confirm what you're analyzing)\n"
        f"2. INTERACTION SUMMARY (how many interactions of note found; overall severity)\n"
        f"3. FOR EACH INTERACTION: name the pair, severity, mechanism (plain language), "
        f"   clinical significance, and recommended action\n"
        f"4. NO SIGNIFICANT INTERACTIONS FOUND (list pairs with no notable interaction)\n"
        f"5. IMPORTANT DISCLAIMER (pharmacist consultation required for complete review)\n\n"
        f"Severity classification: Mild | Mild-Moderate | Moderate | Moderate-Severe | Severe\n"
    )

    print(f"\n{'='*60}")
    print("MEDICATION INTERACTION OVERVIEW")
    print(f"{'='*60}\n")
    print(MEDICAL_DISCLAIMER.strip())
    print()
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# NUTRITION LABEL DECODER
# ---------------------------------------------------------------------------

def cmd_nutrition(args: argparse.Namespace) -> None:
    system = (
        "You are a registered dietitian's assistant and nutrition educator. You decode nutrition "
        "labels into plain-language insight — contextualizing every number against daily "
        "recommended values, typical dietary guidelines, and real-world comparisons. You highlight "
        "the most important numbers for health (added sugar, sodium, fiber, saturated fat), "
        "provide a 'marketing reality check' when product branding may be misleading, and give "
        "a clear, honest verdict. You are specific, not generic."
    )

    if args.file:
        label_data = read_file(args.file)
        source_label = f"from file: {args.file}"
    else:
        label_data = args.label
        source_label = "inline input"

    product_note = f"\nProduct name: {args.product}" if args.product else ""
    goal_note = f"\nUser health goal: {args.goal}" if args.goal else ""

    user_message = (
        f"Decode and analyze the following nutrition label ({source_label})."
        f"{product_note}"
        f"{goal_note}\n\n"
        f"NUTRITION LABEL DATA:\n{label_data}\n\n"
        f"Provide:\n"
        f"1. OVERVIEW (what this product is and calorie context per serving and per package)\n"
        f"2. MACRONUTRIENT ANALYSIS (fat, carbs, protein — what the numbers mean)\n"
        f"3. SUGAR ANALYSIS (total vs. added sugar — compare to daily guidelines)\n"
        f"4. SODIUM & MICRONUTRIENTS (flag if high; contextualize vitamins/minerals)\n"
        f"5. MARKETING REALITY CHECK (does the branding/name match the actual nutrition?)\n"
        f"6. VERDICT (1 paragraph honest assessment of this product)\n"
        f"7. BETTER ALTERNATIVES (what to look for instead, if relevant)\n"
    )

    print(f"\n{'='*60}")
    print("NUTRITION LABEL DECODER")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# ALLERGY RECIPE ADAPTER
# ---------------------------------------------------------------------------

def cmd_adapt_recipe(args: argparse.Namespace) -> None:
    system = (
        "You are a professional chef and food allergist specializing in dietary adaptations. "
        "You understand the culinary function of every ingredient — not just its nutritional "
        "profile but its role in texture, flavor, browning, binding, and moisture. When you "
        "substitute an ingredient, you explain WHY the substitute works, how it changes the "
        "final dish, and any technique adjustments required. Your adaptations are culinarily "
        "sound, not just allergy-safe. For baking, you are especially precise because "
        "chemical reactions matter. You always add cross-contamination warnings for serious allergies."
    )

    if args.file:
        recipe_text = read_file(args.file)
        recipe_source = f"from file: {args.file}"
    elif args.recipe:
        recipe_text = args.recipe
        recipe_source = "inline description"
    else:
        print("Error: Provide either --file or --recipe with the recipe content.", file=sys.stderr)
        sys.exit(1)

    type_note = f"\nRecipe type: {args.type}" if args.type else ""
    serious_note = (
        "\nNote: Please include cross-contamination warnings — this is for a serious allergy, not just a preference."
        if args.serious
        else ""
    )

    user_message = (
        f"Adapt the following recipe to avoid: {args.avoid}\n"
        f"Recipe ({recipe_source}):"
        f"{type_note}"
        f"{serious_note}\n\n"
        f"{recipe_text}\n\n"
        f"Provide:\n"
        f"1. INGREDIENT SUBSTITUTIONS TABLE (original | substitute | notes on why it works)\n"
        f"2. TECHNIQUE ADJUSTMENTS (any changes to method required by the substitutions)\n"
        f"3. FLAVOR NOTES (how will the adapted dish differ from the original?)\n"
        f"4. CROSS-CONTAMINATION WARNINGS (for serious allergy management)\n"
        f"5. ADAPTED RECIPE (full rewritten recipe with all substitutions applied)\n"
    )

    print(f"\n{'='*60}")
    print(f"ALLERGY RECIPE ADAPTER")
    print(f"Avoiding: {args.avoid}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered wellness tools (educational use only — not medical advice).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- symptoms ---
    sy = subparsers.add_parser("symptoms", help="Analyze symptom diary data for patterns")
    sy_source = sy.add_mutually_exclusive_group()
    sy_source.add_argument("symptoms", nargs="?", help="Symptom description as inline text")
    sy_source.add_argument("--file", help="Path to symptom diary text file")
    sy.add_argument("--period", help="Time period covered (e.g. '2 weeks')")

    # --- medications ---
    md = subparsers.add_parser("medications", help="Check potential medication interactions (educational only)")
    md_source = md.add_mutually_exclusive_group()
    md_source.add_argument("medications", nargs="?", help="Comma-separated list of medications/supplements")
    md_source.add_argument("--file", help="Path to file listing medications")

    # --- nutrition ---
    nt = subparsers.add_parser("nutrition", help="Decode and analyze a nutrition label")
    nt_source = nt.add_mutually_exclusive_group()
    nt_source.add_argument("--label", help="Nutrition label data as inline text")
    nt_source.add_argument("--file", help="Path to file with nutrition label data")
    nt.add_argument("--product", help="Product name for context")
    nt.add_argument("--goal", help="Health goal for context (e.g. 'weight loss', 'heart health')")

    # --- adapt-recipe ---
    ar = subparsers.add_parser("adapt-recipe", help="Adapt a recipe to avoid allergens")
    ar_source = ar.add_mutually_exclusive_group()
    ar_source.add_argument("--file", help="Path to recipe text file")
    ar_source.add_argument("--recipe", help="Recipe description or text inline")
    ar.add_argument("--avoid", required=True, help="Comma-separated list of allergens/restrictions to avoid")
    ar.add_argument(
        "--type",
        choices=["baking", "cooking", "dessert", "sauce", "beverage"],
        help="Recipe type (baking gets extra precision)",
    )
    ar.add_argument(
        "--serious",
        action="store_true",
        help="Flag for serious allergy (adds cross-contamination warnings)",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Handle positional args that conflict with --file
    if args.command == "symptoms":
        if not hasattr(args, "symptoms") or (args.symptoms is None and args.file is None):
            print("Error: Provide symptom data as a positional argument or via --file.", file=sys.stderr)
            sys.exit(1)

    if args.command == "medications":
        if not hasattr(args, "medications") or (args.medications is None and args.file is None):
            print("Error: Provide medication list as a positional argument or via --file.", file=sys.stderr)
            sys.exit(1)

    if args.command == "nutrition":
        if args.label is None and args.file is None:
            print("Error: Provide nutrition data via --label or --file.", file=sys.stderr)
            sys.exit(1)

    dispatch = {
        "symptoms": cmd_symptoms,
        "medications": cmd_medications,
        "nutrition": cmd_nutrition,
        "adapt-recipe": cmd_adapt_recipe,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
