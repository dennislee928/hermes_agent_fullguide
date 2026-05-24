# History Explainer

## Description
Receive clear, engaging explanations of historical events, periods, figures, and concepts. Hermes provides context, cause-and-effect chains, multiple perspectives, and connections to present-day implications, making history accessible and memorable rather than a list of dates.

## Why Hermes
Historical explanation requires synthesizing causes, actors, consequences, and interpretations — a task that benefits from Hermes's broad training on historical scholarship. It naturally structures responses with context before detail, mirroring good pedagogical practice.

## Quickstart
```bash
python examples/education/learning_assistant.py history "explain the causes of World War I"
```

## Sample Input
```
Topic: The fall of the Roman Empire
Audience: 10th-grade students
```

## Output Format
```
THE FALL OF THE WESTERN ROMAN EMPIRE (476 CE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONTEXT
At its height, Rome ruled over 50 million people across three continents. By 476 CE, the Western half had collapsed. Understanding why requires looking at overlapping problems that developed over centuries.

KEY CAUSES
1. Military Overextension — The empire's borders stretched thousands of miles, making defense extremely costly and eventually impossible without relying on barbarian mercenaries who held no loyalty to Rome.

2. Economic Decline — Heavy taxation, currency debasement (reducing silver content in coins), and disrupted trade routes caused inflation and poverty.

3. Political Instability — In the 3rd century alone, Rome had over 50 emperors. Constant civil wars drained resources and prevented coherent governance.

4. External Pressures — The Huns' migration from Central Asia pushed Germanic tribes (Visigoths, Vandals, Ostrogoths) into Roman territory, overwhelming border defenses.

5. The East/West Split (395 CE) — Dividing the empire weakened the west by removing eastern resources.

KEY DATE: 476 CE — Germanic chieftain Odoacer deposes the last Western emperor, Romulus Augustulus.

MODERN CONNECTIONS
Historians debate whether Rome truly "fell" or gradually transformed into medieval Europe. Many Roman institutions, laws, and the Latin language survived in the Eastern (Byzantine) Empire until 1453 CE.
```

## Tips
- Specify `--audience` (e.g., elementary, high-school, college) to calibrate vocabulary and depth.
- Ask for `--perspectives` to get multiple historical interpretations of a contested event.
- Use for comparative history: `"compare the fall of Rome with the fall of the Han Dynasty"`.
- Great for essay prep — ask for `"key arguments historians make about [event]"`.
