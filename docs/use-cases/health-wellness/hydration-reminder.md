# Hydration Reminder

## Description
Calculate personalized daily water intake goals based on weight, activity level, climate, and health goals. Generates a practical hydration schedule with timing cues and tips for building consistent hydration habits throughout the day.

## Why Hermes
Hydration advice is most useful when personalized and actionable. Hermes combines the relevant physiological factors (body weight, exercise sweat rate, climate) to produce a realistic daily schedule rather than generic "drink 8 glasses" advice.

## Quickstart
```bash
python examples/health-wellness/mindfulness_tools.py hydration --weight 70 --unit kg --activity moderate --climate hot
```

## Sample Input
```
Weight: 165 lbs
Activity level: moderately active (30-60 min exercise most days)
Climate: hot and humid
Goal: improve energy levels
```

## Output Format
```
PERSONALIZED HYDRATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━

DAILY TARGET: 3.2 liters (approx. 108 oz / 13.5 cups)
Calculation basis: 165 lbs (75 kg) × 35ml/kg base = 2.6L + 400ml activity adjustment + 200ml climate adjustment

DAILY SCHEDULE
7:00 AM  — Wake up: 500ml (2 cups) immediately. Your body is dehydrated after sleep.
8:30 AM  — With breakfast or commute: 250ml (1 cup)
10:00 AM — Mid-morning: 250ml (1 cup)
12:00 PM — Before lunch: 250ml (1 cup) — drinking before meals aids digestion and reduces overeating
1:00 PM  — With/after lunch: 250ml (1 cup)
3:00 PM  — Afternoon energy dip: 500ml (2 cups) — the 3pm slump is often dehydration
5:00 PM  — Pre-workout: 500ml (2 cups) starting 1-2 hours before exercise
6:30 PM  — During exercise: 150-250ml every 20 minutes
7:30 PM  — Post-workout recovery: 500ml (2 cups) to replace sweat losses
9:00 PM  — Evening: 200ml (last large intake — avoid large amounts 1hr before bed)

TOTAL: 3.4 liters (slight buffer above target)

HYDRATION TIPS FOR YOUR GOALS
- Energy: Dehydration as mild as 1-2% body weight reduces cognitive performance and physical energy. Morning hydration before caffeine makes a measurable difference.
- Hot climate: Add an extra 200-500ml on days above 30°C or when sweating heavily.
- Electrolytes: If exercising over 60 minutes, consider adding a pinch of salt or electrolyte supplement to post-workout water to aid reabsorption.

HYDRATION HABIT BUILDER
- Link each water intake to an existing habit (wake up, each meal, each coffee)
- Use a marked 1L bottle to track progress visually
- Urine color check: pale yellow = good; dark yellow = drink more; clear = slightly over-hydrated
```

## Tips
- Re-run in winter and summer as climate adjustments significantly affect targets.
- Use `--medical "kidney stones"` to get condition-specific hydration guidance (always verify with your doctor).
- Track urine color as the simplest real-time hydration indicator.
- Coffee and tea count toward hydration despite mild diuretic effects at typical consumption levels.
