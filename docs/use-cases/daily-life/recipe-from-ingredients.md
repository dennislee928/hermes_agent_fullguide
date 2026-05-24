# Recipe From Ingredients

## Description
Turn whatever is already in your fridge or pantry into a complete, step-by-step recipe without a trip to the store. Hermes understands ingredient combinations, cooking techniques, and dietary constraints so the result is both practical and delicious.

## Why Hermes for This
Hermes excels at open-ended creative generation with hard constraints — it respects the "only these ingredients" boundary while still producing coherent, well-structured culinary output. Its instruction-following capability means it won't hallucinate exotic items you don't have.

## Quickstart
```bash
cd examples/daily-life
python food_and_nutrition.py recipe "chicken, rice, tomatoes, garlic, olive oil"
```

## Sample Prompt / Input
```
Ingredients I have: chicken breast, cooked rice, canned tomatoes, garlic, olive oil, dried oregano, salt, pepper.
Suggest a complete dinner recipe using only these items.
```

## Expected Output Format
```
**One-Pan Garlic Tomato Chicken with Rice**

Prep time: 10 min | Cook time: 25 min | Serves: 2

**Ingredients:**
- 2 chicken breasts
- 1 cup cooked rice
- 1 can (400 g) diced tomatoes
...

**Instructions:**
1. Heat olive oil in a skillet over medium-high heat.
2. Season chicken with salt, pepper, and oregano; sear 4 min per side.
...

**Tips:** Cover the pan for the last 5 minutes to keep the chicken moist.
```

## Tips
- List quantities if you know them — the model will scale the recipe accordingly.
- Add a dietary flag like `--diet gluten-free` to filter out incompatible techniques (e.g., flour-based thickeners).
- Ask for multiple recipe variations by appending "give me 3 options" to your prompt.
- Mention your cooking equipment (air fryer, Instant Pot) for tailored instructions.
