# Restaurant Recommender

## Description
Get restaurant recommendations tailored to cuisine type, occasion, dietary restrictions, and atmosphere preference. While Hermes cannot access real-time review sites, it provides search strategies, what to look for, and cuisine-specific guidance for any city.

## Why Hermes for This
Hermes excels at providing context-rich, nuanced guidance on what makes a great restaurant for a specific occasion — helping users know exactly what to search for and what questions to ask, rather than just listing names that may be outdated.

## Quickstart
```bash
cd examples/daily-life
python travel_and_social.py restaurant --city "Tokyo" --cuisine "ramen" --occasion "casual lunch"
python travel_and_social.py restaurant --city "New York" --occasion "anniversary dinner" --budget "upscale" --diet "vegetarian"
```

## Sample Prompt / Input
```
I'm in Tokyo and want an authentic ramen experience for a casual lunch.
I prefer tonkotsu or miso broth. Budget: under ¥1,500. Solo diner.
What should I look for and where should I search?
```

## Expected Output Format
```
**Ramen Recommendations — Tokyo (Casual Lunch)**
Style: Tonkotsu or Miso | Budget: Under ¥1,500 | Solo dining

---
**What to Look For**
- Queue outside at lunchtime = local quality signal; most good ramen shops have short waits
- Vending machine ordering (ticket machines) = authentic, established shop
- Solo counter seating (カウンター) is standard — no awkwardness dining alone
- Look for shops with limited menu — specialty shops focusing on one broth style are usually better

**Recommended Search Strategies**
1. Google Maps: Search "家系ラーメン" (ie-kei, tonkotsu-soy hybrid) or "味噌ラーメン Tokyo"
2. Tabelog.com — Japan's top review site; filter by ラーメン + your ward/district
3. Ramen Beast (ramenb.com) — English-language guide by neighborhood

**Neighborhoods with High Ramen Density**
- Shinjuku / Takadanobaba — large variety, very accessible
- Shibuya — tourist-friendly shops with English menus
- Ikebukuro — known for rich tonkotsu, particularly ie-kei style

**Ordering Tips**
- "Katamen" (硬め) = firm noodles; "yawarakame" (柔らかめ) = soft
- "Karame" (辛め) = stronger tare (seasoning); "usume" (薄め) = lighter
- Add "hanjuku tamago" (soft-boiled egg) — it's worth the ¥100-150 extra

**Price Range:** Most bowls ¥900-1,300 | Extra toppings ¥100-200 each
```

## Tips
- Specify the district or neighborhood for hyper-local suggestions.
- Mention dietary restrictions upfront (halal, vegetarian, nut allergy) — the model will flag cuisine types to avoid.
- Ask for "hidden gem vs. famous spot" distinction if you want to avoid tourist traps.
- For restaurant searches without a specific city, describe the atmosphere (cozy, lively, romantic) for better guidance.
