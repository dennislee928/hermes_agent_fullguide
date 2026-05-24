# Business Idea Validator

## Description
Business Idea Validator stress-tests a business concept by analyzing market opportunity, competitive landscape, key assumptions, and potential failure modes. It gives entrepreneurs an honest, structured initial assessment before investing significant time or money.

## Why Hermes
Hermes applies structured analytical frameworks (problem/solution fit, market sizing, competitive moats, risk analysis) to business ideas without the cheerleading bias that often inflates early-stage evaluations. It asks the right hard questions and surfaces blind spots.

## Quickstart
```bash
python examples/work-productivity/business_tools.py validate-idea \
  --idea "A subscription app that helps remote workers find co-working day passes globally" \
  --market B2C \
  --stage "pre-revenue, idea stage"
```

## Sample Input
```
Idea: A platform where small restaurants can list their empty tables during off-peak hours
      as "remote work spots" for $10/day. Restaurants earn extra revenue; workers get
      cheap, charming workspaces.
Target market: Urban remote workers + independent restaurants
Stage: Idea stage, no product built yet
My background: 5 years in restaurant ops, no tech background
```

## Expected Output Format
```
Business Idea Validation: Restaurant Remote Work Platform

PROBLEM CLARITY: Strong
The underutilized restaurant table problem is real and well-documented.
Remote workers seeking affordable, non-coffee-shop spaces is a growing need.

MARKET OPPORTUNITY: Moderate
TAM estimate: ~15M remote workers in the US willing to pay for flex workspace
SAM (urban, restaurant-adjacent): ~1.5M potential users
$10/day x 1.5M users x 2 days/week = ~$1.5B annual market at full penetration
Comparable: Peerspace, LiquidSpace (B2B focus), Workfrom (directory model)

KEY ASSUMPTIONS TO TEST
1. Restaurants will participate at $10 table fee split (test: 10 restaurant signups)
2. Workers will prefer restaurants over coffee shops (test: 50 user interviews)
3. $10/day is the right price point (test: A/B pricing survey)
4. Both sides will use an app vs. direct contact (test: simple landing page)

RISKS & RED FLAGS
1. Two-sided marketplace cold start — chicken-and-egg acquisition problem. 
   Mitigation: Launch city-by-city, handpick first 20 restaurants.

2. Unit economics: at $10/table, revenue share and payment processing leaves 
   thin margins. Need to model carefully.

3. Founder-market fit: restaurant ops experience is strong; tech build is a gap.
   Mitigation: Find a technical co-founder or use no-code tools to validate first.

OVERALL VERDICT: Promising Idea — Validate Before Building
Recommended next step: Build a 2-page landing page, run Google Ads for $200,
and see if workers sign up before any restaurant does. This tests demand first.
```

## Tips
- Be honest in `--stage`; validation for "idea stage" vs. "revenue stage" looks very different.
- Use `--devil-advocate` flag to get a stronger critical analysis with more failure modes.
- Combine with the Project Timeline Estimator to sketch out a validation roadmap.
- Re-run after each major assumption test to see if the assessment changes.
