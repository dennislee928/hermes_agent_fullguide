# Songwriting Assistant

## Description
Generate complete song lyrics including verses, chorus, bridge, and hook — or assist with specific sections, rhyme schemes, metaphor development, or melody concepts. Hermes adapts to any genre from country to hip-hop to folk, matching lyrical conventions and emotional register.

## Why Hermes
Great songwriting requires both technical craft (rhyme scheme, meter, syllable count for singability) and emotional authenticity. Hermes generates lyrics that scan naturally for singing, avoids forced rhymes, and creates imagery that resonates rather than just ticking structural boxes.

## Quickstart
```bash
python examples/creative/creative_tools.py song --mood melancholic --theme "lost love" --style "indie folk"
```

## Sample Input
```
Mood: Hopeful but bittersweet
Theme: Leaving home for the first time
Style: Americana / folk country
Structure: Verse-Chorus-Verse-Chorus-Bridge-Chorus
```

## Output Format
```
SONG: "The Road Home Runs Both Ways"
Style: Americana / Folk Country
Structure: V-C-V-C-B-C

[VERSE 1]
My mother pressed her hands against the glass
The morning that I loaded up the truck
She didn't wave — she knew I'd look back last
And held my gaze until the driveway turned to dust

She said, "the road home runs both ways, baby,
And every mile you put between us here
Just means there's that much road to bring you back to me"
Her voice the only thing that wasn't clear

[CHORUS]
Oh, but I was born for somewhere I'd never been
For the wide-open ache of in-between
I'll carry what you gave me, every mile I go
And I'll be home, I'll be home — I just don't know when

[VERSE 2]
The exits blur like birthdays into years
The coffee cups and radio static nights
I've called you when the loneliness feels near
And heard you say you're proud in that soft, careful way...

[Bridge, final chorus continue in full output]

SONGWRITING NOTES
- The refrain "road runs both ways" serves as the emotional fulcrum — departure and return held in tension
- Syllable scan: verses are in loose 10-10-10-10 iambic structure for singability
- Bridge shifts to second-person to create intimacy before final chorus
- Consider: the pause before "I just don't know when" in the chorus is a natural moment for a melodic pull
```

## Tips
- Specify `--structure` explicitly (e.g., `VCVCBC`) for precise song architecture.
- Add `--rhyme-scheme ABAB` or `--rhyme-scheme AABB` to control rhyme pattern.
- Use `--develop-hook "your current hook idea"` to expand a strong line you already have.
- Ask for `"3 alternative chorus options"` to compare emotional angles before committing.
- Provide `--key` and `--tempo` for melody and feel suggestions alongside the lyrics.
