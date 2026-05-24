# Short Story Generator

## Description
Generate original short fiction across any genre, setting, and length. Hermes creates stories with coherent narrative arcs, developed characters, atmospheric prose, and satisfying resolutions — not just plot summaries, but actual readable fiction.

## Why Hermes
Hermes-3's training on diverse literary sources gives it a strong grasp of genre conventions, narrative structure, and prose style. It maintains internal consistency across a story, avoids common AI fiction pitfalls (meandering plots, cardboard characters), and can write in distinct styles when prompted.

## Quickstart
```bash
python examples/creative/creative_tools.py story --genre thriller --setting "Tokyo 2050" --length short
```

## Sample Input
```
Genre: Magical realism
Setting: A small fishing village, present day
Theme: Memory and loss
Length: Short (800-1200 words)
Style: Literary fiction
```

## Output Format
```
THE WEIGHT OF SALT
— A Short Story —

The fisherman found the jar on the third morning after his wife's funeral, wedged between two rocks where the tide had deposited it like an afterthought. It was sealed with wax the color of old honey, and inside, pressed flat against the glass, was what appeared to be a map drawn in blue ink that had not quite dried.

He almost left it. His son had warned him about collecting things from the beach, and at seventy-two, Jorge had collected enough. But the jar caught the light in a way that reminded him of Elena's eyes when she laughed — that particular quality of light that turns something ordinary into evidence of grace — and so he put it in his coat pocket and carried it home through the salt-thick air...

[Story continues for ~1,000 words with full narrative arc, climax, and resolution]
```

## Tips
- Specify `--style` to direct Hermes toward a particular author's register: `"Hemingway's minimalism"`, `"magical realism in the style of Márquez"`, or `"noir"`.
- Use `--pov` to specify first, second, or third person narration.
- Add `--theme` for thematic depth beyond plot mechanics.
- `--length medium` (2,000-3,500 words) for a more developed narrative with subplot.
- For serialized fiction, include `--continue "previous chapter text"` to maintain continuity.
