# Language Tutor

## Description
Practice a foreign language through translation, grammar explanation, vocabulary drilling, and conversational coaching. Hermes can explain why a translation is structured a certain way, highlight common learner mistakes, and adjust the explanation depth to match the learner's proficiency level.

## Why Hermes
Language tutoring demands both accurate translation and clear metalinguistic explanation — telling the learner not just what the correct form is but why. Hermes-3's instruction-following ability ensures it maintains the tutor persona, switches languages cleanly, and provides grammatical reasoning rather than bare translations.

## Quickstart
```bash
python examples/education/learning_assistant.py translate --text "Hello world" --to Spanish --explain
```

## Sample Input
```
Text: "I have been waiting for you for three hours."
Target language: French
Explain: true
```

## Output Format
```
TRANSLATION: French
Original:    "I have been waiting for you for three hours."
Translation: "Je t'attends depuis trois heures."

GRAMMAR NOTES
- French uses the present tense ("attends") where English uses the present perfect continuous ("have been waiting") when the action is still ongoing. This is a key structural difference.
- "Depuis" expresses duration from a point in the past to now — equivalent to "for" or "since" in this context.
- "Te" contracts to "t'" before a vowel (elision).

COMMON MISTAKES TO AVOID
✗ "J'ai attendu pour toi pendant trois heures" — Uses passé composé (completed action) rather than present tense; "pour toi" is unnatural here.
✓ "Je t'attends depuis trois heures." — Correct form.

PRONUNCIATION TIP
"depuis" = duh-PWEE; the final 's' is silent.
```

## Tips
- Use `--from` to specify the source language when dealing with ambiguous short phrases.
- Add `--level beginner` to get simpler grammatical explanations suitable for learners just starting out.
- Ask Hermes to generate 5 practice sentences using the same grammar structure with `--practice 5`.
- Use for vocabulary context: `"translate 'serendipity' to Japanese and explain cultural nuance"`.
