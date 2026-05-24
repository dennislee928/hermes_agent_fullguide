# Flashcard Generator

## Description
Automatically generate study flashcards from any topic, passage, or set of notes. Hermes produces question-and-answer pairs formatted for spaced repetition, covering key concepts, definitions, dates, and relationships found within the source material.

## Why Hermes
Hermes-3 follows structured output instructions with high fidelity, which is critical for flashcard generation where consistent Q&A formatting is required. Its broad knowledge base means it can generate accurate cards across subjects ranging from organic chemistry to world history without factual drift.

## Quickstart
```bash
python examples/education/study_tools.py flashcards --topic "French Revolution" --count 20
```

## Sample Input
```
Topic: Mitosis
Count: 10
```

## Output Format
```
FLASHCARD 1
Q: What are the four stages of mitosis?
A: Prophase, Metaphase, Anaphase, Telophase

FLASHCARD 2
Q: What happens during prophase?
A: Chromosomes condense and become visible; the mitotic spindle begins to form and the nuclear envelope breaks down.

...
```

## Tips
- Provide a passage of text with `--text` to generate cards grounded in a specific source rather than general knowledge.
- Use `--difficulty hard` to push Hermes toward nuanced, application-level questions rather than pure recall.
- Pipe the output to a `.csv` file and import directly into Anki using the "Question/Answer" note type.
- Add `--count 50` for comprehensive deck coverage before a major exam.
