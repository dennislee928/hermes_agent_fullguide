# Personal Budget Advisor

## Description
Analyze your income and expense breakdown to identify savings opportunities, suggest a realistic budget framework, and provide actionable steps to reach specific financial goals. Advice is practical and non-judgmental.

## Why Hermes for This
Hermes can apply budgeting frameworks (50/30/20, zero-based, envelope method) to real numbers and reason about trade-offs — identifying which expenses to cut first based on your stated priorities rather than applying rigid rules.

## Quickstart
```bash
cd examples/daily-life
python habits_and_budget.py budget --income 4500 --expenses "rent:1400,food:600,transport:200,subscriptions:80,dining:300,misc:400"
python habits_and_budget.py budget --income 3000 --goal "save 500/month for emergency fund"
```

## Sample Prompt / Input
```
Monthly income (after tax): $4,500
Monthly expenses:
- Rent: $1,400
- Groceries: $400
- Dining out: $300
- Transport (car + gas): $350
- Subscriptions: $120
- Gym: $50
- Entertainment: $200
- Clothing: $150
- Miscellaneous: $200
Goal: Save $600/month for a house down payment.
```

## Expected Output Format
```
**Personal Budget Analysis**
Monthly income: $4,500 | Current spending: $3,170 | Current surplus: $1,330

---
**Current vs. 50/30/20 Framework**

| Category         | Your Spending | 50/30/20 Target | Status    |
|------------------|---------------|-----------------|-----------|
| Needs (50%)      | $2,200 (49%)  | $2,250          | On track  |
| Wants (30%)      | $770 (17%)    | $1,350          | Under ✓   |
| Savings (20%)    | $0 currently  | $900            | Gap ⚠     |

**Good news:** You already have a $1,330 surplus — you are spending below income.
The issue is it's likely not being directed intentionally.

---
**Reaching Your $600/Month Savings Goal**

You have $1,330 in surplus. To reliably save $600:

**Step 1 — Automate:** Set up an automatic transfer of $600 to a high-yield savings
account on payday. What you don't see, you won't spend.

**Step 2 — Subscription Audit ($120/month)**
Review each subscription this week:
- Streaming services: Are you using all of them? Likely $20-40 savings.
- Cancel anything unused → potential savings: $30-50/month.

**Step 3 — Dining Out ($300/month)**
This is your highest discretionary category. Reducing by 1-2 meals out per week
could save $60-100/month without feeling deprived.

**Projected savings with changes:**
$600 (automated) + ~$80 (subscriptions) + ~$80 (dining) = **~$760/month saved**

**Time to goal (assuming $20,000 down payment target): ~26 months**

---
**Quick Wins This Week**
1. Open a high-yield savings account (look for >4.5% APY)
2. Set up automatic $600 transfer for next payday
3. Spend 15 minutes reviewing and canceling unused subscriptions
```

## Tips
- Include all income sources (freelance, side jobs) for a complete picture.
- Mention specific financial goals (emergency fund, vacation, debt payoff) for targeted advice.
- Ask "what if" questions: "What if I cut dining in half?" to explore scenarios.
- This is general guidance, not financial advice — consult a certified financial planner for investment strategy.
