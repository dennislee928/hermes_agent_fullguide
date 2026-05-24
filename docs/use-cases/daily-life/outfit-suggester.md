# Outfit Suggester

## Description
Get complete outfit recommendations tailored to a specific occasion, weather conditions, and available wardrobe pieces. Suggestions include clothing, footwear, and accessories with styling rationale.

## Why Hermes for This
Hermes understands fashion context — dress codes, seasonal appropriateness, color coordination, and occasion-specific norms — and can provide confident, specific suggestions rather than vague generalities.

## Quickstart
```bash
cd examples/daily-life
python home_and_lifestyle.py outfit --occasion "job interview" --weather "cold"
python home_and_lifestyle.py outfit --occasion "beach wedding" --weather "hot and sunny"
python home_and_lifestyle.py outfit --occasion "first date dinner" --weather "mild" --style "smart casual"
```

## Sample Prompt / Input
```
I have a job interview at a tech startup (business casual environment).
Weather: 55°F / 13°C, light rain expected.
My available items: navy chinos, black jeans, white Oxford shirt, grey crewneck sweater,
brown leather loafers, white sneakers, olive bomber jacket, black wool overcoat.
Suggest a complete outfit.
```

## Expected Output Format
```
**Outfit Recommendation — Tech Startup Interview**
Occasion: Business casual | Weather: 55°F, light rain

---
**Recommended Look: Smart Casual with Polish**

| Item          | Piece                     | Why It Works                                      |
|---------------|---------------------------|---------------------------------------------------|
| Bottoms       | Navy chinos               | Clean, professional, versatile                    |
| Top           | White Oxford shirt        | Crisp and interview-appropriate                   |
| Layer         | Grey crewneck sweater     | Adds warmth and a modern, relaxed-professional vibe |
| Outerwear     | Black wool overcoat       | Rain-resistant and polished — better than the bomber for an interview |
| Shoes         | Brown leather loafers     | Complements navy/grey palette; appropriate formality |

**Styling Tips:**
- Tuck the Oxford in partially (French tuck) for a modern, intentional look.
- Roll the chino cuffs once to avoid getting them wet from rain splashes.
- The navy + grey + brown palette is classic and effortlessly put-together.
- Skip a tie — at a tech startup it would read as overdressed.

**Alternative (if chinos are wrinkled):**
Black jeans + white Oxford + grey sweater + black overcoat + brown loafers — still professional, slightly more casual.
```

## Tips
- List your actual wardrobe items for outfit suggestions you can immediately use.
- Specify dress code explicitly (business formal, smart casual, black tie) when known.
- Add `--budget 100` to get shopping suggestions for missing pieces.
- Ask for "capsule wardrobe advice" to get higher-level guidance on building a versatile closet.
