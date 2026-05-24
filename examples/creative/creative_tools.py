#!/usr/bin/env python3
"""
creative_tools.py — Hermes-powered creative tools: short story generator,
songwriting assistant, poem generator, social media caption writer,
and brand naming assistant.

Usage:
  python creative_tools.py story --genre thriller --setting "Tokyo 2050" --length short
  python creative_tools.py story --genre "magical realism" --theme "memory and loss" --style "literary fiction"
  python creative_tools.py song --mood melancholic --theme "lost love" --style "indie folk"
  python creative_tools.py song --mood hopeful --theme "new beginnings" --structure VCVCBC
  python creative_tools.py poem --type sonnet --occasion birthday --for "my grandmother"
  python creative_tools.py poem --type villanelle --subject insomnia --tone "dark humor"
  python creative_tools.py caption --image-desc "sunset over mountains" --platform instagram --tone inspirational
  python creative_tools.py caption --image-desc "product flatlay" --platform linkedin --brand "small ceramics studio"
  python creative_tools.py brand --product "sustainable water bottle" --audience "eco-conscious millennials" --count 10
  python creative_tools.py brand --product "AI finance app" --values "approachable, empowering" --avoid "banking jargon"
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
# SHORT STORY GENERATOR
# ---------------------------------------------------------------------------

def cmd_story(args: argparse.Namespace) -> None:
    system = (
        "You are a gifted fiction writer with command of multiple genres and styles. "
        "You write stories with coherent three-act structure (setup, conflict, resolution), "
        "characters who feel like real people rather than types, specific sensory details that "
        "ground the reader in place and time, and endings that feel earned rather than convenient. "
        "You avoid common AI fiction failures: meandering plots, telling instead of showing, "
        "purple prose, and cardboard characters. Your dialogue sounds like it is actually spoken. "
        "If given a style reference, you capture its spirit without parody or pastiche."
    )

    length_guidance = {
        "flash": "Write a flash fiction story of 250-500 words. Every word must carry weight.",
        "short": "Write a short story of 800-1,200 words with a complete narrative arc.",
        "medium": "Write a short story of 2,000-3,000 words with developed characters and subplot.",
        "long": "Write a long short story of 3,500-5,000 words with full scene development.",
    }
    length_desc = length_guidance.get(args.length, length_guidance["short"])

    genre_note = f"Genre: {args.genre}\n" if args.genre else ""
    setting_note = f"Setting: {args.setting}\n" if args.setting else ""
    theme_note = f"Theme: {args.theme}\n" if args.theme else ""
    style_note = f"Prose style: {args.style}\n" if args.style else ""
    pov_note = f"Point of view: {args.pov}\n" if args.pov else ""
    character_note = f"Central character: {args.character}\n" if args.character else ""

    continue_text = ""
    if args.continue_from:
        continue_text = f"\nContinue from or build on this existing text:\n\n{read_file(args.continue_from) if args.continue_from.endswith('.txt') else args.continue_from}\n"

    user_message = (
        f"Write an original short story with the following specifications:\n\n"
        f"{genre_note}"
        f"{setting_note}"
        f"{theme_note}"
        f"{style_note}"
        f"{pov_note}"
        f"{character_note}"
        f"Length: {length_desc}\n"
        f"{continue_text}\n"
        f"Write the complete story. Give it a title. "
        f"The story should have a beginning that hooks, a middle with genuine tension or discovery, "
        f"and an ending that resonates. Do not summarize or outline — write the actual story."
    )

    print(f"\n{'='*60}")
    print(f"SHORT STORY GENERATOR")
    if args.genre:
        print(f"Genre: {args.genre}", end="")
    if args.setting:
        print(f" | Setting: {args.setting}", end="")
    print()
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SONGWRITING ASSISTANT
# ---------------------------------------------------------------------------

def cmd_song(args: argparse.Namespace) -> None:
    system = (
        "You are a professional songwriter with credits across multiple genres. "
        "You write lyrics that scan naturally for singing — you count syllables and "
        "feel the meter, you write rhymes that feel inevitable rather than forced, "
        "and you create imagery that is specific and evocative rather than generic. "
        "You understand song structure: verses carry story, the chorus is the emotional peak "
        "and repeatable hook, the bridge provides contrast and release. "
        "Your lyrics avoid clichés unless you subvert them intentionally. "
        "You include songwriting notes to explain key craft decisions."
    )

    structure_default = "Verse-Chorus-Verse-Chorus-Bridge-Chorus"
    structure = args.structure if args.structure else structure_default

    mood_note = f"Mood/tone: {args.mood}\n" if args.mood else ""
    theme_note = f"Theme: {args.theme}\n" if args.theme else ""
    style_note = f"Genre/style: {args.style}\n" if args.style else ""
    key_note = f"Key: {args.key}\n" if args.key else ""
    tempo_note = f"Tempo feel: {args.tempo}\n" if args.tempo else ""
    rhyme_note = f"Rhyme scheme: {args.rhyme_scheme}\n" if args.rhyme_scheme else ""

    develop_hook = ""
    if args.develop_hook:
        develop_hook = f"\nDevelop or expand on this existing hook/line:\n'{args.develop_hook}'\n"

    user_message = (
        f"Write a complete song with the following specifications:\n\n"
        f"{mood_note}"
        f"{theme_note}"
        f"{style_note}"
        f"{key_note}"
        f"{tempo_note}"
        f"Structure: {structure}\n"
        f"{rhyme_note}"
        f"{develop_hook}\n"
        f"Provide:\n"
        f"1. SONG TITLE\n"
        f"2. COMPLETE LYRICS (with [VERSE 1], [CHORUS], [VERSE 2], [BRIDGE], etc. labels)\n"
        f"3. SONGWRITING NOTES (explain the key craft choices: central metaphor, rhyme structure, "
        f"   emotional arc, any moment in the lyrics you want to highlight)\n"
        f"4. PERFORMANCE SUGGESTION (tempo, feel, dynamics idea)\n"
    )

    print(f"\n{'='*60}")
    print("SONGWRITING ASSISTANT")
    if args.style:
        print(f"Style: {args.style}", end="")
    if args.mood:
        print(f" | Mood: {args.mood}", end="")
    print()
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# POEM GENERATOR
# ---------------------------------------------------------------------------

def cmd_poem(args: argparse.Namespace) -> None:
    system = (
        "You are an accomplished poet with mastery of both formal and free verse traditions. "
        "When writing formal poetry (sonnet, villanelle, haiku, etc.) you adhere strictly to "
        "the form's rules — meter, rhyme scheme, line count, and stanza structure. "
        "You write poems that have genuine image-making — concrete, specific images rather than "
        "abstract sentiment. Your poems reward reading aloud: they have sonic texture, rhythm "
        "that supports meaning, and a volta or turn that surprises the reader. "
        "You avoid sentimental clichés and easy resolutions. "
        "Include poet's notes explaining key craft decisions after the poem."
    )

    form_guidance = {
        "sonnet": "Shakespearean sonnet: 14 lines, ABAB CDCD EFEF GG rhyme scheme, iambic pentameter, volta before the couplet.",
        "haiku": "Traditional haiku: 5-7-5 syllable structure across three lines, seasonal reference (kigo) if appropriate, juxtaposition.",
        "villanelle": "Villanelle: 19 lines, two refrains (A1 and A2), five tercets plus a closing quatrain (ABA ABA ABA ABA ABA ABAA).",
        "ode": "Ode: celebratory lyric poem, 3+ stanzas, sustained attention to one subject, elevated but accessible diction.",
        "elegy": "Elegy: poem of mourning or lamentation, movement from grief toward acceptance or commemoration.",
        "free verse": "Free verse: no required rhyme or meter, but conscious attention to line breaks, white space, and rhythmic phrasing.",
        "ballad": "Ballad: narrative poem, ABAB or ABCB rhyme scheme, 4-line stanzas, musical quality, often tells a story of loss or adventure.",
    }

    form_desc = form_guidance.get(args.type.lower() if args.type else "free verse", f"Form: {args.type}")

    subject_note = f"Subject: {args.subject}\n" if args.subject else ""
    occasion_note = f"Occasion: {args.occasion}\n" if args.occasion else ""
    for_note = f"Written for: {args.for_person}\n" if args.for_person else ""
    tone_note = f"Tone: {args.tone}\n" if args.tone else ""
    length_note = f"Length preference: {args.length}\n" if args.length else ""

    user_message = (
        f"Write a poem with the following specifications:\n\n"
        f"Form: {form_desc}\n"
        f"{subject_note}"
        f"{occasion_note}"
        f"{for_note}"
        f"{tone_note}"
        f"{length_note}\n"
        f"Write the complete poem with a title.\n"
        f"After the poem, include POET'S NOTES: briefly explain 2-3 key craft decisions "
        f"(imagery choices, structural moves, the volta if applicable, sonic choices).\n"
    )

    print(f"\n{'='*60}")
    print(f"POEM GENERATOR: {args.type if args.type else 'Free Verse'}")
    if args.occasion:
        print(f"Occasion: {args.occasion}", end="")
    if args.for_person:
        print(f" | For: {args.for_person}", end="")
    print()
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# SOCIAL MEDIA CAPTION WRITER
# ---------------------------------------------------------------------------

def cmd_caption(args: argparse.Namespace) -> None:
    platform_guidance = {
        "instagram": (
            "Instagram: warm, aspirational, or conversational tone. "
            "Key message in first 125 characters (truncation point). "
            "Use strategic line breaks. 8-15 hashtags (mix niche and medium tags). "
            "End with soft CTA. Emojis used sparingly for personality, not spam."
        ),
        "linkedin": (
            "LinkedIn: professional but human, not corporate-stiff. "
            "Open with a hook (not 'I am excited to share...'). "
            "Longer form is acceptable (150-300 words). "
            "3-5 relevant hashtags maximum. First-person narrative works well. "
            "End with a question or clear professional CTA."
        ),
        "tiktok": (
            "TikTok: casual, direct, energetic. Ultra-short (50-150 chars). "
            "Hook is everything — first line must grab. "
            "Conversational, Gen Z-adjacent without being forced. "
            "3-5 hashtags including trending ones. Often ends with a challenge or question."
        ),
        "twitter": (
            "Twitter/X: concise, punchy, wit-dense. Maximum 280 characters. "
            "Every word earns its place. Can be opinionated or provocative. "
            "2-3 hashtags max or none at all. No filler phrases."
        ),
        "facebook": (
            "Facebook: friendly, community-oriented, slightly longer than Twitter. "
            "Storytelling approach works well. 1-3 hashtags or none. "
            "Questions drive engagement. Less formal than LinkedIn."
        ),
    }

    platform_desc = platform_guidance.get(
        args.platform.lower(), f"Platform: {args.platform}"
    )

    brand_note = f"\nBrand voice/values: {args.brand}" if args.brand else ""
    tone_note = f"\nTone: {args.tone}" if args.tone else ""
    cta_note = f"\nDesired CTA: {args.cta}" if args.cta else ""
    goal_note = f"\nContent goal: {args.goal}" if args.goal else ""

    user_message = (
        f"Write 3 social media caption options for the following:\n\n"
        f"Platform: {args.platform} — {platform_desc}\n"
        f"Image/content description: {args.image_desc}"
        f"{brand_note}"
        f"{tone_note}"
        f"{cta_note}"
        f"{goal_note}\n\n"
        f"Provide 3 distinct options:\n"
        f"- OPTION 1: Storytelling/narrative approach\n"
        f"- OPTION 2: Short and punchy\n"
        f"- OPTION 3: Engagement/question-based\n\n"
        f"For each option include the full caption text with hashtags.\n"
        f"After all 3 options, add PLATFORM NOTES: 3-4 specific tips for this "
        f"platform and this content type.\n"
    )

    print(f"\n{'='*60}")
    print(f"CAPTION WRITER: {args.platform.upper()}")
    if args.tone:
        print(f"Tone: {args.tone}")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# BRAND NAMING ASSISTANT
# ---------------------------------------------------------------------------

def cmd_brand(args: argparse.Namespace) -> None:
    system = (
        "You are a professional brand strategist and naming expert with experience across "
        "consumer products, technology, services, and lifestyle brands. "
        "You generate names with genuine creative variety — not just compound words or "
        "portmanteaus. Your naming types include: evocative/metaphorical, coined/invented, "
        "mythological/classical reference, everyday word reframed, nature-inspired, "
        "abstract/conceptual, and descriptive-with-twist. "
        "For each name you provide: the type, a clear rationale (meaning and strategic fit), "
        "domain availability note, and tone fit assessment. "
        "You always note that names need trademark and domain verification before use."
    )

    audience_note = f"\nTarget audience: {args.audience}" if args.audience else ""
    values_note = f"\nBrand values: {args.values}" if args.values else ""
    avoid_note = f"\nAvoid: {args.avoid}" if args.avoid else ""
    naming_type_note = f"\nPrefer this naming type: {args.naming_type}" if args.naming_type else ""

    user_message = (
        f"Generate {args.count} original brand name options for:\n\n"
        f"Product/Service: {args.product}"
        f"{audience_note}"
        f"{values_note}"
        f"{avoid_note}"
        f"{naming_type_note}\n\n"
        f"For each name provide:\n"
        f"1. The name (in all caps)\n"
        f"2. Naming type (evocative / coined / classical / reframed word / etc.)\n"
        f"3. Rationale (meaning, associations, strategic positioning — 2-3 sentences)\n"
        f"4. Domain check note (.com likely available / taken — suggest variants)\n"
        f"5. Tone fit (High / Medium / Low — with 1 sentence why)\n\n"
        f"After all names, provide:\n"
        f"- TOP 3 RECOMMENDATIONS for this brief (with 1-sentence reason each)\n"
        f"- NEXT STEPS (trademark check, domain check, audience testing)\n"
        f"- NAMING DISCLAIMER (not pre-cleared for trademark or availability)\n"
    )

    print(f"\n{'='*60}")
    print("BRAND NAMING ASSISTANT")
    print(f"Product: {args.product}")
    if args.audience:
        print(f"Audience: {args.audience}")
    print(f"Generating {args.count} names")
    print(f"{'='*60}\n")
    stream_chat(system, user_message)


# ---------------------------------------------------------------------------
# CLI SETUP
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hermes-powered creative tools: story, song, poem, caption, brand naming.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # --- story ---
    st = subparsers.add_parser("story", help="Generate an original short story")
    st.add_argument("--genre", help="Story genre (e.g. thriller, sci-fi, magical realism, romance)")
    st.add_argument("--setting", help="Time and place (e.g. 'Tokyo 2050', 'rural Ireland 1920s')")
    st.add_argument("--theme", help="Thematic focus (e.g. 'memory and loss', 'identity')")
    st.add_argument("--style", help="Prose style (e.g. 'minimalist Hemingway', 'noir', 'lyrical')")
    st.add_argument("--pov", choices=["first", "second", "third-limited", "third-omniscient"], help="Point of view")
    st.add_argument("--character", help="Central character description")
    st.add_argument(
        "--length",
        choices=["flash", "short", "medium", "long"],
        default="short",
        help="Story length (default: short = 800-1200 words)",
    )
    st.add_argument("--continue-from", help="Text or .txt file path to continue from")

    # --- song ---
    sg = subparsers.add_parser("song", help="Write song lyrics")
    sg.add_argument("--mood", help="Emotional mood (e.g. melancholic, hopeful, angry, joyful)")
    sg.add_argument("--theme", help="Song theme (e.g. 'lost love', 'leaving home', 'resilience')")
    sg.add_argument("--style", help="Genre/style (e.g. 'indie folk', 'R&B', 'country', 'pop')")
    sg.add_argument("--structure", help="Song structure (e.g. VCVCBC for Verse-Chorus-Verse-Chorus-Bridge-Chorus)")
    sg.add_argument("--key", help="Musical key (e.g. G major, D minor)")
    sg.add_argument("--tempo", help="Tempo feel (e.g. slow ballad, mid-tempo, uptempo)")
    sg.add_argument("--rhyme-scheme", help="Rhyme scheme (e.g. ABAB, AABB, ABCB)")
    sg.add_argument("--develop-hook", help="An existing line or hook to develop")

    # --- poem ---
    pm = subparsers.add_parser("poem", help="Generate a poem in any form")
    pm.add_argument(
        "--type",
        help="Poem form (e.g. sonnet, haiku, villanelle, ode, elegy, free verse, ballad)",
    )
    pm.add_argument("--subject", help="Poem subject or topic")
    pm.add_argument("--occasion", help="Occasion (e.g. birthday, memorial, wedding, graduation)")
    pm.add_argument("--for", dest="for_person", help="Who the poem is for (e.g. 'my grandmother')")
    pm.add_argument("--tone", help="Tone (e.g. celebratory, melancholic, humorous, reverent)")
    pm.add_argument("--length", help="Length preference (e.g. short, long, 3 stanzas)")

    # --- caption ---
    cp = subparsers.add_parser("caption", help="Write platform-optimized social media captions")
    cp.add_argument("--image-desc", required=True, help="Description of the image or content")
    cp.add_argument(
        "--platform",
        required=True,
        choices=["instagram", "linkedin", "tiktok", "twitter", "facebook"],
        help="Social media platform",
    )
    cp.add_argument("--tone", help="Caption tone (e.g. inspirational, funny, educational, professional)")
    cp.add_argument("--brand", help="Brand voice or values description")
    cp.add_argument("--cta", help="Desired call-to-action (e.g. 'visit website', 'comment below', 'share')")
    cp.add_argument("--goal", help="Content goal (e.g. 'drive sales', 'build community', 'announce launch')")

    # --- brand ---
    bn = subparsers.add_parser("brand", help="Generate brand name options")
    bn.add_argument("--product", required=True, help="Product or service description")
    bn.add_argument("--audience", help="Target audience description")
    bn.add_argument("--values", help="Brand values (e.g. 'clarity, approachability, innovation')")
    bn.add_argument("--avoid", help="Things to avoid (e.g. 'corporate jargon, hard-to-spell words')")
    bn.add_argument("--count", type=int, default=10, help="Number of name options to generate (default: 10)")
    bn.add_argument(
        "--naming-type",
        choices=["evocative", "coined", "classical", "reframed", "nature", "abstract"],
        help="Preferred naming type",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    dispatch = {
        "story": cmd_story,
        "song": cmd_song,
        "poem": cmd_poem,
        "caption": cmd_caption,
        "brand": cmd_brand,
    }

    handler = dispatch.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
