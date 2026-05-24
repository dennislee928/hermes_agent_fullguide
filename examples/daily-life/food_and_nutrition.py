#!/usr/bin/env python3
"""
food_and_nutrition.py — Hermes Daily Life Examples
Covers: recipe-from-ingredients, weekly-meal-planner, grocery-list-optimizer, nutrition-tracker

Usage:
    python food_and_nutrition.py recipe "chicken, rice, tomatoes"
    python food_and_nutrition.py meal-plan --days 7 --diet vegetarian
    python food_and_nutrition.py grocery --meals "pasta,salad,soup"
    python food_and_nutrition.py nutrition "200g chicken breast, 100g rice"
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
    print()  # trailing newline after stream ends


# ---------------------------------------------------------------------------
# Sub-command handlers
# ---------------------------------------------------------------------------

def cmd_recipe(args: argparse.Namespace) -> None:
    system = (
        "You are an expert home cook and recipe developer. "
        "Your specialty is creating delicious, practical recipes using only the ingredients "
        "the user has on hand. Never suggest buying additional ingredients. "
        "Format your response with a recipe title, prep/cook times, ingredient list with "
        "quantities, numbered step-by-step instructions, and a short tips section. "
        "Use markdown formatting."
    )
    diet_note = f" The recipe must be {args.diet}." if args.diet else ""
    equipment_note = f" Available cooking equipment: {args.equipment}." if args.equipment else ""
    user_msg = (
        f"I have these ingredients: {args.ingredients}.\n"
        f"Please create a complete dinner recipe using only these items.{diet_note}{equipment_note}\n"
        "Include the recipe title, prep and cook times, exact ingredient quantities, "
        "numbered instructions, and a tips section."
    )
    print(f"\n=== Recipe Generator ===\nIngredients: {args.ingredients}\n")
    stream_chat(system, user_msg)


def cmd_meal_plan(args: argparse.Namespace) -> None:
    system = (
        "You are a professional nutritionist and meal planning expert. "
        "Create balanced, realistic meal plans that are enjoyable and easy to prepare. "
        "Format plans as markdown tables with one row per day, covering breakfast, lunch, "
        "dinner, and snacks. Include weekly prep notes at the end."
    )
    calories_note = f" Target approximately {args.calories} calories per day." if args.calories else ""
    cuisine_note = f" Preferred cuisine style: {args.cuisine}." if args.cuisine else ""
    user_msg = (
        f"Create a {args.days}-day {args.diet} meal plan.{calories_note}{cuisine_note}\n"
        "Include breakfast, lunch, dinner, and one snack per day. "
        "On weekdays prefer meals under 30 minutes to prepare. "
        "After the table, add a 'Weekly Prep Notes' section with batch-cooking tips. "
        "Use markdown formatting."
    )
    print(f"\n=== {args.days}-Day Meal Planner ({args.diet}) ===\n")
    stream_chat(system, user_msg)


def cmd_grocery(args: argparse.Namespace) -> None:
    system = (
        "You are an efficient meal prep assistant. Given a list of meals, generate a "
        "comprehensive, deduplicated grocery list organized by store aisle/section. "
        "Combine duplicate ingredients and show total quantities. "
        "Separate 'pantry staples you likely already have' at the bottom. "
        "Use markdown checklist format (- [ ] item)."
    )
    servings_note = f" Scale all quantities for {args.servings} servings per meal." if args.servings else ""
    user_msg = (
        f"I'm making these meals this week: {args.meals}.{servings_note}\n"
        "Generate an optimized grocery list organized by store section "
        "(Produce, Meat & Seafood, Dairy & Eggs, Dry Goods, Canned/Jarred, "
        "Frozen, Pantry Staples). Combine duplicate ingredients and show total quantities. "
        "Use markdown checklist format."
    )
    print(f"\n=== Grocery List Optimizer ===\nMeals: {args.meals}\n")
    stream_chat(system, user_msg)


def cmd_nutrition(args: argparse.Namespace) -> None:
    system = (
        "You are a certified nutritionist with deep knowledge of food science. "
        "Analyze food portions and provide detailed nutritional breakdowns. "
        "Present data as a markdown table with calories, protein, carbohydrates, fat, "
        "fiber, and sodium. Include % Daily Value based on a 2000 kcal diet. "
        "After the table, highlight nutritional strengths and provide 2-3 actionable suggestions."
    )
    goal_note = f" The person's nutritional goal is: {args.goal}." if args.goal else ""
    user_msg = (
        f"Analyze the nutritional content of this meal:\n{args.food}\n{goal_note}\n"
        "Provide: calories, protein, carbohydrates, fat, fiber, sodium, and notable "
        "vitamins/minerals. Show amounts and % Daily Value (2000 kcal basis) in a table. "
        "Then add a Highlights section and 2-3 improvement Suggestions."
    )
    print(f"\n=== Nutrition Tracker ===\nFood: {args.food}\n")
    stream_chat(system, user_msg)


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Food & Nutrition assistant powered by Hermes via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # recipe
    p_recipe = subparsers.add_parser("recipe", help="Generate a recipe from available ingredients.")
    p_recipe.add_argument("ingredients", help="Comma-separated list of ingredients you have.")
    p_recipe.add_argument("--diet", default="", help="Dietary constraint e.g. gluten-free, vegan.")
    p_recipe.add_argument("--equipment", default="", help="Available cooking equipment.")

    # meal-plan
    p_meal = subparsers.add_parser("meal-plan", help="Generate a weekly meal plan.")
    p_meal.add_argument("--days", type=int, default=7, help="Number of days to plan (default: 7).")
    p_meal.add_argument("--diet", default="balanced", help="Diet type e.g. vegetarian, keto, vegan (default: balanced).")
    p_meal.add_argument("--calories", type=int, default=0, help="Target daily calories (optional).")
    p_meal.add_argument("--cuisine", default="", help="Preferred cuisine style e.g. mediterranean.")

    # grocery
    p_grocery = subparsers.add_parser("grocery", help="Build an optimized grocery list from planned meals.")
    p_grocery.add_argument("--meals", required=True, help="Comma-separated list of meals e.g. 'pasta,salad,soup'.")
    p_grocery.add_argument("--servings", type=int, default=0, help="Number of servings per meal (optional).")

    # nutrition
    p_nutrition = subparsers.add_parser("nutrition", help="Analyze nutritional content of a meal.")
    p_nutrition.add_argument("food", help="Description of food with portions e.g. '200g chicken, 100g rice'.")
    p_nutrition.add_argument("--goal", default="", help="Nutritional goal e.g. muscle-gain, weight-loss.")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "recipe": cmd_recipe,
        "meal-plan": cmd_meal_plan,
        "grocery": cmd_grocery,
        "nutrition": cmd_nutrition,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
