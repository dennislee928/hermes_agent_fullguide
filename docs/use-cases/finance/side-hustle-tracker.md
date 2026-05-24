# Side Hustle Tracker

## Description
Analyze your side hustle income, expenses, and time investment to calculate true hourly rate, tax obligations, growth opportunities, and whether scaling or pivoting makes financial sense. Provides a simple profit/loss overview and actionable optimization suggestions.

## Why Hermes
Side hustle analysis benefits from honest, multi-angle assessment — Hermes evaluates both the financial return and the time cost, surfaces often-overlooked tax obligations for self-employment income, and identifies the specific variables that most affect profitability.

## Quickstart
```bash
python examples/finance/budget_tools.py side-hustle --income 800 --expenses "tools:50,platform:15,marketing:30" --hours 20
```

## Sample Input
```
Side hustle type: Freelance graphic design
Monthly revenue: $1,200
Monthly expenses:
  Adobe Creative Cloud: $54.99
  Fiverr/Upwork platform fees (20%): $240
  Marketing/ads: $30
  Equipment depreciation (est.): $25
Monthly hours: 25
Main job salary: $65,000/year
```

## Output Format
```
SIDE HUSTLE ANALYSIS: Freelance Graphic Design
Monthly Revenue: $1,200 | Hours: 25
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FINANCIAL OVERVIEW

Revenue:                    $1,200.00
Platform fees (20%):         -$240.00
Software (Adobe):             -$54.99
Marketing:                    -$30.00
Equipment depreciation:       -$25.00
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Gross Profit:                 $850.01

TAX OBLIGATIONS (estimated)
Self-employment tax (15.3%):  -$130.05
Federal income tax (~22%):    -$187.00
Estimated tax on net income:  -$317.05
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
After-Tax Profit:             $532.96/month
Annual after-tax income:      $6,395.52

TRUE HOURLY RATE
Gross hours: 25/month
Effective after-tax hourly rate: $532.96 ÷ 25 = $21.32/hour

COMPARISON CONTEXT
Your main job effective hourly rate (based on $65,000/2,080 hrs): $31.25/hour
Side hustle effective rate: $21.32/hour

PLATFORM FEE IMPACT
Platform fees are consuming $240/month (20% of revenue). This is the single largest profit leaker.
Recommendation: After establishing relationships on Fiverr/Upwork, migrate recurring clients to direct billing to eliminate platform fees. On $1,200/month revenue, this could add $180-$200/month to your take-home.

SCALING ANALYSIS
If you increased rates by 20% (from implied avg ~$48/hr to ~$58/hr) and kept the same 25 hours:
  New revenue: $1,440
  Additional after-tax: ~$128/month
  This requires raising rates, not more hours — higher leverage.

TAX ACTION ITEMS
1. Make quarterly estimated tax payments (April 15, June 15, Sept 15, Jan 15) to avoid underpayment penalty.
2. Track ALL business expenses — you're likely missing some deductible items.
3. Deductible but not listed: home office (if applicable), professional development, business travel.

GROWTH OPPORTUNITIES
1. Direct client migration: Move 2-3 Upwork clients to direct billing — saves 20% platform fees.
2. Rate increase: Your $21/hr effective rate is below market for experienced graphic designers. A 25% rate increase on existing volume has the highest ROI.
3. Productize: Create fixed-price service packages (e.g., "logo package: $350") to improve pricing power and reduce scope creep.
```

## Tips
- Always calculate the true hourly rate (after taxes) — it's often lower than expected.
- Quarterly tax payments are not optional if you earn over $1,000/year from self-employment — the penalty adds up.
- Track every business expense throughout the year, not just at tax time.
- Platform fees are often the highest-ROI area to attack — direct client relationships eliminate them.
