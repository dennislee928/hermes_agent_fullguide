# Hermes Agent Full Guide

A comprehensive guide for running [NousResearch Hermes LLMs](https://huggingface.co/NousResearch) locally — from first install to production desktop apps on every major platform.

## What's inside

| Section | What you get |
|---|---|
| [Setup guides](docs/setup/) | One-command installs for macOS, Windows, Linux, iOS, Android |
| [Configs](configs/) | Ollama Modelfile, Docker Compose, system prompts |
| [Use cases](docs/use-cases/) | RAG, function calling, agent loops, code assistant — with working code |
| [Examples](examples/) | Runnable Python + TypeScript code for every use case |
| [Desktop apps](desktop-apps/) | Electron, Tauri, React Native, Swift app skeletons |
| [Pipelines](pipelines/) | GitHub Actions that build `.exe` / `.dmg` / `.AppImage` / `.apk` / `.ipa` |

## Quick start (any OS)

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh      # macOS/Linux
# Windows: winget install Ollama.Ollama

# 2. Pull Hermes 3
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF

# 3. Chat
ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

## Recommended models

| Model | Size | Best for |
|---|---|---|
| Hermes-3-Llama-3.1-8B | ~5 GB | Daily use, low VRAM |
| Hermes-3-Llama-3.1-70B | ~40 GB | Max quality, needs GPU |
| Hermes-2-Pro-Mistral-7B | ~4 GB | Function calling |
| Hermes-2-Theta-Llama-3-8B | ~5 GB | Agent/tool use |

## Navigation

- **New to local LLMs?** → Start with your OS setup guide in [docs/setup/](docs/setup/)
- **Want to build something?** → Jump to [docs/use-cases/](docs/use-cases/)
- **Building a desktop app?** → See [desktop-apps/](desktop-apps/) and [pipelines/](pipelines/)
