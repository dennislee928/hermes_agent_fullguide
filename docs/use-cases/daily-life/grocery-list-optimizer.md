# Grocery List Optimizer

## Description
Convert a set of planned meals into a deduplicated, aisle-organized grocery list with quantities and optional cost estimates. It eliminates duplicate ingredients across recipes and groups items by store section for efficient shopping.

## Why Hermes for This
Hermes's ability to reason about ingredient overlap across multiple recipes — and then reorganize output by category — makes it ideal for this aggregation task. It produces clean, structured lists without manual cross-referencing.

## Quickstart
```bash
cd examples/daily-life
python food_and_nutrition.py grocery --meals "pasta bolognese, caesar salad, vegetable soup"
python food_and_nutrition.py grocery --meals "tacos,stir fry,omelette" --servings 4
```

## Sample Prompt / Input
```
I'm making these meals this week: pasta bolognese (2 servings), Caesar salad (4 servings), vegetable soup (6 servings).
Generate an optimized grocery list organized by store aisle. Combine duplicate ingredients and show total quantities.
```

## Expected Output Format
```
**Grocery List — 3 Meals, ~4 Servings Average**

**Produce**
- [ ] Romaine lettuce, 1 large head
- [ ] Carrots, 4 medium
- [ ] Celery, 3 stalks
- [ ] Onion, 2 medium
- [ ] Garlic, 1 bulb

**Meat & Seafood**
- [ ] Ground beef, 500 g

**Dry Goods & Pasta**
- [ ] Spaghetti, 400 g
- [ ] Canned diced tomatoes, 2 × 400 g cans
- [ ] Chicken broth, 1 L carton

**Dairy & Eggs**
- [ ] Parmesan cheese, 100 g block
- [ ] Eggs, 4

**Pantry (likely have)**
- Olive oil, salt, pepper, dried herbs
```

## Tips
- Pass `--servings N` to scale all quantities to your household size.
- Add `--budget 50` to get a rough cost-awareness note per section.
- Combine with the meal planner output by piping its meals directly into this command.
- The "likely have" section can be suppressed with `--no-pantry-items`.
