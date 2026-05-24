# Exam Strategy Advisor

## Description
Receive a customized exam strategy covering time management during the test, optimal question-attack order, common pitfall avoidance, stress management techniques, and last-minute review priorities — all tailored to the specific exam type, subject, and time available.

## Why Hermes
Effective exam strategy is highly context-dependent: a strategy for a multiple-choice standardized test differs fundamentally from one for an open-book essay exam or a timed math test. Hermes adapts its recommendations to the specific exam format and subject, producing actionable rather than generic advice.

## Quickstart
```bash
python examples/education/study_tools.py exam-strategy --exam "AP Calculus AB" --time "3 hours" --format "multiple choice + free response"
```

## Sample Input
```
Exam: LSAT Logical Reasoning
Duration: 35 minutes per section
Question count: 25-26 per section
Format: Multiple choice
Weak areas: Assumption questions, Parallel Reasoning
```

## Output Format
```
EXAM STRATEGY: LSAT Logical Reasoning
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIME MANAGEMENT
- Target pace: 1 minute 20 seconds per question
- At the 17-minute mark, you should be on question ~13
- Flag and skip any question taking over 2 minutes — return at the end
- Reserve final 3 minutes for reviewing flagged questions

QUESTION-ATTACK ORDER
1. Answer "easy" question types first: Must Be True, Strengthen, Weaken
2. Save Assumption and Parallel Reasoning for later passes (your identified weak areas)
3. Never leave a question blank — there is no penalty for guessing

ASSUMPTION QUESTIONS — Your Weak Area
Strategy: Ask "What must be true for this argument to work?" before reading the answer choices. Eliminate any answer that goes beyond the argument's scope or is already stated.
Common trap: Answers that sound relevant but actually describe a strengthen or weaken rather than a necessary assumption.
Quick fix: Pre-phrase the assumption before looking at choices — this dramatically reduces trap selection.

PARALLEL REASONING — Your Weak Area
Strategy: Identify the logical structure (form) of the original argument first. Look for the answer with identical logical structure, ignoring content.
Quick fix: Assign variable labels (A→B, therefore C) to abstract the structure.

STRESS MANAGEMENT
- 3-breath reset: If you notice anxiety, take 3 slow breaths before continuing. This takes 15 seconds and resets focus.
- Reframe: A hard question likely means the curve is harder for everyone — it's not just you.

NIGHT BEFORE
- No new material after 8 PM
- Review your 3 most common error types only
- Sleep 7+ hours — more valuable than any cramming

MORNING OF
- Eat a moderate breakfast 2 hours before
- Arrive 20 minutes early to settle in
- Do 5-10 warm-up questions to prime logical thinking
```

## Tips
- Provide your specific weak areas for targeted tactical advice.
- Use `--format essay` for essay exam strategy, `--format oral` for oral examination coaching.
- Run two weeks before the exam for a strategic overview and again the night before for a condensed version.
- Combine with the study-plan-maker to align your preparation strategy with the exam strategy.
