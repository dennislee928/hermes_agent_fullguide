# Brand Naming Assistant

## Description
Generate original brand name options for any product, service, or company. Each name comes with a rationale explaining the meaning, associations, and strategic positioning — plus availability considerations and domain/trademark guidance.

## Why Hermes
Brand naming requires balancing memorability, pronounceability, distinctiveness, and strategic positioning — while avoiding unintended connotations in other languages or markets. Hermes generates names with genuine creative variety (not just compound words) and provides the reasoning behind each option.

## Quickstart
```bash
python examples/creative/creative_tools.py brand --product "sustainable water bottle" --audience "eco-conscious millennials" --count 10
```

## Sample Input
```
Product: AI-powered personal finance app
Target audience: Millennials and Gen Z, financially anxious, want to build wealth
Values: Clarity, approachability, empowerment, not stuffy or corporate
Count: 10
Avoid: Banking jargon, anything that sounds like a legacy financial institution
```

## Output Format
```
BRAND NAME SUGGESTIONS: AI Finance App
Target: Millennials/Gen Z | Values: Approachable, Empowering
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. VERDANT
   Type: Evocative / natural metaphor
   Rationale: From "verdant" (lush, growing). Signals financial growth without using finance-speak. Sounds aspirational and fresh; easy to say and spell.
   Domain check: verdant.com — likely taken; verdantapp.com, getverdant.com worth checking.
   Tone fit: High — nature metaphors resonate with eco-conscious younger demographics.

2. CLIO
   Type: Short / mythological
   Rationale: Greek muse of history — apt for an app that learns from your financial history to guide future decisions. Short, memorable, distinctive. Works as app name.
   Domain check: clio.com is taken (legal software); cliomoney.com, meetclio.com are potential options.
   Tone fit: High — intellectual without being stuffy; works for a younger, culturally aware audience.

3. MOSAIC
   Type: Conceptual / metaphor
   Rationale: Financial health is built from many small pieces. Warm, visual, approachable. Suggests complexity made comprehensible.
   Domain check: mosaicapp.com worth checking.
   Tone fit: Very high — the "putting it all together" metaphor directly addresses financial anxiety.

4. FLOAT
   Type: Everyday word / reframed
   Rationale: Double meaning: "stay afloat" financially + the float of calm, easy management. Simple, one syllable, memorable.
   Domain check: float.com taken (project management tool) — floatfinance.com, getfloat.co as alternatives.
   Tone fit: High — casual and approachable; strong brand character.

5. KITH
   Type: Coined / social
   Rationale: Old English for "one's acquaintances, community." Suggests financial community and belonging; short, distinctive, modern feel.
   Domain check: kith.com taken (streetwear brand) — kithhq.com, kiithapp.com with double-i variant.
   Tone fit: Medium-high — community angle works, but consider brand confusion with existing Kith.

6. SCAFFOLD
   Type: Metaphor / structural
   Rationale: Building financial structure; the app as scaffolding for your financial life. Unusual in finance — memorable for that reason.
   Tone fit: Medium — more architectural/industrial; may not feel warm enough for the anxious-audience brief.

7. LUMEN
   Type: Light metaphor / scientific
   Rationale: Unit of light — the app that illuminates your finances. Clean, modern, short. Works across languages.
   Domain check: lumen.com taken — lumenmoney.com, getlumen.app worth checking.
   Tone fit: High — clarity metaphor is directly on brief.

8. GROVE
   Type: Nature / calm metaphor
   Rationale: A grove suggests shelter, growth, peace — all positive financial associations. Soft sound, easy to remember.
   Tone fit: High — very approachable; warm without being infantilizing.

9. TENOR
   Type: Musical / tonal
   Rationale: Suggests the tone and rhythm of your financial life. Distinctive in finance vertical; musical associations feel modern and creative-class friendly.
   Tone fit: Medium — distinctive but may need more explanation.

10. WAYPOINT
    Type: Navigation metaphor
    Rationale: Milestone on a journey — exactly what financial goals are. Implies progress and direction without urgency or anxiety.
    Tone fit: High — goal-oriented millennials respond well to journey/progress metaphors.

TOP RECOMMENDATIONS FOR YOUR BRIEF
1. MOSAIC — directly addresses financial anxiety with the "pieces together" metaphor
2. FLOAT — most casual and approachable; strong brand character; easy app store discoverability
3. LUMEN — elegant clarity metaphor; modern; cross-language friendly

NEXT STEPS
1. Check trademark availability at USPTO.gov (US) or your relevant IP office
2. Check exact domain + common variants (.com, .app, .co)
3. Search existing app stores for exact and close-match names
4. Test shortlist names with 5-10 members of your target audience for association and pronunciation
```

## Tips
- Provide your values and "avoid" list — these constraints produce better results than open-ended requests.
- Ask for a second round focused on a specific naming type: `"give me 10 more coined/invented word names"`.
- Always check trademark and domain availability before finalizing — names in the output are not pre-cleared.
- Test finalists with actual members of your target audience for unexpected associations.
- Consider how the name sounds as an app command: "Open Float," "Ask Mosaic" — spoken use matters.
