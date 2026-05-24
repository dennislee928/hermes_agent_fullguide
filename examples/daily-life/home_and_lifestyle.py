#!/usr/bin/env python3
"""
home_and_lifestyle.py — Hermes Daily Life Examples
Covers: home-cleaning-schedule, home-repair-troubleshooter, plant-care-assistant,
        pet-care-advisor, outfit-suggester

Usage:
    python home_and_lifestyle.py cleaning-schedule --rooms 4 --frequency weekly
    python home_and_lifestyle.py cleaning-schedule --rooms 6 --people 4 --pets --frequency biweekly
    python home_and_lifestyle.py repair "leaking faucet"
    python home_and_lifestyle.py repair "toilet keeps running" --skill beginner
    python home_and_lifestyle.py plant "monstera"
    python home_and_lifestyle.py plant "fiddle leaf fig" --environment "low light, dry apartment"
    python home_and_lifestyle.py pet "golden retriever 3 years"
    python home_and_lifestyle.py pet "persian cat 10 years" --issue "not eating well"
    python home_and_lifestyle.py outfit --occasion "job interview" --weather "cold"
    python home_and_lifestyle.py outfit --occasion "beach wedding" --wardrobe "navy suit, white linen shirt"
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
    print()


# ---------------------------------------------------------------------------
# Sub-command handlers
# ---------------------------------------------------------------------------

def cmd_cleaning_schedule(args: argparse.Namespace) -> None:
    system = (
        "You are a professional home organization and cleaning expert. "
        "Create practical, sustainable cleaning schedules that fit real people's lives. "
        "Divide tasks into Daily (5-15 min), Weekly deep clean, and Monthly sections. "
        "For weekly tasks, organize by room. Use markdown checklist format (- [ ] task). "
        "Be specific about techniques and products when helpful."
    )
    pets_note = " The household has pets — include pet-specific cleaning tasks." if args.pets else ""
    user_msg = (
        f"Create a home cleaning schedule for a {args.rooms}-room home "
        f"with {args.people} occupant(s). Cleaning frequency preference: {args.frequency}.{pets_note}\n"
        "Organize into three sections: Daily tasks (5-15 min), "
        "Weekly deep clean (by room with estimated time per room), "
        "and Monthly tasks. Use markdown checklist format. "
        "End with a 'Time-Saving Tips' section with 3 tips."
    )
    print(f"\n=== Home Cleaning Schedule ===\nRooms: {args.rooms} | People: {args.people} | Frequency: {args.frequency}\n")
    stream_chat(system, user_msg)


def cmd_repair(args: argparse.Namespace) -> None:
    system = (
        "You are a knowledgeable home repair expert — the equivalent of a skilled handyman friend "
        "who gives honest, practical advice. "
        "For each repair issue: diagnose the most likely cause, list required tools, "
        "give step-by-step instructions, state difficulty level and estimated cost, "
        "and clearly identify when to call a professional instead. "
        "Safety warnings must be clearly marked with a ⚠ symbol. "
        "Use markdown formatting."
    )
    skill_note = f" The homeowner's DIY skill level is: {args.skill}." if args.skill else ""
    brand_note = f" Brand/model information: {args.brand}." if args.brand else ""
    user_msg = (
        f"Home repair issue: {args.issue}.{skill_note}{brand_note}\n"
        "Provide: (1) likely diagnosis/cause, (2) required tools list, "
        "(3) estimated repair time and cost, (4) numbered step-by-step instructions, "
        "(5) safety warnings if applicable, (6) when to call a professional. "
        "Include difficulty rating: Easy / Moderate / Advanced."
    )
    print(f"\n=== Home Repair Troubleshooter ===\nIssue: {args.issue}\n")
    stream_chat(system, user_msg)


def cmd_plant(args: argparse.Namespace) -> None:
    system = (
        "You are a expert horticulturist and plant care specialist. "
        "Provide thorough, accurate plant care guides tailored to the specific environment described. "
        "Cover: light requirements, watering frequency and method, humidity needs, "
        "soil preferences, fertilizing schedule, common problems and solutions in a table, "
        "and repotting guidelines. "
        "If symptoms are described, diagnose the likely cause first. "
        "Use markdown formatting with clear sections."
    )
    environment_note = f" Growing environment: {args.environment}." if args.environment else ""
    outdoor_note = f" This is an outdoor plant in USDA zone {args.zone}." if args.zone else ""
    symptoms_note = f" Current symptoms/issues: {args.symptoms}." if args.symptoms else ""
    user_msg = (
        f"Plant: {args.plant_name}.{environment_note}{outdoor_note}{symptoms_note}\n"
        "Provide a complete care guide covering: Light, Watering, Humidity, "
        "Soil & Potting, Fertilizing, Common Problems (as a table with Symptom | Cause | Fix), "
        "and Repotting guidelines. "
        "If symptoms were mentioned, lead with a Diagnosis section."
    )
    print(f"\n=== Plant Care Assistant ===\nPlant: {args.plant_name}\n")
    stream_chat(system, user_msg)


def cmd_pet(args: argparse.Namespace) -> None:
    system = (
        "You are a knowledgeable veterinary technician and animal behavior specialist. "
        "Provide comprehensive, breed- and age-specific pet care advice that is practical and warm. "
        "Always recommend consulting a licensed veterinarian for health concerns, diagnoses, or medications. "
        "Cover: diet, exercise, grooming (as a table), vet schedule, and breed-specific health considerations. "
        "Use markdown formatting with clear sections."
    )
    issue_note = f" Current concern or issue: {args.issue}." if args.issue else ""
    user_msg = (
        f"Pet: {args.pet_description}.{issue_note}\n"
        "Provide a comprehensive care overview including: "
        "Diet (recommended food type, portions, foods to avoid), "
        "Exercise (daily requirements and activity ideas), "
        "Grooming (as a table: Task | Frequency | Notes), "
        "Vet Schedule (annual and breed-specific checkups), "
        "and Breed/Species-Specific Health Considerations. "
        "If an issue was mentioned, add a 'Current Concern' section first. "
        "End with a disclaimer to consult a veterinarian for medical advice."
    )
    print(f"\n=== Pet Care Advisor ===\nPet: {args.pet_description}\n")
    stream_chat(system, user_msg)


def cmd_outfit(args: argparse.Namespace) -> None:
    system = (
        "You are a professional personal stylist with expertise in fashion for all occasions. "
        "Provide specific, confident outfit recommendations with clear reasoning. "
        "If a wardrobe is provided, only suggest items from that wardrobe. "
        "Format the main recommendation as a markdown table (Item | Piece | Why It Works). "
        "Include styling tips and at least one alternative outfit option. "
        "Use markdown formatting."
    )
    wardrobe_note = f" Available wardrobe items: {args.wardrobe}." if args.wardrobe else " Suggest ideal items for the occasion."
    style_note = f" Preferred style: {args.style}." if args.style else ""
    user_msg = (
        f"Occasion: {args.occasion}. Weather: {args.weather}.{wardrobe_note}{style_note}\n"
        "Recommend a complete outfit including: top, bottoms, outerwear (if needed), "
        "shoes, and any relevant accessories. "
        "Format as a table (Item Category | Specific Piece | Why It Works). "
        "Then add 'Styling Tips' (3 specific tips) and one 'Alternative Look' option."
    )
    print(f"\n=== Outfit Suggester ===\nOccasion: {args.occasion} | Weather: {args.weather}\n")
    stream_chat(system, user_msg)


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Home & Lifestyle assistant powered by Hermes via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # cleaning-schedule
    p_clean = subparsers.add_parser("cleaning-schedule", help="Generate a home cleaning schedule.")
    p_clean.add_argument("--rooms", type=int, default=4, help="Number of rooms (default: 4).")
    p_clean.add_argument("--people", type=int, default=2, help="Number of occupants (default: 2).")
    p_clean.add_argument("--frequency", default="weekly", help="Cleaning frequency: daily, weekly, biweekly (default: weekly).")
    p_clean.add_argument("--pets", action="store_true", help="Include pet-specific cleaning tasks.")

    # repair
    p_repair = subparsers.add_parser("repair", help="Troubleshoot and get repair guidance for home issues.")
    p_repair.add_argument("issue", help='Description of the problem e.g. "leaking faucet".')
    p_repair.add_argument("--skill", default="", help="DIY skill level: beginner, intermediate, advanced.")
    p_repair.add_argument("--brand", default="", help="Brand or model of the fixture/appliance.")

    # plant
    p_plant = subparsers.add_parser("plant", help="Get a complete plant care guide.")
    p_plant.add_argument("plant_name", help="Plant name e.g. 'monstera' or 'Monstera deliciosa'.")
    p_plant.add_argument("--environment", default="", help="Growing environment e.g. 'low light apartment, dry climate'.")
    p_plant.add_argument("--zone", default="", help="USDA hardiness zone for outdoor plants.")
    p_plant.add_argument("--symptoms", default="", help="Current symptoms e.g. 'yellow leaves, drooping'.")

    # pet
    p_pet = subparsers.add_parser("pet", help="Get breed-specific pet care advice.")
    p_pet.add_argument("pet_description", help='Pet description e.g. "golden retriever 3 years" or "persian cat 10 years".')
    p_pet.add_argument("--issue", default="", help="Current concern e.g. 'not eating well', 'excessive barking'.")

    # outfit
    p_outfit = subparsers.add_parser("outfit", help="Get outfit recommendations for any occasion.")
    p_outfit.add_argument("--occasion", required=True, help='Occasion e.g. "job interview", "beach wedding".')
    p_outfit.add_argument("--weather", required=True, help='Weather conditions e.g. "cold", "hot and sunny", "mild".')
    p_outfit.add_argument("--wardrobe", default="", help="Comma-separated list of available wardrobe items.")
    p_outfit.add_argument("--style", default="", help='Style preference e.g. "smart casual", "minimalist".')

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "cleaning-schedule": cmd_cleaning_schedule,
        "repair": cmd_repair,
        "plant": cmd_plant,
        "pet": cmd_pet,
        "outfit": cmd_outfit,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
