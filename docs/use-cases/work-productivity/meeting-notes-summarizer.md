# Meeting Notes Summarizer

## Description
Meeting Notes Summarizer condenses raw, unstructured meeting transcripts or bullet-point notes into a concise summary with decisions made, action items, and owners. It saves teams the manual effort of distilling a 60-minute meeting into a 1-page record.

## Why Hermes
Hermes handles long, noisy input well and accurately extracts structured items (decisions, action items, risks) even when the source text is informal or contains tangents. Its context window and instruction compliance mean it won't hallucinate attendees or fabricate decisions that weren't in the notes.

## Quickstart
```bash
# From a file
python examples/work-productivity/meetings_and_docs.py summarize --file notes.txt

# From piped input
cat meeting_transcript.txt | python examples/work-productivity/meetings_and_docs.py summarize
```

## Sample Input
```
[Rough notes from product sync]
alice said we should push the launch back two weeks because QA found 3 critical bugs
bob agreed, said his team needs the time
carol asked about the marketing campaign - do we tell them?
alice: yes, she'll email them today
dave: the infra work is done, he can help QA if needed
action: alice emails marketing, bob prioritizes bug fixes, dave supports QA
next sync thursday same time
```

## Expected Output Format
```
## Meeting Summary — Product Sync
Date: [DATE]

### Key Decisions
- Launch postponed by two weeks due to 3 critical QA bugs.
- Engineering will support QA with Dave's available capacity.

### Action Items
| Owner | Action                                      | Due       |
|-------|---------------------------------------------|-----------|
| Alice | Email marketing team about launch delay     | Today     |
| Bob   | Prioritize and schedule critical bug fixes  | This week |
| Dave  | Coordinate with QA team on support capacity | This week |

### Next Meeting
Thursday, same time.
```

## Tips
- Paste raw transcript text — Hermes handles filler words, crosstalk indicators, and informal phrasing.
- Use `--format slack` to get a more compact version suitable for pasting into a Slack message.
- Add `--extract decisions` or `--extract actions` if you only need one section.
- For long transcripts (>2000 words), pipe the file for best results.
