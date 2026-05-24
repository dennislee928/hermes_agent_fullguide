# Work & Productivity Examples

Runnable Python scripts that use Hermes (via Ollama) to automate 20 common workplace tasks across communication, documentation, career development, project management, and business operations.

## Prerequisites

**Ollama running locally with the Hermes model:**
```bash
ollama serve
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

**Python dependencies:**
```bash
pip install -r requirements.txt
```

## Scripts

### email_and_comms.py
Email drafting and tone checking.

```bash
# Draft a professional email
python email_and_comms.py draft \
  --to "client" \
  --subject "project update" \
  --tone professional \
  --context "Milestone 2 complete, on track for delivery next Friday."

# Draft with additional options
python email_and_comms.py draft \
  --to "manager" \
  --subject "requesting PTO" \
  --tone friendly \
  --context "Need next Friday afternoon for a medical appointment." \
  --length short \
  --sender "Alex"

# Check tone of an existing email (from file)
python email_and_comms.py tone-check --file my_email.txt --intended-tone "firm but collaborative"

# Check tone of inline text
python email_and_comms.py tone-check \
  --text "Per my last email, this was clearly stated. Please advise." \
  --intended-tone professional
```

**Available tones:** `professional`, `formal`, `friendly`, `assertive`, `empathetic`, `concise`

---

### meetings_and_docs.py
Meeting agendas, note summarization, business reports, SOPs, and onboarding guides.

```bash
# Generate a meeting agenda
python meetings_and_docs.py agenda \
  --title "Q3 Sprint Kickoff" \
  --duration 60 \
  --attendees "PM, Engineering Lead, Designer, QA Lead" \
  --topics "sprint goals, backlog grooming, design review, blockers" \
  --goal "Align team on sprint priorities"

# Summarize meeting notes from a file
python meetings_and_docs.py summarize --file meeting_notes.txt

# Summarize piped input
cat transcript.txt | python meetings_and_docs.py summarize

# Write a business report
python meetings_and_docs.py report \
  --title "Q2 Marketing Performance" \
  --audience executive \
  --data "Traffic up 7%, conversion down 0.4pp, email open rate 31%, paid ROI 3.1x"

# Write an SOP
python meetings_and_docs.py sop \
  --process "Monthly financial close" \
  --department "Finance" \
  --tools "QuickBooks, Google Sheets, Slack" \
  --roles "Accountant, Finance Manager, CFO"

# Generate an onboarding guide
python meetings_and_docs.py onboarding \
  --role "Customer Success Manager" \
  --team "Customer Success" \
  --tools "Salesforce, Intercom, Notion, Slack" \
  --goal "Own 15 accounts independently by month 3"
```

---

### career_tools.py
Cover letters, resume reviews, interview prep, and performance reviews.

```bash
# Write a cover letter (with resume and JD files)
python career_tools.py cover-letter \
  --role "Software Engineer" \
  --company "Acme Corp" \
  --resume resume.txt \
  --jd job_description.txt

# Cover letter without files (Hermes writes generically for the role)
python career_tools.py cover-letter \
  --role "Senior Product Manager" \
  --company "Stripe" \
  --highlights "5 years fintech PM, launched 3 payment products"

# Review a resume
python career_tools.py review-resume \
  --resume resume.txt \
  --role "Data Scientist" \
  --level mid

# Resume review with job description for ATS gap analysis
python career_tools.py review-resume \
  --resume resume.txt \
  --role "Backend Engineer" \
  --level senior \
  --jd job_description.txt

# Interview prep (behavioral focus)
python career_tools.py interview-prep \
  --role "Product Manager" \
  --level senior \
  --focus behavioral \
  --company "Google"

# Interview prep (system design)
python career_tools.py interview-prep \
  --role "Staff Software Engineer" \
  --level staff \
  --focus system-design \
  --background "8 years backend, distributed systems"

# Write a performance review (manager POV)
python career_tools.py perf-review \
  --role "Senior Engineer" \
  --rating "exceeds expectations" \
  --notes "Delivered auth rewrite, mentored 2 juniors, strong code quality"

