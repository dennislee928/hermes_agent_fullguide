# Research Paper Summarizer

## Description
Transform dense academic papers into clear, structured summaries that capture the research question, methodology, key findings, limitations, and implications. Output is calibrated for researchers, students, or general readers depending on the specified audience.

## Why Hermes
Academic papers are structured documents with predictable sections, but extracting the essential contribution requires understanding what makes a finding novel versus what is background. Hermes identifies the paper's core contribution and structures the summary around it rather than producing a section-by-section synopsis.

## Quickstart
```bash
python examples/education/writing_and_research.py summarize --file paper.txt
```

## Sample Input
```
[Full text of a 10-page neuroscience paper on working memory and sleep deprivation]
```

## Output Format
```
RESEARCH PAPER SUMMARY
Title: Sleep Deprivation Selectively Impairs Prefrontal-Dependent Working Memory Processes
Authors: Chen et al. | Journal: Nature Neuroscience | Year: 2023
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RESEARCH QUESTION
Does 24-hour sleep deprivation impair working memory uniformly, or does it selectively affect prefrontal-dependent processes while sparing hippocampal-dependent memory?

METHODOLOGY
- 48 participants (24 sleep-deprived, 24 control)
- fMRI during n-back working memory tasks
- Analysis: BOLD signal in prefrontal cortex vs. hippocampus across memory load conditions

KEY FINDINGS
1. Sleep deprivation reduced prefrontal cortex activation by 34% during high-load working memory tasks.
2. Hippocampal activation was statistically unchanged between groups.
3. Performance decrements were largest in tasks requiring active manipulation of held information (not passive maintenance).

LIMITATIONS
- Sample drawn from university students; generalizability to older adults unclear.
- Only 24-hour deprivation studied; chronic deprivation effects may differ.
- fMRI measures neural correlates, not direct causal evidence.

IMPLICATIONS
Findings suggest targeted interventions (e.g., sleep hygiene for students before exams requiring complex reasoning) rather than blanket claims that sleep deprivation impairs all memory equally.

KEY TERMS
- n-back task: A working memory test requiring subjects to remember stimuli presented n steps back
- BOLD signal: Blood-oxygen-level-dependent signal, the fMRI measure of neural activity
- Prefrontal cortex: Brain region associated with executive function and active cognitive manipulation

PLAIN-LANGUAGE SUMMARY
After a sleepless night, your brain struggles more with tasks that require you to manipulate information (like mental math) than tasks requiring you to simply hold and recall information. The "executive" front part of the brain is more affected than the memory-storage regions.
```

## Tips
- Paste the full paper text as a `.txt` file for complete summaries.
- Add `--audience general` for a plain-language version suitable for sharing with non-specialists.
- Use `--focus methodology` when evaluating whether to replicate a study.
- Combine with citation-formatter to generate a properly formatted reference after summarizing.
