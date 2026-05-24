# Social Media Caption Writer

## Description
Generate platform-optimized captions for any image, product, event, or brand message. Tailors voice, length, hashtag strategy, and CTA to the specific platform (Instagram, LinkedIn, TikTok, Twitter/X, Facebook) and desired tone.

## Why Hermes
Platform-appropriate writing requires understanding the distinct conventions, character limits, and audience expectations of each social network. Hermes adapts voice fluently between LinkedIn's professional register, Instagram's aspirational tone, TikTok's conversational energy, and Twitter's wit-density.

## Quickstart
```bash
python examples/creative/creative_tools.py caption --image-desc "sunset over mountains" --platform instagram --tone inspirational
```

## Sample Input
```
Image description: Product flat lay of handmade ceramic mugs in earthy tones on a linen surface
Platform: Instagram
Brand: Small ceramic studio, values: slow living, handcraft, sustainability
Tone: Warm, intentional, slightly poetic
Goal: Drive to website / shop link
```

## Output Format
```
SOCIAL MEDIA CAPTION: Instagram
Brand: Ceramic Studio | Tone: Warm/Intentional
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPTION 1 (Storytelling)
There's something about wrapping your hands around a mug that actually started as clay on someone's wheel.

Each of these took about two hours to make — from wedging the clay to the final glaze firing. We like to think that time stays in the object somehow.

New pieces just dropped in the shop. Link in bio.

#handmadeceramic #slowliving #ceramics #handmade #smallbatch #makersgonnamake #sustainableliving #pottery

---

OPTION 2 (Short & punchy)
Your morning ritual deserves something made by hand.

New mugs // link in bio 🌿

#ceramics #handmadehome #slowmornings #pottery #handmade

---

OPTION 3 (Community/conversational)
We've been asked a lot lately: how long does each mug take to make?

The honest answer: about two weeks from clay to your hands, if you count drying time. This batch has been worth the wait.

What's the first drink you'd put in yours? ☕

[First comment: full hashtag list to keep caption clean]

---

PLATFORM NOTES
- All options use line breaks strategically — Instagram truncates at ~125 characters before "more"; key message lands in first 2 lines.
- Option 3 uses a question to drive engagement (comments boost algorithm reach).
- Hashtags: 8-15 is the current Instagram sweet spot. Niche tags (#handmadeceramic) reach warmer audiences than mega-tags (#pottery with 50M posts).
- "Link in bio" is still the only clickable Instagram format for feed posts.
```

## Tips
- Provide 3 tone options and choose the one that fits your current content mix best.
- Vary between storytelling captions, short-punchy, and question-based to maintain feed variety.
- For LinkedIn: use `--platform linkedin` for professional, longer-form content without hashtag overload.
- Use `--cta "sign up"` or `--cta "comment below"` to specify the desired action.
- A/B test options 1 and 2 across different posts to learn which tone resonates with your audience.
