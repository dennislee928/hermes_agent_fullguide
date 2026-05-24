#!/usr/bin/env python3
"""
travel_and_social.py — Hermes Daily Life Examples
Covers: travel-packing-list, vacation-itinerary-planner, restaurant-recommender,
        gift-idea-generator, party-planner

Usage:
    python travel_and_social.py packing --destination "Tokyo" --days 10 --activities "sightseeing,hiking"
    python travel_and_social.py packing --destination "beach resort" --days 5 --carry-on

    python travel_and_social.py itinerary --destination "Kyoto, Japan" --days 5 --style "cultural"
    python travel_and_social.py itinerary --destination "Barcelona" --days 7 --budget moderate

    python travel_and_social.py restaurant --city "Tokyo" --cuisine "ramen" --occasion "casual lunch"
    python travel_and_social.py restaurant --city "New York" --occasion "anniversary dinner" --diet "vegetarian"

    python travel_and_social.py gift --for "dad, 58, loves fishing" --budget 75 --occasion "birthday"
    python travel_and_social.py gift --for "best friend, late 20s, into yoga" --budget 50

    python travel_and_social.py party --type "birthday" --guests 20 --budget 300 --theme "90s"
    python travel_and_social.py party --type "dinner party" --guests 8 --budget 150
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

def cmd_packing(args: argparse.Namespace) -> None:
    system = (
        "You are a seasoned travel expert and packing specialist who has visited over 50 countries. "
        "Create thorough, destination-specific packing lists that balance completeness with practicality. "
        "Organize items by category using markdown checklist format (- [ ] item). "
        "Mark essential items clearly. Include destination-specific tips at the end. "
        "Use markdown formatting."
    )
    carry_on_note = " Optimize for carry-on only — apply capsule wardrobe approach with re-wear planning." if args.carry_on else ""
    activities_note = f" Planned activities: {args.activities}." if args.activities else ""
    weather_note = f" Expected weather: {args.weather}." if args.weather else ""
    user_msg = (
        f"Create a packing list for a {args.days}-day trip to {args.destination}.{activities_note}{weather_note}{carry_on_note}\n"
        "Organize into sections: Clothing, Toiletries, Documents & Money, Electronics, "
        "and Destination-Specific Items. "
        "Mark must-have items as essential. Include a 'Destination-Specific Tips' section at the end "
        "with 3-5 items unique to this destination or trip type."
    )
    print(f"\n=== Travel Packing List ===\nDestination: {args.destination} | Duration: {args.days} days\n")
    stream_chat(system, user_msg)


def cmd_itinerary(args: argparse.Namespace) -> None:
    system = (
        "You are an expert travel planner with deep destination knowledge across the world. "
        "Create day-by-day itineraries that balance must-see highlights with realistic pacing. "
        "Group geographically nearby attractions on the same day to minimize travel time. "
        "For each day include: morning, afternoon, and evening activities with meal suggestions. "
        "End with a Logistics section and estimated daily budget breakdown. "
        "Use markdown formatting."
    )
    budget_note = f" Budget level: {args.budget}." if args.budget else " Assume moderate budget."
    style_note = f" Travel style: {args.style}." if args.style else ""
    pace_note = " Build in extra free/spontaneous time — slower pace preferred." if args.pace == "slow" else ""
    solo_note = " Solo traveler." if args.solo else ""
    user_msg = (
        f"Plan a {args.days}-day itinerary for {args.destination}.{style_note}{budget_note}{pace_note}{solo_note}\n"
        "Create a day-by-day plan with morning, afternoon, and evening blocks for each day. "
        "Group nearby attractions. Include meal suggestions at local restaurants. "
        "End with: (1) Logistics section (transport, accommodation tips), "
        "(2) Estimated daily budget breakdown in local currency and USD equivalent."
    )
    print(f"\n=== Vacation Itinerary Planner ===\nDestination: {args.destination} | Duration: {args.days} days\n")
    stream_chat(system, user_msg)


def cmd_restaurant(args: argparse.Namespace) -> None:
    system = (
        "You are a food journalist and seasoned traveler with expertise in global dining culture. "
        "Provide context-rich restaurant guidance including what to look for, how to find good places, "
        "neighborhood recommendations, and ordering tips. "
        "When recommending specific establishments, note that availability changes — focus on "
        "'what to look for' and 'how to search' strategies that remain useful. "
        "Include local dining customs and practical tips. Use markdown formatting."
    )
    diet_note = f" Dietary requirement: {args.diet}." if args.diet else ""
    budget_note = f" Budget level: {args.budget}." if args.budget else ""
    user_msg = (
        f"I'm looking for restaurant recommendations in {args.city}. "
        f"Cuisine: {args.cuisine}. Occasion: {args.occasion}.{diet_note}{budget_note}\n"
        "Provide: (1) What to look for as quality signals in this cuisine type, "
        "(2) Best neighborhoods or areas to search, "
        "(3) Recommended search platforms/apps for this city, "
        "(4) Ordering tips and local customs, "
        "(5) Price range guidance. "
        "Be specific and practical."
    )
    print(f"\n=== Restaurant Recommender ===\nCity: {args.city} | Cuisine: {args.cuisine}\n")
    stream_chat(system, user_msg)


def cmd_gift(args: argparse.Namespace) -> None:
    system = (
        "You are a thoughtful gift consultant who specializes in personalized gift recommendations. "
        "Give specific, actionable gift ideas with clear reasoning for why each fits the recipient. "
        "Include a mix of physical items, experiences, and DIY options where appropriate. "
        "For each suggestion: name the gift, give a price range, explain why it suits this person, "
        "and provide a concrete 'where to find it' tip. "
        "Prioritize experience gifts for recipients who 'don't like clutter'. "
        "Use markdown formatting."
    )
    occasion_note = f" Occasion: {args.occasion}." if args.occasion else ""
    avoid_note = f" Items to avoid (already have or won't like): {args.avoid}." if args.avoid else ""
    diy_note = " Include at least one DIY/handmade gift idea." if args.diy else ""
    user_msg = (
        f"Gift recipient: {args.recipient}.{occasion_note} Budget: ${args.budget}.{avoid_note}{diy_note}\n"
        "Suggest 5 thoughtful, personalized gift ideas. For each: "
        "(1) Gift name and description, "
        "(2) Price range within budget, "
        "(3) Why it suits this specific person, "
        "(4) Where to find it (store, website, or search term). "
        "End with a brief 'Gift Giving Tip' relevant to this recipient type."
    )
    print(f"\n=== Gift Idea Generator ===\nFor: {args.recipient} | Budget: ${args.budget}\n")
    stream_chat(system, user_msg)


def cmd_party(args: argparse.Namespace) -> None:
    system = (
        "You are a creative event planner with expertise in memorable parties on any budget. "
        "Create complete, executable party plans with realistic budget breakdowns. "
        "Include: theme concept, planning timeline, food and drink menu with quantities, "
        "decoration list with approximate costs, activity ideas, and a day-of checklist. "
        "Be specific — include actual product search terms, quantities scaled to guest count, "
        "and cost estimates for each category. Use markdown formatting."
    )
    theme_note = f" Requested theme: {args.theme}." if args.theme else ""
    diet_note = f" Dietary requirements: {args.diet}." if args.diet else ""
    outdoor_note = " Outdoor event — include weather contingency suggestions." if args.outdoor else " Indoor event."
    age_note = f" Party is for age {args.age}." if args.age else ""
    user_msg = (
        f"Plan a {args.type} party for {args.guests} guests. Total budget: ${args.budget}.{theme_note}{diet_note}{outdoor_note}{age_note}\n"
        "Provide: (1) Theme concept and aesthetic, "
        "(2) Planning timeline (weeks before event), "
        "(3) Food & drink menu with quantities scaled to {guests} guests, "
        "(4) Decoration list with estimated costs, "
        "(5) Activity ideas (at least 2), "
        "(6) Budget breakdown table by category, "
        "(7) Day-of checklist. "
        "Make all suggestions specific and actionable."
    ).format(guests=args.guests)
    print(f"\n=== Party Planner ===\nType: {args.type} | Guests: {args.guests} | Budget: ${args.budget}\n")
    stream_chat(system, user_msg)


# ---------------------------------------------------------------------------
# CLI setup
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Travel & Social assistant powered by Hermes via Ollama.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # packing
    p_pack = subparsers.add_parser("packing", help="Generate a trip-specific packing list.")
    p_pack.add_argument("--destination", required=True, help="Travel destination e.g. 'Tokyo' or 'beach resort'.")
    p_pack.add_argument("--days", type=int, required=True, help="Trip duration in days.")
    p_pack.add_argument("--activities", default="", help="Planned activities e.g. 'sightseeing,hiking,business dinner'.")
    p_pack.add_argument("--weather", default="", help="Expected weather e.g. 'hot and humid', 'cold and rainy'.")
    p_pack.add_argument("--carry-on", action="store_true", dest="carry_on", help="Optimize for carry-on luggage only.")

    # itinerary
    p_itin = subparsers.add_parser("itinerary", help="Plan a day-by-day vacation itinerary.")
    p_itin.add_argument("--destination", required=True, help="Travel destination.")
    p_itin.add_argument("--days", type=int, required=True, help="Trip duration in days.")
    p_itin.add_argument("--style", default="", help="Travel style e.g. 'cultural', 'food and art', 'adventure'.")
    p_itin.add_argument("--budget", default="", help="Budget level: budget, moderate, upscale.")
    p_itin.add_argument("--pace", default="", help="Pace preference: slow, moderate, packed.")
    p_itin.add_argument("--solo", action="store_true", help="Solo traveler flag.")

    # restaurant
    p_rest = subparsers.add_parser("restaurant", help="Get restaurant guidance and recommendations.")
    p_rest.add_argument("--city", required=True, help="City name.")
    p_rest.add_argument("--cuisine", default="any", help="Cuisine type e.g. 'ramen', 'italian', 'any'.")
    p_rest.add_argument("--occasion", default="casual dining", help="Dining occasion e.g. 'anniversary dinner', 'casual lunch'.")
    p_rest.add_argument("--diet", default="", help="Dietary requirement e.g. 'vegetarian', 'halal'.")
    p_rest.add_argument("--budget", default="", help="Budget level e.g. 'budget', 'moderate', 'upscale'.")

    # gift
    p_gift = subparsers.add_parser("gift", help="Generate personalized gift ideas.")
    p_gift.add_argument("--for", required=True, dest="recipient", help='Recipient description e.g. "dad, 58, loves fishing".')
    p_gift.add_argument("--budget", type=int, required=True, help="Maximum budget in USD.")
    p_gift.add_argument("--occasion", default="", help="Gift occasion e.g. 'birthday', 'christmas', 'graduation'.")
    p_gift.add_argument("--avoid", default="", help="Items to avoid e.g. 'already has a good coffee maker'.")
    p_gift.add_argument("--diy", action="store_true", help="Include a DIY/handmade gift option.")

    # party
    p_party = subparsers.add_parser("party", help="Get a complete party planning guide.")
    p_party.add_argument("--type", required=True, help='Party type e.g. "birthday", "dinner party", "graduation".')
    p_party.add_argument("--guests", type=int, required=True, help="Number of guests.")
    p_party.add_argument("--budget", type=int, required=True, help="Total budget in USD.")
    p_party.add_argument("--theme", default="", help="Theme or vibe e.g. '90s', 'garden party', 'tropical'.")
    p_party.add_argument("--diet", default="", help="Dietary requirements e.g. 'includes vegan guests'.")
    p_party.add_argument("--outdoor", action="store_true", help="Outdoor event flag.")
    p_party.add_argument("--age", default="", help="Age of person being celebrated (for birthday parties).")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "packing": cmd_packing,
        "itinerary": cmd_itinerary,
        "restaurant": cmd_restaurant,
        "gift": cmd_gift,
        "party": cmd_party,
    }
    dispatch[args.command](args)


if __name__ == "__main__":
    main()
