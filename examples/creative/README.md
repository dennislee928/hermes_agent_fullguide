# Creative Examples

Hermes-powered command-line tools for creative writing and brand work. All scripts connect to a local Ollama instance running the Hermes-3 model.

## Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai) running locally (`ollama serve`)
- The Hermes model pulled: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`

## Installation

```bash
pip install -r requirements.txt
```

## Scripts

### creative_tools.py

Short story generator, songwriting assistant, poem generator, social media caption writer, and brand naming assistant — all in one script.

```bash
# Short story generation
python creative_tools.py story --genre thriller --setting "Tokyo 2050" --length short
python creative_tools.py story --genre "magical realism" --theme "memory and loss" --style "literary fiction"
python creative_tools.py story --genre horror --length flash --pov second

# Songwriting
python creative_tools.py song --mood melancholic --theme "lost love" --style "indie folk"
python creative_tools.py song --mood hopeful --theme "new beginnings" --style "americana" --structure VCVCBC
python creative_tools.py song --develop-hook "the road home runs both ways" --style country

# Poetry
python creative_tools.py poem --type sonnet --occasion birthday --for "my grandmother"
python creative_tools.py poem --type villanelle --subject insomnia --tone "quietly desperate, dark humor"
python creative_tools.py poem --type haiku --subject "first snow"
python creative_tools.py poem --type free verse --subject "grief" --tone elegiac

# Social media captions
python creative_tools.py caption --image-desc "sunset over mountains" --platform instagram --tone inspirational
python creative_tools.py caption --image-desc "team photo at product launch" --platform linkedin --goal "announce launch"
python creative_tools.py caption --image-desc "handmade ceramic mugs" --platform instagram --brand "small ceramics studio, slow living values" --cta "shop link in bio"

# Brand naming
python creative_tools.py brand --product "sustainable water bottle" --audience "eco-conscious millennials" --count 10
python creative_tools.py brand --product "AI finance app" --audience "millennials, financially anxious" --values "clarity, approachable" --avoid "banking jargon"
python creative_tools.py brand --product "online tutoring platform" --count 8 --naming-type coined
```

## Tips

- For stories, `--length flash` (250-500 words) is great for quick creative sparks; `--length medium` (2,000-3,000 words) produces fully developed narratives.
- For songs, provide both `--mood` and `--theme` for the most emotionally coherent output.
- For poems, formal types (sonnet, villanelle) will adhere strictly to structure; `--type free verse` gives more expressive latitude.
- For captions, always specify `--platform` — the output is specifically optimized for each platform's conventions.
- For brand names, include `--avoid` to steer away from naming approaches that don't fit your brand.

Use `--help` on any subcommand for the full option list:

```bash
python creative_tools.py story --help
python creative_tools.py brand --help
```
