# Retirement Planner

## Description
Input your current age, savings, income, and retirement goals to receive a personalized retirement projection with savings milestones, account type recommendations (401k, IRA, Roth), contribution strategies, and a gap analysis showing what adjustments are needed to reach your target.

## Why Hermes
Retirement planning involves compounding calculations, tax optimization across account types, and translating abstract numbers into concrete monthly action steps. Hermes performs these calculations and presents the results in a way that motivates action rather than overwhelming with complexity.

## Quickstart
```bash
python examples/finance/financial_advisor.py retirement --age 32 --savings 45000 --income 75000 --target-age 65
```

## Sample Input
```
Current age: 35
Current retirement savings: $45,000
Annual income: $80,000
Employer 401k match: 4% of salary
Current contribution: 6% of salary
Target retirement age: 65
Expected retirement income need: $60,000/year (today's dollars)
```

## Output Format
```
RETIREMENT PROJECTION
Age: 35 | Current Savings: $45,000 | Income: $80,000
Target: Retire at 65 with $60,000/year income
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RETIREMENT TARGET
To fund $60,000/year for 25 years (age 65-90) with 3% inflation adjustment:
Required nest egg at retirement: approximately $1,500,000 (4% withdrawal rule)
Inflation-adjusted target (30 years of growth): $1,500,000

CURRENT TRAJECTORY

Current annual contribution:
  Your 6% of $80,000: $4,800/year
  Employer 4% match: $3,200/year
  Total: $8,000/year

Projection at current rate (7% avg annual return):
  At age 65: approximately $1,087,000

GAP ANALYSIS
Target: $1,500,000
Projected: $1,087,000
Shortfall: ~$413,000 (27% gap)

To close the gap — options:

Option A: Increase contribution to 10% of salary
  Additional from you: $3,200/year more
  Projected result: ~$1,410,000 (nearly on target)

Option B: Increase contribution to 12% of salary
  Additional from you: $4,800/year more
  Projected result: ~$1,580,000 (exceeds target)

Option C: Retire at 67 instead of 65
  At current 6% contribution: ~$1,265,000 (reduces gap)

RECOMMENDATION
Increase your 401k contribution from 6% to 10% of salary ($266/month more). This is the single highest-impact change you can make. The impact of each additional contribution dollar is larger now (at 35) than it will be at 55 — time is your most valuable financial asset.

ACCOUNT STRATEGY

Priority order for retirement savings:
1. 401k up to employer match (4% — you're doing this): NEVER leave free money on the table.
2. Max Roth IRA ($7,000/year limit, 2024): Tax-free growth and withdrawals.
3. Max 401k ($23,000/year limit, 2024): Higher contribution limits than IRA.
4. Taxable brokerage: Additional savings beyond tax-advantaged limits.

TAX CONSIDERATION
At $80,000 income, you're likely in the 22% federal bracket. Traditional 401k contributions reduce taxable income now (worth 22 cents per dollar contributed). Roth IRA grows tax-free for retirement. Optimal strategy: maximize traditional 401k first, then Roth IRA.

MILESTONES TO AIM FOR
Age 40: $175,000 saved (on 10% contribution track)
Age 45: $320,000
Age 50: $540,000 (can now make $7,500 catch-up contributions)
Age 55: $820,000
Age 60: $1,200,000
Age 65: $1,580,000

DISCLAIMER: Projections assume 7% average annual return (historical long-term average), not guaranteed. Consult a licensed financial planner for personalized retirement advice.
```

## Tips
- The most important variable is how early you start — starting at 25 vs 35 can mean $500,000+ difference.
- Always capture the full employer match before contributing to any other account — it's an instant 100% return.
- Increase contributions by 1% each year — you rarely notice the difference in take-home pay.
- Run again after any major life change: marriage, salary increase, inheritance, career change.
