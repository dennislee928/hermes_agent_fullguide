# Finance Examples

Hermes-powered command-line tools for personal finance, budgeting, and financial education. All scripts connect to a local Ollama instance running the Hermes-3 model.

**DISCLAIMER: All output is for educational purposes only and does not constitute financial, investment, tax, or legal advice. Consult licensed professionals (CFP, CPA, attorney) for personalized guidance.**

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) running locally (`ollama serve`)
- The Hermes model pulled: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

## Installation

```bash
pip install -r requirements.txt
```

## Scripts

### budget_tools.py

Personal budget analyzer, subscription audit, emergency fund calculator, and side hustle tracker.

```bash
# Analyze your monthly budget against the 50/30/20 framework
python budget_tools.py analyze --income 5000 --expenses "rent:1500,food:600,transport:200,subscriptions:150"
python budget_tools.py analyze --income 5000 --file expenses.txt

# Audit your subscriptions
python budget_tools.py subscriptions --list "Netflix:15,Spotify:10,Gym:40,iCloud:3"
python budget_tools.py subscriptions --file subscriptions.txt

# Calculate your emergency fund target
python budget_tools.py emergency-fund --monthly-expenses 3200 --months 6
python budget_tools.py emergency-fund --monthly-expenses 3200 --employment freelancer --current-savings 4000 --monthly-savings 400

# Analyze side hustle profitability
python budget_tools.py side-hustle --income 800 --expenses "tools:50,platform:15,marketing:30" --hours 20
python budget_tools.py side-hustle --income 1200 --hours 25 --type "freelance design" --main-income 65000
```

### financial_advisor.py

Investment explainer, tax deduction finder, salary negotiation coach, loan comparison, credit card optimizer, and retirement planner.

```bash
# Learn about investment concepts
python financial_advisor.py invest "explain dollar-cost averaging vs lump sum investing"
python financial_advisor.py invest "what is an index fund and why do advisors recommend them" --level beginner

# Find potential tax deductions
python financial_advisor.py tax-deductions --situation "freelancer, home office, student loan, $800 charity donation"
python financial_advisor.py tax-deductions --file my_situation.txt --filing-status single

# Salary negotiation strategy
python financial_advisor.py negotiate --role "Software Engineer" --offer 95000 --target 110000 --location "San Francisco"
python financial_advisor.py negotiate --role "Marketing Manager" --offer 78000 --target 88000 --location "Chicago" --experience "7 years"

# Compare loan options
python financial_advisor.py loans --amount 25000 --term 60 --options "Bank A:6.5%,Credit Union:5.9%,Online Lender:7.1%"

# Optimize credit card rewards
python financial_advisor.py credit-cards --spending "groceries:600,dining:300,travel:200,gas:150,other:400" --cards "Chase Sapphire Preferred, Citi Double Cash"

# Retirement projection
python financial_advisor.py retirement --age 32 --savings 45000 --income 75000 --target-age 65
python financial_advisor.py retirement --age 35 --savings 45000 --income 80000 --target-age 65 --employer-match "4% of salary" --retirement-income 60000
```

## Input Files

You can provide longer inputs via text files using `--file`:

```
# expenses.txt
rent: 1500
groceries: 400
transport: 450
utilities: 120
gym: 60
subscriptions: 150
```

Use `--help` on any subcommand for the full option list:

```bash
python budget_tools.py analyze --help
python financial_advisor.py retirement --help
```
