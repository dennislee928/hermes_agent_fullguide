# Vacation Itinerary Planner

## Description
Create a day-by-day vacation itinerary with time-blocked activities, restaurant recommendations, travel logistics, and estimated costs. The plan balances must-see highlights with downtime so it stays enjoyable rather than exhausting.

## Why Hermes for This
Hermes has broad destination knowledge and can reason about geographic proximity (grouping nearby attractions), pacing (rest days, travel times), and preference matching (culture-heavy vs. relaxation-focused trips).

## Quickstart
```bash
cd examples/daily-life
python travel_and_social.py itinerary --destination "Kyoto, Japan" --days 5 --style "cultural"
python travel_and_social.py itinerary --destination "Barcelona" --days 7 --style "food and art" --budget moderate
```

## Sample Prompt / Input
```
Plan a 5-day itinerary for Kyoto, Japan in April (cherry blossom season).
I love temples, traditional food, and photography. Moderate budget.
I'm a solo traveler comfortable using public transport.
```

## Expected Output Format
```
**5-Day Kyoto Itinerary — Cherry Blossom Season**
Travel style: Cultural / Photography | Budget: Moderate | Transport: Public transit + walking

---
**Day 1 — Arrival & Higashiyama District**
Morning:
- Arrive Kyoto Station; check in to guesthouse near Gion (~¥5,000-8,000/night)
- Lunch: Nishiki Market — try yudofu (tofu hot pot) and street skewers (~¥1,500)

Afternoon:
- Kiyomizudera Temple (¥400) — arrive before 3 PM to beat crowds; stunning mountain views
- Walk the Sannen-zaka and Ninen-zaka stone-paved lanes

Evening:
- Gion neighborhood stroll at dusk — best chance to spot maiko (apprentice geiko)
- Dinner: Izakaya near Gion — yakitori and local sake (~¥2,500)

---
**Day 2 — Arashiyama Bamboo Grove & Temples**
...

**Day 5 — Nishiki, Fushimi Inari & Departure**
...

---
**Logistics**
- IC Card (Suica/ICOCA): Load ¥3,000-5,000 for buses and trains
- Best cherry blossom spots: Maruyama Park (free), Philosopher's Path, Arashiyama
- Book popular restaurants 1-2 days ahead via Tabelog or walk-in at lunch

**Estimated Daily Budget**
Accommodation: ¥6,000 | Food: ¥3,000 | Attractions: ¥1,500 | Transport: ¥800
**Total 5-day estimate: ~¥55,000 (~$370 USD)**
```

## Tips
- Specify travel style (adventure, relaxation, culture, food) for a tailored tone.
- Add `--pace slow` for a less packed schedule with more spontaneous time built in.
- Ask for a rainy-day backup plan for each day if your destination is weather-dependent.
- Include arrival and departure times so the model can plan Day 1 and last-day logistics accurately.
