# Weekly Meal Planner

## Description
Generate a structured 7-day meal plan tailored to dietary preferences, caloric goals, and cooking skill level. The plan includes breakfast, lunch, dinner, and optional snacks for every day of the week.

## Why Hermes for This
Hermes can juggle multiple constraints simultaneously — calories, macros, diet type, cuisine variety, and prep time — while outputting a clean, table-formatted plan ready to print or paste into a notes app.

## Quickstart
```bash
cd examples/daily-life
python food_and_nutrition.py meal-plan --days 7 --diet vegetarian
python food_and_nutrition.py meal-plan --days 5 --diet keto --calories 1800
```

## Sample Prompt / Input
```
Create a 7-day vegetarian meal plan targeting 2000 calories per day.
Include breakfast, lunch, dinner, and one snack.
Prefer quick meals (under 30 minutes) on weekdays.
```

## Expected Output Format
```
**7-Day Vegetarian Meal Plan (~2000 kcal/day)**

| Day       | Breakfast            | Lunch                  | Dinner                  | Snack           |
|-----------|----------------------|------------------------|-------------------------|-----------------|
| Monday    | Greek yogurt parfait | Lentil soup + bread    | Veggie stir-fry + rice  | Apple + almonds |
| Tuesday   | Oatmeal + berries    | Caprese salad + wrap   | Black bean tacos        | Hummus + veggies|
...

**Weekly Prep Notes:**
- Cook a large batch of lentils on Sunday for Mon/Wed lunches.
- Pre-chop stir-fry vegetables on Sunday evening.
```

## Tips
- Specify allergies (e.g., `--no-nuts`, `--no-dairy`) to avoid unsafe suggestions.
- Use `--cuisine mediterranean` or `--cuisine asian` to theme the week.
- Request a combined grocery list at the end by adding `--grocery-list` flag.
- Re-run with a different random seed phrase to get variety across weeks.
