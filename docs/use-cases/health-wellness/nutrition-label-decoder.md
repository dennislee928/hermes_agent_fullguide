# Nutrition Label Decoder

## Description
Paste any nutrition label data and receive a plain-language breakdown of what the numbers actually mean for your health — contextualizing calories, macronutrients, sodium, sugar, fiber, and vitamins against daily recommended values and common dietary guidelines.

## Why Hermes
Nutrition labels are dense with numbers that are meaningless without context. Hermes translates them into practical insight — noting when sodium is high for a single serving, when "low fat" actually means high sugar, or when a product is genuinely nutritious versus cleverly marketed.

## Quickstart
```bash
python examples/health-wellness/wellness_tools.py nutrition --label "Calories 250, Fat 12g, Sodium 480mg, Sugar 8g"
```

## Sample Input
```
Product: "Healthy Harvest Granola Bar"
Serving size: 1 bar (45g)
Servings per container: 6
Calories: 190
Total Fat: 7g (Saturated Fat: 1g, Trans Fat: 0g)
Cholesterol: 0mg
Sodium: 140mg
Total Carbohydrate: 29g (Dietary Fiber: 3g, Total Sugars: 12g, Added Sugars: 8g)
Protein: 4g
Vitamin D: 0mcg, Calcium: 20mg, Iron: 1mg, Potassium: 150mg
```

## Output Format
```
NUTRITION LABEL ANALYSIS: Healthy Harvest Granola Bar
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OVERVIEW
190 calories per bar is moderate for a snack — equivalent to roughly a banana + tablespoon of peanut butter. If you eat the whole package (6 bars), that's 1,140 calories, roughly half a typical adult's daily intake.

CALORIE CONTEXT
190 cal/bar — Reasonable for a snack; moderate for a "healthy" bar

FAT ANALYSIS
Total Fat: 7g (9% daily value) — Moderate
Saturated Fat: 1g — Low (good)
Trans Fat: 0g — Good

CARBOHYDRATES & SUGAR — Worth Scrutinizing
Total Carbs: 29g — Moderate
Dietary Fiber: 3g — Decent (10% DV; aim for 25-38g/day)
Total Sugar: 12g — Moderate
Added Sugar: 8g — This is where to pay attention.
The American Heart Association recommends no more than 25g (women) / 36g (men) of added sugar daily. One bar uses 32% of a woman's daily added sugar budget. "Healthy" bars often hide significant added sugar.

SODIUM: 140mg (6% DV) — Low and acceptable for a snack

PROTEIN: 4g — Low. This bar will not keep you full long. Consider pairing with a protein source.

MARKETING REALITY CHECK
The name "Healthy Harvest" and natural-seeming branding are worth skepticism. The added sugar content (8g per bar) is higher than you might expect from packaging that implies wholesome ingredients. Compare to alternatives with <5g added sugar.

VERDICT
A serviceable snack with decent fiber but notable added sugar and low protein. Fine occasionally; not ideal as a daily staple if managing blood sugar or calorie intake.
```

## Tips
- Compare similar products: paste two labels and ask "which is healthier and why?"
- Watch for serving size manipulation — a "100 calorie" serving is meaningless if you eat three.
- High fiber (5g+/serving) and protein (10g+/serving) are the best markers of a genuinely satiating snack.
- Always check added sugars separately from total sugars — naturally occurring sugars in fruit/dairy are different.
