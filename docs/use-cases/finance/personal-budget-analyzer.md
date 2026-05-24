# Personal Budget Analyzer

## Description
Input your monthly income and expense categories to receive a structured budget analysis: spending ratios, comparison to common budgeting frameworks (50/30/20), identification of overspending categories, and specific, actionable recommendations for improving your financial position.

## Why Hermes
Budget analysis requires applying financial frameworks to personal data while producing recommendations that are realistic and specific rather than generic. Hermes applies the 50/30/20 rule and other frameworks accurately and identifies the highest-leverage changes based on the actual numbers provided.

## Quickstart
```bash
python examples/finance/budget_tools.py analyze --income 5000 --expenses "rent:1500,food:600,transport:200,subscriptions:150"
```

## Sample Input
```
Monthly income: $5,000 (after tax)
Expenses:
  Rent: $1,500
  Groceries: $400
  Dining out: $350
  Transport (car): $450
  Insurance: $200
  Subscriptions: $150
  Entertainment: $300
  Gym: $60
  Utilities: $120
  Clothing: $200
  Savings: $200
```

## Output Format
```
BUDGET ANALYSIS REPORT
Monthly Income: $5,000
Total Expenses Tracked: $3,930
Unaccounted: $1,070 (21.4% — see notes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

50/30/20 FRAMEWORK COMPARISON
Category      | Your Spending | 50/30/20 Target | Status
--------------|---------------|-----------------|--------
Needs (50%)   | $2,720 (54.4%)| $2,500          | Over by $220
Wants (30%)   | $1,010 (20.2%)| $1,500          | Under — good
Savings (20%) | $200 (4%)     | $1,000          | CRITICALLY LOW

CATEGORIZATION
Needs: Rent ($1,500), Groceries ($400), Transport ($450), Insurance ($200), Utilities ($120) = $2,670
Wants: Dining ($350), Subscriptions ($150), Entertainment ($300), Gym ($60), Clothing ($200) = $1,060
Savings/Debt: $200

PRIORITY ISSUES
1. SAVINGS (Critical): You are saving 4% of income vs. the recommended 20%. This is the most important area to address. Even moving to 10% ($500/mo) would represent a 150% improvement.

2. UNACCOUNTED $1,070: 21% of your income is untracked. This is likely going to miscellaneous spending, cash, or irregular expenses. Track this carefully for one month.

3. TRANSPORT: $450/month (9% of income) is high. If this is a car loan + insurance + fuel, consider whether the total cost of vehicle ownership is justified.

ACTIONABLE RECOMMENDATIONS
1. Automate $300/month savings transfer on payday — "pay yourself first" before discretionary spending.
2. Reduce dining out by 30% ($105 savings) by meal prepping 2-3 dinners per week.
3. Audit subscriptions — $150/month is substantial; review which are actively used (see subscription-audit tool).
4. Track the unaccounted $1,070 for 30 days using a spending app.

POSITIVE OBSERVATIONS
- Wants spending (20.2%) is well below the 30% guideline — you are not overspending on discretionary items.
- Utilities ($120) and gym ($60) are reasonable.
```

## Tips
- Include all recurring expenses, even small ones — subscriptions accumulate significantly.
- Run monthly for trend analysis; compare reports to identify creeping lifestyle inflation.
- The unaccounted gap is often the most revealing number — track it for one month.
- Combine with the subscription-audit tool for a complete picture of recurring charges.
