# Interview Prep

## Description
Interview Prep generates role-specific practice questions, model answers using the STAR framework, and coaching notes to help candidates prepare thoroughly for any interview. It covers behavioral, technical, and situational question types calibrated to the seniority level.

## Why Hermes
Hermes generates questions that reflect real interview patterns for specific roles and levels, not generic lists. It also produces high-quality STAR-format sample answers that candidates can adapt, and identifies likely follow-up questions to help with deeper preparation.

## Quickstart
```bash
python examples/work-productivity/career_tools.py interview-prep \
  --role "Product Manager" \
  --level senior \
  --company "Google" \
  --focus behavioral
```

## Sample Input
```
Role: Staff Software Engineer
Level: Staff (L6 equivalent)
Company: Airbnb
Focus: System design + behavioral
My background: 8 years backend, distributed systems, led 2 platform migrations
```

## Expected Output Format
```
Interview Prep: Staff Software Engineer at Airbnb

BEHAVIORAL QUESTIONS (Leadership & Influence)

Q1: Tell me about a time you drove a major technical decision without formal authority.
Sample STAR Answer:
  Situation: Our team's service was hitting scaling limits at 50k RPS...
  Task: We needed to choose between two architectural approaches...
  Action: I organized a design review, created a comparison doc, and aligned 4 teams...
  Result: Adopted approach reduced latency 40% and has scaled to 300k RPS.
Likely follow-up: "What would you do differently?"

Q2: Describe a time you had to push back on a product decision...
[continues for 5-7 behavioral questions]

SYSTEM DESIGN QUESTIONS
Q1: Design Airbnb's search ranking system.
Key areas to cover: indexing strategy, ranking signals, personalization, A/B testing...

PREPARATION TIPS
- Airbnb values "belong anywhere" — frame team collaboration stories around inclusion.
- Staff-level bar expects scope of impact across multiple teams or products.
```

## Tips
- Include your background with `--background` so Hermes tailors sample answers to your experience.
- Use `--focus behavioral`, `--focus system-design`, or `--focus technical` for targeted prep.
- Add `--company` for culture-specific coaching notes (e.g., Amazon Leadership Principles).
- Run multiple times with different `--focus` values to cover all interview rounds.
