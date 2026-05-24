# Investment Explainer

## Description
Receive clear, jargon-free explanations of investment concepts, vehicles, strategies, and terminology. Covers stocks, bonds, ETFs, index funds, mutual funds, real estate, options, and alternative investments — explaining mechanics, risk profiles, tax implications, and how each fits into a broader portfolio strategy.

## Why Hermes
Investment education requires accurate explanations of complex financial mechanisms without oversimplification or hype. Hermes explains both the mechanics and the risk factors of investment vehicles clearly, always noting that this is educational content rather than personalized financial advice.

## Quickstart
```bash
python examples/finance/financial_advisor.py invest "explain dollar-cost averaging vs lump sum investing"
```

## Sample Input
```
Topic: What is an index fund and why do most financial advisors recommend them?
Level: Beginner
```

## Output Format
```
INVESTMENT EXPLAINER: Index Funds
Level: Beginner
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WHAT IS AN INDEX FUND?
An index fund is a type of investment that automatically buys a small piece of every company in a specific market index (like the S&P 500, which tracks the 500 largest US companies). Instead of trying to pick winning stocks, you own a tiny slice of hundreds or thousands of companies at once.

HOW IT WORKS
When you invest $1,000 in an S&P 500 index fund, that $1,000 is spread across all 500 companies in proportion to their size. Apple might get $70, Microsoft $65, and so on down to small allocations for smaller companies.

WHY ADVISORS RECOMMEND THEM

1. Low Cost: Index funds charge minimal fees (0.03%-0.10%/year) because no one is actively picking stocks. Actively managed funds typically charge 0.5%-1.5%. On a $100,000 investment over 30 years, this difference can amount to $50,000+.

2. Consistent Performance: Decades of data show that most actively managed funds fail to beat their benchmark index over 10+ year periods. If professionals can't reliably beat the index, it's rational to simply buy the index.

3. Instant Diversification: Owning 500 companies means one company's failure barely affects your portfolio. Owning 5 stocks means one failure is devastating.

4. Simplicity: No decisions required beyond "invest regularly." This removes emotional decision-making (buying high out of excitement, selling low out of fear).

REAL NUMBERS
The S&P 500 has returned an average of ~10.5% annually before inflation (7-8% inflation-adjusted) over the past 50 years. $10,000 invested in 1973 with dividends reinvested grew to approximately $800,000 by 2023.

RISKS TO UNDERSTAND
- Index funds fall when the entire market falls — in 2008, the S&P 500 dropped 37%. They recovered, but it took 4+ years.
- They do not protect you from market crashes; they participate in them fully.
- International diversification reduces dependence on a single country's economy.

GETTING STARTED
Vanguard (VTSAX, VOO), Fidelity (FZROX — zero fee), and Schwab (SWTSX) offer widely recommended index funds. Invest through a tax-advantaged account (401k, IRA) when possible.

DISCLAIMER: This is educational information only. Consult a licensed financial advisor before making investment decisions.
```

## Tips
- Use for learning before meeting with a financial advisor — arrive informed.
- Ask for comparisons: `"index funds vs ETFs — what's the actual difference?"`.
- Request risk explanations: `"what are the risks of bonds in a rising interest rate environment?"`.
- Great for understanding employer benefits: `"explain the difference between traditional and Roth 401k"`.
