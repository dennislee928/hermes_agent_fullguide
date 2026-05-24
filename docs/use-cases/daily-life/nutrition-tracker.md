# Nutrition Tracker

## Description
Analyze a list of foods and portions to estimate calories, macronutrients (protein, carbs, fat), and key micronutrients (fiber, sodium, vitamins). It also flags nutritional gaps and suggests simple improvements.

## Why Hermes for This
Hermes has broad knowledge of common food nutritional profiles and can reason about dietary balance without requiring an external database API. It provides immediate, conversational feedback rather than a raw data dump.

## Quickstart
```bash
cd examples/daily-life
python food_and_nutrition.py nutrition "200g chicken breast, 100g brown rice, 1 cup broccoli, 1 tbsp olive oil"
python food_and_nutrition.py nutrition "2 eggs scrambled, 2 slices toast, 1 cup orange juice"
```

## Sample Prompt / Input
```
Analyze the nutritional content of this meal:
- 200g grilled chicken breast
- 100g cooked brown rice
- 1 cup steamed broccoli
- 1 tablespoon olive oil

Give me calories, protein, carbs, fat, fiber, and any notable vitamins or minerals.
```

## Expected Output Format
```
**Nutritional Analysis**

| Nutrient      | Amount     | % Daily Value (2000 kcal) |
|---------------|------------|---------------------------|
| Calories      | ~540 kcal  | 27%                       |
| Protein       | ~52 g      | 104%                      |
| Carbohydrates | ~42 g      | 14%                       |
| Fat           | ~15 g      | 19%                       |
| Fiber         | ~5 g       | 18%                       |
| Sodium        | ~150 mg    | 7%                        |

**Highlights:**
- Excellent protein source — well above the single-meal target.
- Good complex carbs from brown rice; low glycemic impact.
- Broccoli contributes Vitamin C (~90% DV) and Vitamin K.

**Suggestions:**
- Add a small portion of healthy fats (avocado, nuts) to boost omega-3s.
- Consider a calcium source such as yogurt or cheese with another meal today.
```

## Tips
- Use common measurements (grams, cups, tablespoons) for best accuracy.
- Track a full day by listing all meals together for cumulative totals.
- Specify a target (e.g., `--goal muscle-gain`) to get context-aware advice.
- Note that estimates are approximate — consult a registered dietitian for medical nutrition therapy.
