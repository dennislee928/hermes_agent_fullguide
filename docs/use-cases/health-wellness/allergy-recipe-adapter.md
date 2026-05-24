# Allergy Recipe Adapter

## Description
Submit any recipe and a list of allergens or dietary restrictions. Receive a fully adapted version of the recipe with ingredient substitutions, notes on how each substitution affects texture/flavor, and any technique adjustments needed to make the adapted recipe work.

## Why Hermes
Recipe adaptation requires understanding both the culinary function of each ingredient (gluten's structural role in baking, dairy's fat content in sauces) and the properties of viable substitutes. Hermes provides substitutions that actually work chemically and culinarily, not just nutritionally equivalent swaps.

## Quickstart
```bash
python examples/health-wellness/wellness_tools.py adapt-recipe --file pasta.txt --avoid "gluten, dairy"
```

## Sample Input
```
Recipe: Chicken Alfredo Pasta
Restrictions: dairy-free, gluten-free
```

## Output Format
```
ADAPTED RECIPE: Chicken Alfredo (Dairy-Free, Gluten-Free)
Original restrictions: Remove dairy, remove gluten
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

INGREDIENT SUBSTITUTIONS

| Original | Substitute | Notes |
|----------|------------|-------|
| Fettuccine pasta | Brown rice fettuccine or chickpea pasta | Rice pasta is closest in texture; cook al dente — it overcooks faster than wheat pasta |
| Heavy cream (1 cup) | Full-fat coconut cream (1 cup) | Use a brand with minimal additives. The coconut flavor is mild when paired with garlic and chicken. OR use cashew cream for a more neutral flavor. |
| Parmesan cheese (1 cup, grated) | Nutritional yeast (3 tbsp) + cashew cream (¼ cup) | Nutritional yeast provides umami/cheesy flavor; cashew cream adds richness. Combined they approximate Parmesan's role. |
| Butter (2 tbsp) | Vegan butter or extra-virgin olive oil | Olive oil changes the flavor profile slightly toward Mediterranean; vegan butter maintains a more traditional richness. |
| All-purpose flour (for thickening, if used) | Tapioca starch or arrowroot (1:1) | Whisk into cold liquid before adding to the pan to prevent lumps. |

TECHNIQUE ADJUSTMENTS
1. Make the cashew cream ahead: Soak 1 cup raw cashews in water 4+ hours, drain, blend with ½ cup water until very smooth. Strain if needed.
2. The sauce may be slightly thinner than traditional Alfredo — add 1 tsp tapioca starch dissolved in cold water and simmer to thicken.
3. Brown rice pasta: Boil in well-salted water, test frequently from 7 minutes. It goes from al dente to mushy quickly.

FLAVOR NOTES
This adaptation produces a sauce that is creamy and savory with a subtle richness. It will not taste identical to dairy Alfredo but is genuinely delicious. The key is the nutritional yeast — don't omit it.

CROSS-CONTAMINATION NOTE
If this is for a serious dairy or gluten allergy (not just a preference), ensure all equipment, cookware, and the chicken itself (some marinated chicken contains gluten) are certified free of cross-contamination.
```

## Tips
- List all allergens explicitly: `--avoid "gluten, dairy, eggs, tree nuts"` for multi-allergy adaptations.
- For baking, specify `--type baking` — baking adaptations are chemically more complex and need the flag.
- Ask for alternative substitutions: "give me 3 different dairy-free cream substitutes with pros and cons."
- Always check manufacturer labels of substitute ingredients for hidden allergens.
