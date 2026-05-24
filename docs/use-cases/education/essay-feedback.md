# Essay Feedback

## Description
Submit any essay draft and receive structured, actionable feedback covering thesis strength, argument coherence, evidence quality, paragraph structure, tone, grammar patterns, and suggestions for improvement. The feedback mimics a thoughtful instructor's marginal notes and summary comments.

## Why Hermes
Hermes-3 is trained on a broad corpus of academic writing norms and can distinguish between stylistic preferences and genuine structural weaknesses. Unlike simple grammar checkers, it evaluates the logical flow of arguments and the quality of supporting evidence.

## Quickstart
```bash
python examples/education/writing_and_research.py essay-feedback --file essay.txt
```

## Sample Input
```
[Contents of essay.txt — a 500-word argumentative essay on climate policy]
```

## Output Format
```
ESSAY FEEDBACK REPORT
━━━━━━━━━━━━━━━━━━━━
Overall Grade Estimate: B+ (88/100)

THESIS (Score: 8/10)
Your thesis clearly states a position, but it lacks a "because" clause that signals your main line of argument. Suggested revision: "...because [reason 1] and [reason 2]."

ARGUMENT STRUCTURE (Score: 7/10)
Paragraph 3 introduces a new claim not previewed in the introduction. Consider either adding it to your thesis roadmap or moving it to an existing paragraph that addresses a related point.

EVIDENCE (Score: 9/10)
Strong use of statistics in paragraph 2. Paragraph 4 makes a sweeping claim without citation — add a source or hedge the language.

GRAMMAR & STYLE
- Overuse of passive voice (7 instances). Prefer active constructions.
- Comma splice in paragraph 1, sentence 3.
- Word variety: "significant" used 5 times — try "substantial," "considerable," "notable."

SUGGESTIONS FOR REVISION
1. Strengthen the thesis with a reason clause.
2. Add a topic sentence to paragraph 3.
3. Cite the statistic on page 2 or soften with "according to some researchers."
```

## Tips
- Provide the essay as a `.txt` file for best results with `--file`.
- Add `--level college` or `--level highschool` to calibrate feedback expectations.
- Use `--focus structure` to limit feedback to organization only — useful for targeted revision passes.
- Run multiple passes: one for structure, one for language, one for argument — each using the relevant `--focus` flag.