# Self-review (employee POV)
python career_tools.py perf-review \
  --role "Designer" \
  --rating "meets expectations" \
  --pov employee \
  --notes "Shipped all projects on time, led rebrand project"
```

**Rating options:** `exceeds expectations`, `meets expectations`, `needs improvement`
**Level options:** `entry`, `mid`, `senior`, `staff`, `executive`

---

### project_management.py
Task prioritization, project timelines, OKRs, retrospectives, and presentation outlines.

```bash
# Prioritize a task list (Eisenhower Matrix)
python project_management.py prioritize \
  --tasks "Fix auth bug, Write quarterly report, Review PRs, Update docs, Respond to client"

# Prioritize from a file (one task per line)
python project_management.py prioritize --file tasks.txt

# MoSCoW prioritization
python project_management.py prioritize \
  --tasks "User auth, Payment integration, Email notifications, Dark mode" \
  --framework moscow

# Generate a project timeline
python project_management.py timeline \
  --project "Build customer feedback portal" \
  --team "2 engineers, 1 designer, 1 PM" \
  --deadline "10 weeks" \
  --deliverables "user research, prototype, MVP, launch" \
  --buffer 15

# Generate OKRs
python project_management.py okr \
  --team "Engineering" \
  --quarter Q3 \
  --themes "reliability, developer velocity, platform foundation" \
  --company-goal "Reduce time-to-deploy by 50%"

# Retrospective
python project_management.py retro \
  --sprint "Sprint 24" \
  --went-well "shipped feature on time, strong code reviews" \
  --improve "deploy failed twice, standup runs too long" \
  --format action-plan

# Presentation outline
python project_management.py outline \
  --topic "Product Roadmap H2 2024" \
  --audience "C-suite and Board" \
  --slides 12 \
  --goal "Secure alignment on roadmap priorities" \
  --format pitch
```

---

### business_tools.py
Contract summarization, invoice generation, expense categorization, and business idea validation.

```bash
# Summarize a contract
python business_tools.py summarize-contract --file contract.txt

# Focus on specific clauses
python business_tools.py summarize-contract \
  --file vendor_agreement.txt \
  --focus "payment terms, data rights, termination, liability"

# Generate an invoice
python business_tools.py invoice \
  --client "BuildRight Inc." \
  --items "Brand identity:1:$2500,Logo variations:1:$500,Brand guidelines:1:$800" \
  --due-days 15 \
  --invoice-num "INV-2024-047" \
  --sender "Jane Smith Design Studio"

# Invoice with tax
python business_tools.py invoice \
  --client "Acme Corp" \
  --items "Consulting:40hrs:$200,Training workshop:1:$1500" \
  --due-days 30 \
  --tax 8.5

# Categorize expenses
python business_tools.py categorize-expenses --file expenses.txt

# With custom categories
python business_tools.py categorize-expenses \
  --file october_expenses.txt \
  --categories "Travel,Software/SaaS,Cloud Infrastructure,Meals,Marketing,Office Supplies"

# Validate a business idea
python business_tools.py validate-idea \
  --idea "A platform where restaurants rent empty tables to remote workers for $10/day" \
  --market B2C \
  --stage "idea stage" \
  --founder-background "5 years restaurant operations"

# Devil's advocate mode (more critical analysis)
python business_tools.py validate-idea \
  --idea "An AI-powered recipe app for home cooks" \
  --market B2C \
  --devil-advocate
```

---

## Tips

- All scripts stream output in real-time — output appears as Hermes generates it.
- Use `--help` on any script or subcommand for full option documentation:
  ```bash
  python career_tools.py --help
  python career_tools.py cover-letter --help
  ```
- Provide more context for better results. The richer your input, the more specific the output.
- Most scripts accept `--file` arguments to read input from files rather than inline text.
- For meeting summarization, pipe transcripts directly: `cat notes.txt | python meetings_and_docs.py summarize`

## Troubleshooting

**"Cannot connect to Ollama"**: Run `ollama serve` in a separate terminal.

**Model not found**: Pull the model with `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

**Slow responses**: The 8B model runs on CPU if no GPU is available. First response may take 30-60 seconds to warm up.
