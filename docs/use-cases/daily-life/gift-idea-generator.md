# Gift Idea Generator

## Description
Generate thoughtful, personalized gift ideas based on the recipient's interests, age, relationship to you, occasion, and budget. Suggestions range from experiential gifts to physical items with specific product category guidance.

## Why Hermes for This
Hermes can combine multiple personal attributes (interests, age, budget, occasion) to suggest gifts that feel genuinely considered rather than generic. It understands why certain gifts work for certain people and explains the reasoning.

## Quickstart
```bash
cd examples/daily-life
python travel_and_social.py gift --for "dad, 58, loves fishing and cooking" --budget 75 --occasion "birthday"
python travel_and_social.py gift --for "best friend, late 20s, into yoga and travel" --budget 50 --occasion "christmas"
```

## Sample Prompt / Input
```
Gift for: My dad, 58 years old, retired. Loves fishing, cooking (especially BBQ),
and watching football. Doesn't like clutter. Budget: $75. Occasion: Father's Day.
```

## Expected Output Format
```
**Gift Ideas — Dad, 58 | Father's Day | Budget: $75**
Interests: Fishing, BBQ, Football | Note: Prefers non-cluttered gifts

---
**Top Picks**

1. **Personalized Fishing Lure Set** (~$35-50)
   A custom set of high-quality lures in his favorite fish species' colors.
   Consumable (doesn't add clutter), practical, and personalized. Pair with a
   handwritten note about a specific fishing memory for extra impact.
   *Search: "personalized fishing lure set" on Etsy or Bass Pro Shops*

2. **BBQ Rub & Sauce Gift Set** (~$40-60)
   Curated collection of small-batch rubs and sauces from different regional BBQ traditions.
   Consumable, zero clutter, directly serves his hobby. Many come in attractive gift boxes.
   *Search: "BBQ rub sampler gift set" on Amazon or local specialty food store*

3. **Experience: Guided Fishing Trip** (~$75-150 depending on location)
   Book a half-day guided fishing trip in your area. The best non-clutter gift — creates
   a shared memory. Even better if you join him.
   *Search: "[your city] guided fishing trip day license"*

4. **Football Stadium Food Cookbook** (~$30) + Specialty Hot Sauce (~$20)
   Combines football and cooking. "Stadium Eats" style cookbooks are popular and novel.
   *Budget-friendly combo with room for a gift card to his favorite team's store*

5. **Personalized BBQ Branding Iron** (~$40-60)
   Stamps his initials into steaks and brisket. Novel, useful, and durable.
   *Search: "personalized BBQ branding iron" — widely available online*

**Experience Gift Tip:** For someone who "doesn't like clutter," experiential gifts
(fishing trip, cooking class, game tickets) are almost always the best choice.
```

## Tips
- The more specific you are about the person's interests, the more targeted the suggestions.
- Mention items they already own to avoid duplicates (e.g., "already has a good rod").
- Add `--diy` to get handmade gift ideas if you want to make something personal.
- Ask for a "budget under $20" version for coworkers or acquaintances.
