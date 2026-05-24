# Tax Deduction Finder

## Description
Describe your employment situation, life circumstances, and major expenses to receive a checklist of commonly overlooked tax deductions and credits you may be eligible for. Output includes the deduction type, eligibility criteria, estimated value, and documentation needed.

## Why Hermes
Tax law contains hundreds of deductions most people never claim because they don't know they exist. Hermes systematically reviews your situation against common deduction categories and surfaces relevant ones — always noting that a licensed tax professional should verify eligibility for your specific situation.

## Quickstart
```bash
python examples/finance/financial_advisor.py tax-deductions --situation "freelancer, home office, student loan, donated $500 to charity"
```

## Sample Input
```
Filing status: Single
Employment: Full-time employee + freelance side income (~$15,000)
Home: Renter, uses one room exclusively as home office for freelance work
Other: Student loan interest payments ($1,200/year), donated $800 to charity, contributed $3,000 to traditional IRA, bought a new laptop for freelance work ($1,200)
```

## Output Format
```
TAX DEDUCTION FINDER
Profile: Single | Employee + Freelancer | [Tax Year]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEDUCTIONS LIKELY APPLICABLE TO YOUR SITUATION

1. HOME OFFICE DEDUCTION (Schedule C)
Eligibility: You use a room exclusively and regularly for freelance work.
Method A (Simplified): $5 per square foot, up to 300 sq ft = up to $1,500 deduction
Method B (Actual): Percentage of home expenses (rent, utilities, internet) equal to office sq footage / total sq footage
Recommendation: Calculate both and use the larger. For most renters, the actual method is larger.
Documentation needed: Sketch or measurement of office space; utility bills

2. BUSINESS EQUIPMENT DEDUCTION (Section 179, Schedule C)
Your laptop ($1,200): Fully deductible in the year of purchase as a business expense if used predominantly for freelance work.
Note: If used partially for personal use, only the business-use percentage is deductible.
Documentation: Receipt, record of business use percentage

3. STUDENT LOAN INTEREST DEDUCTION (Form 1040, Line 21)
Amount: Up to $2,500 of student loan interest paid is deductible (above-the-line — no need to itemize).
Your situation: You paid $1,200, so the full $1,200 is potentially deductible.
Income phase-out: Begins at $75,000 MAGI (single) for 2023; verify your income is below this threshold.
Documentation: Form 1098-E from your loan servicer

4. CHARITABLE CONTRIBUTION DEDUCTION
Your donation: $800 cash donation
Note: This requires itemizing deductions (Schedule A). Compare your total itemized deductions to the standard deduction ($13,850 for single filers, 2023). Unless you have significant other itemized deductions, the standard deduction may be larger.
Documentation: Acknowledgment letter from charity if donation > $250

5. TRADITIONAL IRA DEDUCTION
Your contribution: $3,000
As an employee with workplace retirement plan access, deductibility phases out between $73,000-$83,000 MAGI (single, 2023). If your income is below $73,000, the full $3,000 may be deductible.
Documentation: IRA contribution confirmation from institution

6. SELF-EMPLOYMENT TAX DEDUCTION (Schedule 1)
As a freelancer, you pay both employer and employee portions of Social Security/Medicare (15.3%). You can deduct half (7.65%) of this amount. On $15,000 income: approximately $1,147 deduction.
This is automatic — calculated on Schedule SE.

7. SELF-EMPLOYED HEALTH INSURANCE
If you paid for your own health insurance at any point while freelancing and were not eligible for employer coverage, premiums may be deductible.

ESTIMATED TOTAL ABOVE-THE-LINE DEDUCTIONS (not requiring itemizing)
Student loan interest: $1,200
IRA contribution: $3,000
SE tax deduction: ~$1,147
SE health insurance: varies
Home office + equipment (reduce Schedule C income): up to $2,700+

DISCLAIMER: This is for educational purposes only. Tax laws change annually and individual eligibility depends on specific circumstances. Consult a licensed CPA or tax attorney before filing.
```

## Tips
- Provide as much detail about your situation as possible for the most comprehensive list.
- Always verify with a CPA or tax professional — this is a starting checklist, not tax advice.
- Run this before meeting your tax professional so you arrive with a complete picture of your situation.
- Many freelancers significantly underclaim business deductions — the home office and equipment deductions are frequently missed.
