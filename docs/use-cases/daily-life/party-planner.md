# Party Planner

## Description
Get a complete party planning guide including theme ideas, timeline, food and drink menu, decoration suggestions, activity ideas, and a shopping list — all scaled to your guest count and budget.

## Why Hermes for This
Hermes can coordinate all aspects of event planning simultaneously — balancing budget across food, decor, and activities while ensuring the timeline is realistic. It produces actionable, ready-to-execute plans rather than vague inspiration.

## Quickstart
```bash
cd examples/daily-life
python travel_and_social.py party --type "birthday" --guests 20 --budget 300 --age 30
python travel_and_social.py party --type "dinner party" --guests 8 --budget 150 --diet "mixed including vegan"
```

## Sample Prompt / Input
```
Plan a 30th birthday party for my friend. About 20 guests, mostly mid-20s to early-30s.
Budget: $300. Indoor apartment party. She loves the 90s, brunch food, and dancing.
```

## Expected Output Format
```
**30th Birthday Party Plan**
Theme: 90s Brunch Party | Guests: 20 | Budget: $300 | Venue: Indoor apartment

---
**Theme: "Totally 90s Brunch Bash"**
Aesthetic: Scrunchies, neon, cassette tapes, VHS vibes — but make it chic for a 30th.

---
**Timeline**
- 3 weeks before: Send digital invites (Canva 90s template), create a Spotify playlist
- 2 weeks before: Confirm guest count, order any custom items (banner, cups)
- 1 week before: Buy non-perishable groceries and alcohol
- Day before: Prep make-ahead food, set up decorations
- Day of (2h before): Set out food, create photo booth corner, chill drinks

**Food & Drink Menu (Brunch Style)**
Savory:
- [ ] Egg & cheese mini bagels (batch-bake day-of)
- [ ] Smoked salmon platter with cream cheese and crackers
- [ ] Fruit skewers with yogurt dip

Sweet:
- [ ] Stacked birthday pancakes (as the "cake")
- [ ] Brownie bites

Drinks:
- [ ] Mimosa station (3 bottles prosecco + OJ/cranberry juice)
- [ ] Coffee & tea station
- [ ] Sparkling water + juice for non-drinkers

**Decorations (~$60)**
- [ ] Neon pink & purple balloons (pack of 50, ~$12)
- [ ] "Finally 30" banner (~$8 on Amazon or print on Canva)
- [ ] Cassette tape string lights (~$15)
- [ ] 90s photo props (sunglasses, peace signs) for photo booth corner (~$10)
- [ ] Polaroid camera for instant memories (~borrowed or $15 film)

**Budget Breakdown**
| Category         | Estimated Cost |
|------------------|----------------|
| Food             | $120           |
| Alcohol/Drinks   | $80            |
| Decorations      | $60            |
| Misc/Buffer      | $40            |
| **Total**        | **~$300**      |

**Activity: 90s Music Bingo**
Print bingo cards with 90s song titles. Play a curated 90s playlist — first to get bingo wins a prize (bottle of wine or 90s candy bag). Takes 20-30 min and gets people mingling.
```

## Tips
- Specify dietary restrictions for guests to get an inclusive menu.
- Add `--outdoor` if weather permits for suggestions on outdoor setup and contingency.
- Ask for a kids' party variant with `--age 8` for age-appropriate activities and themes.
- Request a separate day-of timeline checklist to share with helpers.
