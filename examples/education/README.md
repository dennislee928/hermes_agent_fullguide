# Education Examples

Hermes-powered command-line tools for studying, writing, and research. All scripts connect to a local Ollama instance running the Hermes-3 model.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) running locally (`ollama serve`)
- The Hermes model pulled: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

## Installation

```bash
pip install -r requirements.txt
```

## Scripts

### study_tools.py

Flashcard generator, quiz creator, study plan maker, and exam strategy advisor.

```bash
# Generate 20 flashcards on the French Revolution
python study_tools.py flashcards --topic "French Revolution" --count 20

# Create a 10-question medium-difficulty quiz
python study_tools.py quiz --topic "Python basics" --count 10 --difficulty medium

# Build a study plan for Calculus
python study_tools.py study-plan --subject "Calculus" --exam-date "2024-03-15" --hours-per-day 2

# Get a tailored exam strategy
python study_tools.py exam-strategy --exam "AP Calculus AB" --time "3 hours" --format "multiple choice + free response"
```

### writing_and_research.py

Essay feedback, research paper summarizer, citation formatter, and debate argument generator.

```bash
# Get feedback on an essay (provide a .txt file)
python writing_and_research.py essay-feedback --file essay.txt

# Summarize a research paper
python writing_and_research.py summarize --file paper.txt --audience general

# Format a citation in APA
python writing_and_research.py cite --style APA --source "Author: Chen J, Title: Sleep and Memory, Journal: Nature Neuroscience, Year: 2023, Volume: 26, Pages: 112-119"

# Generate a debate brief
python writing_and_research.py debate --topic "AI in education" --side for
```

### learning_assistant.py

Language tutor, math solver, science explainer, history explainer, vocabulary builder, reading comprehension, and concept map creator.

```bash
# Translate with grammar explanation
python learning_assistant.py translate --text "Hello world" --to Spanish --explain

# Solve a math problem step by step
python learning_assistant.py math "integral of x^2 from 0 to 3"

# Explain a science concept
python learning_assistant.py science "explain CRISPR gene editing for a 15-year-old"

# Explain a historical event
python learning_assistant.py history "explain the causes of World War I"

# Deep vocabulary analysis
python learning_assistant.py vocab --word "ephemeral" --examples 5

# Generate reading comprehension questions
python learning_assistant.py comprehension --file article.txt

# Create a concept map
python learning_assistant.py concept-map --topic "Photosynthesis" --depth 3
```

## Common Options

All scripts support `--file` to read input from a text file instead of inline arguments. Use `--help` on any subcommand for the full option list:

```bash
python study_tools.py flashcards --help
python writing_and_research.py essay-feedback --help
python learning_assistant.py translate --help
```
