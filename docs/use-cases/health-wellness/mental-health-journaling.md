# Mental Health Journaling

## Description
Receive guided journaling prompts, cognitive reframing suggestions, and structured reflection exercises tailored to your current emotional state. Hermes acts as a supportive, non-judgmental journaling coach — not a therapist — helping you process thoughts and emotions through evidence-informed writing exercises.

## Why Hermes
Effective journaling prompts require matching the prompt to the emotional state — prompts for grief differ from those for anxiety or low motivation. Hermes identifies the emotional register from context and generates prompts that are compassionate, specific, and grounded in established journaling practices (CBT, gratitude research, narrative therapy).

## Quickstart
```bash
python examples/health-wellness/mindfulness_tools.py journal --mood "anxious about upcoming job interview"
```

## Sample Input
```
Current state: Feeling overwhelmed and burned out after a difficult week at work
Goal: Process feelings and find some calm
```

## Output Format
```
GUIDED JOURNALING SESSION: Processing Overwhelm
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Take a few slow breaths before you begin. There are no right or wrong answers here.

GROUNDING PROMPT (5 minutes)
Describe exactly what "overwhelmed" feels like in your body right now. Where do you feel it? What does it feel like physically — tightness, heaviness, buzzing? Simply noticing without judgment is the first step.

EXPLORATION PROMPT (10 minutes)
What specific moments from this week feel like the heaviest? List 2-3 specific situations, not general feelings. For each one: what happened, what did you tell yourself about it, and what did that story cost you emotionally?

REFRAME PROMPT (10 minutes)
For the heaviest situation you wrote about: What would you tell a close friend who experienced the exact same thing? Write that response. Notice if the compassion you offer your friend differs from what you offered yourself.

PERSPECTIVE PROMPT (5 minutes)
What is one small thing from this week that went right, even slightly? It doesn't need to be significant. Write about why it matters.

CLOSING REFLECTION (5 minutes)
What is one thing — just one — you can release about this week? Write it down, and then write: "I'm setting this down for now."

AFTER YOUR SESSION
Notice any shift in how you feel compared to before you began. Journaling effects are often subtle but cumulative. Consider sharing recurring themes with a mental health professional if the overwhelm persists.

IMPORTANT: This is a journaling aid, not therapy. If you are experiencing persistent distress, please reach out to a mental health professional or crisis line.
```

## Tips
- Use `--mood` to describe your current emotional state for tailored prompts.
- Morning journaling (10 min) pairs well with `--goal "set intentions for the day"`.
- Evening journaling works well with `--goal "process the day and decompress"`.
- For deeper work, consider sharing patterns from your journal with a licensed therapist.
