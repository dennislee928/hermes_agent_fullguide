# Credit Card Optimizer

## Description
Analyze your spending patterns and current credit cards to identify the optimal card combination for maximizing rewards, minimizing fees, and improving credit utilization. Provides a spending strategy that assigns the right card to each purchase category.

## Why Hermes
Credit card optimization requires cross-referencing reward structures, spending patterns, and annual fee break-even analysis. Hermes applies these calculations systematically and produces a card-to-category assignment strategy that is actually actionable rather than generic "use a rewards card" advice.

## Quickstart
```bash
python examples/finance/financial_advisor.py credit-cards --spending "groceries:600,dining:300,travel:200,gas:150,other:400" --cards "Chase Sapphire Preferred, Citi Double Cash"
```

## Sample Input
```
Monthly spending:
  Groceries: $600
  Dining: $300
  Travel: $200
  Gas: $150
  Amazon: $200
  Other: $400

Current cards:
  Chase Sapphire Preferred (annual fee: $95)
  Citi Double Cash (no annual fee)
  Amazon Visa (no annual fee)
```

## Output Format
```
CREDIT CARD OPTIMIZATION STRATEGY
Monthly Spend: $1,850 | Annual: $22,200
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPTIMIZED CARD ASSIGNMENT

| Category    | Monthly | Best Card              | Rate  | Monthly Rewards |
|-------------|---------|------------------------|-------|-----------------|
| Groceries   | $600    | Chase Sapphire Pref.   | 3x pts| $9.00 (3% equiv)|
| Dining      | $300    | Chase Sapphire Pref.   | 3x pts| $4.50           |
| Travel      | $200    | Chase Sapphire Pref.   | 2x pts| $2.00           |
| Gas         | $150    | Citi Double Cash       | 2%    | $3.00           |
| Amazon      | $200    | Amazon Visa            | 5%    | $10.00          |
| Other       | $400    | Citi Double Cash       | 2%    | $8.00           |
| TOTAL       | $1,850  |                        |       | $36.50/mo       |

ANNUAL REWARDS VALUE: $438 (before annual fees)
Annual fees: $95 (Chase Sapphire Preferred)
NET ANNUAL REWARDS: $343

CURRENT SUBOPTIMAL ASSIGNMENT (if using one card)
If using only Citi Double Cash (2% flat) for everything: $22,200 × 2% = $444/year
Your optimized strategy: $438 + Amazon 5% premium
Net improvement from optimization: Roughly equivalent — but see travel redemption value below.

IMPORTANT: CHASE POINTS REDEMPTION VALUE
Chase Ultimate Rewards points are worth 1.25-2.1 cents each when redeemed for travel via Chase portal or transferred to airline/hotel partners (not the 1 cent assumed above). At 1.5 cents/point: Monthly dining + travel + grocery rewards = ~$24/mo, not $15.50.

ANNUAL FEE BREAK-EVEN ANALYSIS
Chase Sapphire Preferred ($95/year):
Required spending to break even vs. Citi Double Cash (2% flat): ~$3,800/year in bonus categories
Your dining + groceries alone: $10,800/year
Verdict: The Chase card is comfortably justified.

CREDIT SCORE NOTE
- Total credit utilization across all cards: keep below 30% for good score, below 10% for excellent.
- At $1,850/month spend, you need at least $6,167 in total credit limits for <30% utilization.
- Never close old cards — length of credit history affects your score.

POSSIBLE IMPROVEMENTS
Missing card opportunity: None of your cards offers 4-6% on groceries. The Blue Cash Preferred (Amex, $95 annual fee) offers 6% on groceries up to $6,000/year — worth considering given your $7,200/year grocery spend.
```

## Tips
- Run this analysis annually — reward structures change and new cards emerge.
- Use the card assigned to each category consistently; mixing defeats the optimization.
- Never carry a balance on a rewards card — interest charges eliminate all rewards value and then some.
- Consider adding one no-fee card as your "other" catch-all so your rewards card never sits on low-value purchases.
