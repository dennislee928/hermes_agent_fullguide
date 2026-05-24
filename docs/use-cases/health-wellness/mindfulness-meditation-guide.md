# Mindfulness Meditation Guide

## Description
Generate guided meditation scripts, breathing exercise instructions, and mindfulness practices customized for duration, experience level, and specific goals (stress relief, focus, sleep, anxiety, grief). Each script is ready to read aloud or follow along.

## Why Hermes
Meditation guides require a specific tone — calm, paced, and non-prescriptive — along with accurate knowledge of various meditation traditions and techniques (breath awareness, body scan, loving-kindness, visualization). Hermes produces scripts that are neither clinically cold nor pseudo-spiritual, striking a natural, accessible register.

## Quickstart
```bash
python examples/health-wellness/mindfulness_tools.py meditate --duration 10 --goal "reduce anxiety" --level beginner
```

## Sample Input
```
Duration: 5 minutes
Goal: Focus and concentration before work
Level: Intermediate
```

## Output Format
```
GUIDED MEDITATION: Focus & Concentration
Duration: 5 minutes | Level: Intermediate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Begin reading aloud slowly, pausing at each ellipsis for 2-3 seconds]

Find a comfortable seated position... Close your eyes or soften your gaze downward... Take one deep breath in through your nose... hold briefly... and release slowly through your mouth...

Bring your attention to the natural rhythm of your breath. You don't need to change it — simply notice it... the slight expansion of your chest or belly as you inhale... the gentle release as you exhale...

[ANCHOR TECHNIQUE — 2 minutes]
Choose one physical sensation as your anchor point for this session. It might be the feeling of air at the tip of your nose... the rise and fall of your chest... or the contact of your feet on the floor...

When your mind wanders — and it will — simply notice where it went, without judgment... and gently return your attention to your anchor... Each return is a successful repetition. You are building focus with every redirect...

[SHARPENING — 1.5 minutes]
Now narrow your attention further. If you were focusing on breath, zoom in to just the moment of the transition — the exact point where inhale becomes exhale... Hold that precise point in your awareness...

When distraction arises, name it briefly: "thinking"... "planning"... "memory"... then return...

[CLOSING — 30 seconds]
Begin to expand your awareness back to the whole room... Take one full, deliberate breath... Set a quiet intention for the work ahead: one word or phrase that represents your focus for today...

When you're ready, open your eyes.
```

## Tips
- Use `--duration 3` for a quick midday reset between tasks.
- Use `--goal sleep` for a body-scan meditation before bed.
- For anxiety: `--technique "4-7-8 breathing"` generates a breathing-focused script.
- Save your favorite scripts to `.txt` files for offline use.
