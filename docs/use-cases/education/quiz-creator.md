# Quiz Creator

## Description
Generate complete multiple-choice, true/false, or short-answer quizzes on any academic topic. Each question includes a correct answer and, for multiple-choice items, three plausible distractors with explanations of why each wrong answer is incorrect.

## Why Hermes
Hermes excels at constructing distractors that are plausible but clearly wrong upon reflection — the hallmark of a well-designed quiz. Its instruction-following capability ensures consistent formatting so quizzes can be parsed and rendered in any quiz platform.

## Quickstart
```bash
python examples/education/study_tools.py quiz --topic "Python basics" --count 10 --difficulty medium
```

## Sample Input
```
Topic: World War II causes
Count: 5
Difficulty: hard
Format: multiple-choice
```

## Output Format
```
QUESTION 1 (Multiple Choice)
The policy of allowing Hitler to expand German territory in exchange for peace was known as:
A) Containment
B) Appeasement  [CORRECT]
C) Détente
D) Isolationism

Explanation: Appeasement refers specifically to the pre-WWII strategy used by Britain and France, most notably at the Munich Agreement (1938). Containment was a Cold War strategy; Détente was 1970s US-Soviet policy; Isolationism was a US domestic stance.

QUESTION 2 ...
```

## Tips
- Combine with `--format true-false` for quick warm-up assessments.
- Use `--difficulty easy` for introductory review and `--difficulty hard` to prepare for challenging exams.
- Teachers can generate multiple quiz variants by running the command several times on the same topic.
- Export to JSON for integration with quiz platforms like Google Forms or Kahoot.
