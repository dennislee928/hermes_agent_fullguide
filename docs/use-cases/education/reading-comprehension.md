# Reading Comprehension

## Description
Submit any text passage and receive comprehension questions, main idea summaries, vocabulary spotlights, inference challenges, and annotation guidance. Suitable for students practicing reading skills or teachers generating comprehension activities from any text.

## Why Hermes
Reading comprehension work requires understanding a text at multiple levels — literal, inferential, and evaluative. Hermes accurately identifies the main idea, makes reasonable inferences, and generates questions that target each comprehension level rather than just surface details.

## Quickstart
```bash
python examples/education/learning_assistant.py comprehension --file article.txt
```

## Sample Input
```
[Passage from a news article about ocean plastic pollution — 400 words]
```

## Output Format
```
READING COMPREHENSION ANALYSIS
Text: Ocean Plastic Pollution (400 words)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MAIN IDEA
The article argues that ocean plastic pollution has reached a critical threshold, threatening marine ecosystems and human food chains, and that individual action alone is insufficient without systemic policy change.

KEY DETAILS
- 8 million metric tons of plastic enter oceans annually
- Microplastics found in 73% of deep-sea fish sampled
- Current cleanup technologies address less than 1% of existing pollution

VOCABULARY SPOTLIGHT
- "pelagic" (line 4): relating to the open sea, away from coastlines
- "bioaccumulation" (line 12): the buildup of a substance in living tissue over time
- "anthropogenic" (line 19): caused or produced by human activity

COMPREHENSION QUESTIONS
Literal:
1. How many metric tons of plastic enter the ocean each year?
2. What percentage of deep-sea fish contained microplastics?

Inferential:
3. Why does the author suggest individual action is insufficient?
4. What does the phrase "systemic policy change" imply about the author's view of responsibility?

Evaluative:
5. Do you find the author's argument convincing? What evidence would strengthen or weaken it?
6. What counterarguments might someone who opposes plastic bans raise?

ANNOTATION SUGGESTIONS
- Underline the thesis statement (paragraph 1, last sentence)
- Circle transition words that signal cause-and-effect relationships
- Note where the author uses statistics versus expert opinion
```

## Tips
- Provide the text as a `.txt` file with `--file` for passages longer than a few paragraphs.
- Add `--level` (elementary, middle, high, college) to calibrate question complexity.
- Use `--focus inference` to generate only higher-order thinking questions.
- Teachers: run on any passage to quickly generate a full comprehension worksheet.
