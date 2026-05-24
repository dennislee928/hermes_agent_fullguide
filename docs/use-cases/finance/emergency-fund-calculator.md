# Emergency Fund Calculator

## Description
Calculate your personalized emergency fund target based on monthly expenses, job security, dependents, and income stability. Provides a tiered savings goal, a monthly contribution plan to reach it, and guidance on where to keep emergency funds for optimal liquidity and yield.

## Why Hermes
Emergency fund guidance is most useful when personalized — someone with two incomes, no dependents, and high job security needs a smaller buffer than a single parent with variable income. Hermes adjusts the target and timeline based on the individual's actual risk profile rather than applying a one-size-fits-all "3-6 months" rule.

## Quickstart
```bash
python examples/finance/budget_tools.py emergency-fund --monthly-expenses 3200 --months 6
```

## Sample Input
```
Monthly essential expenses: $3,200
Employment type: Freelancer (variable income)
Dependents: 1 child
Job market: Specialized field (longer average job search)
Current emergency fund: $4,000
Monthly savings capacity: $400
```

## Output Format
```
EMERGENCY FUND CALCULATOR
Monthly Expenses: $3,200 | Current Savings: $4,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RISK PROFILE ASSESSMENT
Freelancer (variable income):     HIGH risk — no employer income guarantee
One dependent (child):            MEDIUM additional risk — higher consequence of income gap
Specialized field:                MEDIUM-HIGH — longer job search if needed

RECOMMENDATION: 9-MONTH EMERGENCY FUND
Standard advice is 3-6 months. Your risk profile (freelance + dependent + specialized field) warrants 6-9 months.

TIERED TARGETS

Tier 1 — Minimum Safety Net (3 months): $9,600
Current savings: $4,000 | Gap: $5,600
At $400/month: 14 months to reach Tier 1
Milestone: Once reached, you have basic protection.

Tier 2 — Recommended Target (6 months): $19,200
Gap from current: $15,200
At $400/month: 38 months (~3.2 years)
Milestone: Adequate for most emergencies.

Tier 3 — Optimal for Your Profile (9 months): $28,800
Gap from current: $24,800
At $400/month: 62 months (~5.2 years)
Note: Increase contributions as income allows; also supplemented by income during lean months.

ACCELERATED PLAN OPTIONS

Option A — Increase savings to $600/month
  Tier 1: 10 months | Tier 2: 26 months | Tier 3: 42 months

Option B — Direct one-time windfall (tax return, bonus) to fund
  $2,000 one-time + $400/month: Tier 1 in 9 months

WHAT TO COUNT AS EMERGENCY EXPENSES
Essential only (do not include):
✓ Rent/mortgage
✓ Utilities
✓ Groceries (conservative estimate)
✓ Insurance premiums
✓ Minimum debt payments
✓ Childcare
✗ Subscriptions, dining, entertainment — these are cuttable in a real emergency

WHERE TO KEEP IT

DO: High-yield savings account (HYSA)
  Current rates (2024): 4.5-5.2% APY
  Providers: Ally, Marcus (Goldman), SoFi, Discover
  Recommendation: Keep 1-2 months at your primary bank for instant access; remaining in HYSA.

DON'T: Checking account (earns nothing), Investment account (may be down when you need it), CD (locked up with penalties)

FREELANCER-SPECIFIC NOTE
Because your income is variable, your emergency fund also serves as an income buffer during low-revenue months. Consider keeping your "slow month" buffer (1-2 months of expenses) in the same HYSA — separate from your true emergency fund in your mental accounting, but accessible from the same account.

FIRST STEP
Open a HYSA today (takes 10 minutes). Transfer your existing $4,000 out of checking. You're already 42% of the way to Tier 1.
```

## Tips
- Use essential expenses only (not total spending) as the base — you can cut discretionary spending in an emergency.
- Freelancers and contract workers should target the higher end of the range.
- A HYSA at 4-5% APY means your emergency fund earns meaningful interest — there's no reason to keep it in a 0% checking account.
- Once fully funded, maintain it — replenish immediately after any withdrawal.
