# Poem Generator

## Description
Generate original poems in any form — sonnets, haiku, villanelles, free verse, odes, elegies, epics — for any occasion, subject, or emotional register. Hermes attends to meter, line breaks, imagery, and the sonic texture of language, producing poems that hold up to reading aloud.

## Why Hermes
Poetry generation is one of the hardest tasks for language models because it requires simultaneous attention to meaning, sound, rhythm, and surprise — the moment when a line exceeds what the reader expected. Hermes-3 produces work with genuine image-making and avoids the sentimental abstraction that plagues most AI-generated verse.

## Quickstart
```bash
python examples/creative/creative_tools.py poem --type sonnet --occasion birthday --for "my grandmother"
```

## Sample Input
```
Form: Villanelle
Subject: Insomnia
Tone: Quietly desperate, with dark humor
```

## Output Format
```
THE HOURS KEEP THEIR OWN ACCOUNTS
A Villanelle

The ceiling and I have spent years getting to know each other.
3 AM does not ask whether I'm ready.
I've made my peace with being someone's insomniac brother.

The fan performs its white-noise labor,
the dark outside is calm and steady —
the ceiling and I have spent years getting to know each other.

My body archives every small disorder:
the coffee, the news, the thoughts not yet ready.
I've made my peace with being someone's insomniac brother,

the one who texts too late, who calls December
to ask if winter has a cure for Wednesdays.
The ceiling and I have spent years getting to know each other.

Perhaps the point is not the sleep but to remember
what silence sounds like when it isn't empty.
I've made my peace with being someone's insomniac brother.

Morning will come in, businesslike and tender,
and find me here, disheveled, somehow ready.
The ceiling and I have spent years getting to know each other.
I've made my peace with being someone's insomniac brother.

POET'S NOTES
- Form: Strict villanelle (19 lines, two refrains: lines 1 and 3, repeating as A1 and A2 throughout)
- The shift in the penultimate stanza ("Perhaps the point...") introduces the volta — the emotional turn
- "Businesslike and tender" in the final stanza intentionally juxtaposes registers to create mild irony
```

## Tips
- Specify the exact form for formal poetry — Hermes will adhere to meter and rhyme scheme.
- For free verse, describe the emotional texture rather than a form: `"meditative, slow-moving, sparse"`.
- Use `--length` to request longer narrative poems or very short lyric poems.
- Ask for `"3 opening lines"` to workshop beginnings before committing to a full poem.
- `--occasion eulogy` generates a memorial poem; always review and personalize before use.
