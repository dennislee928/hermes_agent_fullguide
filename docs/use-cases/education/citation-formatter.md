# Citation Formatter

## Description
Convert raw source information into properly formatted citations in any major style — APA, MLA, Chicago, Harvard, Vancouver, or IEEE. Handles books, journal articles, websites, videos, podcasts, and more. Also formats in-text citations and full reference list entries.

## Why Hermes
Citation formatting requires precise rule-following with many style-specific exceptions (authors with suffixes, corporate authors, no-date sources, DOIs, URLs with access dates). Hermes's instruction-following consistency means it applies citation rules accurately rather than guessing at formatting edge cases.

## Quickstart
```bash
python examples/education/writing_and_research.py cite --style APA --source "Author: Chen J, Title: Sleep and Memory, Journal: Nature Neuroscience, Year: 2023, Volume: 26, Pages: 112-119, DOI: 10.1038/s41593-023-01234-5"
```

## Sample Input
```
Style: APA 7th edition
Source type: Journal article
Author: Jennifer M. Watson, David L. Strayer
Title: Supertaskers: Profiles in extraordinary multitasking ability
Journal: Psychonomic Bulletin & Review
Year: 2010
Volume: 17
Issue: 3
Pages: 479-485
DOI: 10.3758/PBR.17.3.479
```

## Output Format
```
CITATION: APA 7th Edition
━━━━━━━━━━━━━━━━━━━━━━━━

REFERENCE LIST ENTRY
Watson, J. M., & Strayer, D. L. (2010). Supertaskers: Profiles in extraordinary multitasking ability. Psychonomic Bulletin & Review, 17(3), 479–485. https://doi.org/10.3758/PBR.17.3.479

IN-TEXT CITATION
(Watson & Strayer, 2010)

NARRATIVE IN-TEXT CITATION
Watson and Strayer (2010) found that...

FORMATTING NOTES
- Two authors: use "&" in reference list; use "and" in running text
- Volume number is italicized along with journal name
- Issue number in parentheses (not italicized) follows volume
- En dash used in page range (479–485), not hyphen
- DOI formatted as URL (https://doi.org/...)
```

## Tips
- Provide as much source information as possible for the most accurate output.
- Use `--source-type website` and include the access date for web sources.
- For books with editors, specify `--role editor` to get the correct `(Ed.)` formatting.
- Batch multiple sources by providing a numbered list and asking for the full reference list sorted alphabetically.
