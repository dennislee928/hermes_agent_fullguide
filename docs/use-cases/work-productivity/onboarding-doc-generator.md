# Onboarding Doc Generator

## Description
Onboarding Doc Generator creates comprehensive, role-specific onboarding documentation from a brief description of the position, team, tools, and key processes. It produces a structured first-30-60-90-day guide that new hires can follow independently.

## Why Hermes
Hermes generates logically sequenced onboarding plans that follow realistic ramp patterns — starting with context and access, moving to observation and shadow work, then independent contribution. It adapts the structure to role type (engineering, sales, design, etc.) without being told every detail.

## Quickstart
```bash
python examples/work-productivity/meetings_and_docs.py onboarding \
  --role "Frontend Engineer" \
  --team "Product Engineering" \
  --tools "Jira, GitHub, Figma, Slack, Notion" \
  --process "2-week sprints, daily standup, weekly design review"
```

## Sample Input
```
Role: Customer Success Manager
Team: Customer Success (3 CSMs + 1 manager)
Tools: Salesforce, Intercom, Notion, Slack, Zoom
Customers: Mid-market SaaS (50-500 employee companies)
Key processes: weekly account reviews, QBRs, escalation protocol
Goals for new hire: own 15 accounts by month 3
```

## Expected Output Format
```
Onboarding Guide — Customer Success Manager

Week 1: Orientation & Context
  - Complete HR and system access checklist (IT will send)
  - Read: Company handbook, product one-pager, ICP definition doc
  - Shadow 3 customer calls (observe only)
  - Set up Salesforce, Intercom, Notion workspace
  - 1:1 with manager to align on 30-60-90 goals

Month 1 Goals: Listen & Learn
  [ ] Shadow all team members on at least one call each
  [ ] Complete Salesforce training module
  [ ] Understand escalation protocol and run one escalation with manager
  [ ] Memorize top 5 customer pain points and our responses

Month 2 Goals: Ramp Up
  [ ] Own 5 accounts with manager oversight
  [ ] Deliver first solo QBR
  [ ] Document one process improvement observation

Month 3 Goals: Full Ownership
  [ ] Own 15 accounts independently
  [ ] Hit first CSAT/NPS target
  [ ] Present learnings to team at monthly sync

Resources & Links:
  - [Notion: CSM Playbook]
  - [Salesforce: Account Tiers Guide]
  - [Escalation Protocol Doc]
```

## Tips
- Include `--goal` (e.g., "own 15 accounts by month 3") to ground the 90-day plan in measurable outcomes.
- Add `--company-stage startup` vs. `--company-stage enterprise` to calibrate formality and structure.
- Use `--format checklist` for a plain checklist format, or `--format narrative` for prose paragraphs.
- Have the new hire's future manager review and annotate before sending.
