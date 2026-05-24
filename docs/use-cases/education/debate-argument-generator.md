# Debate Argument Generator

## Description
Generate structured debate arguments for any topic, either for a specific side or as a full pro/con analysis. Output includes a main claim, supporting sub-arguments with evidence types, potential rebuttals, and counterrebuttal strategies — giving debaters and essay writers a complete argumentative framework.

## Why Hermes
Constructing rigorous arguments requires logical structure, awareness of common fallacies, and the ability to anticipate counterarguments. Hermes produces multi-layered arguments that follow formal debate conventions (claim → warrant → evidence → rebuttal) rather than shallow lists of talking points.

## Quickstart
```bash
python examples/education/writing_and_research.py debate --topic "AI in education" --side for
```

## Sample Input
```
Topic: Universal Basic Income should be implemented nationwide
Side: For
Format: debate
```

## Output Format
```
DEBATE BRIEF: Universal Basic Income — FOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MAIN CLAIM
Universal Basic Income (UBI) should be implemented nationally because it addresses poverty more efficiently than current welfare systems, supports workers displaced by automation, and expands individual freedom.

ARGUMENT 1: Economic Efficiency
Warrant: Current means-tested welfare programs are expensive to administer and create poverty traps.
Evidence: Administrative costs consume 30-40% of some welfare programs (Cato Institute, 2012). UBI pilot programs in Finland (2017-2018) showed comparable poverty reduction at lower administrative cost.
Impact: Taxpayer funds are more efficiently deployed, reaching those in need without bureaucratic overhead.

ARGUMENT 2: Technological Displacement
Warrant: Automation will eliminate millions of jobs within the next decade, creating a structural unemployment crisis.
Evidence: McKinsey Global Institute (2017) estimated 400-800 million jobs globally at risk of automation by 2030. Current safety nets were designed for cyclical, not structural, unemployment.
Impact: Without income support, displaced workers face irreversible poverty, reducing consumer spending and economic stability.

ARGUMENT 3: Freedom and Dignity
Warrant: Unconditional income enables individuals to make education, caregiving, and entrepreneurship decisions without financial coercion.
Evidence: Stockton SEED pilot (2019-2021) showed recipients used funds primarily for necessities and education; employment actually increased among recipients.
Impact: UBI expands practical freedom, enabling individuals to pursue economically valuable activities that current incentives discourage.

ANTICIPATED REBUTTALS AND RESPONSES
Rebuttal: "UBI will cause inflation."
Response: Inflation occurs when money supply increases without corresponding production. UBI redistributes existing resources; targeted evidence from pilot programs shows minimal inflationary effects.

Rebuttal: "People will stop working."
Response: Evidence from 20+ pilot programs consistently shows minimal labor supply reduction; the Stockton SEED showed increased full-time employment.

CLOSING STRATEGY
Emphasize that pilots provide evidence, not just theory. Challenge opponents to engage with actual data rather than theoretical concerns.
```

## Tips
- Use `--side against` to generate the opposing brief for a complete debate prep package.
- Add `--format essay` to restructure the output as a written argumentative essay.
- Use `--evidence-types` to request statistical, anecdotal, or expert-testimony evidence specifically.
- Combine both sides to identify the strongest clash points before a competition.
