# Hermes on macOS

## Requirements

- macOS 12 Monterey or later
- 8 GB RAM minimum (16 GB recommended for 8B models)
- Apple Silicon (M1/M2/M3) gets Metal GPU acceleration automatically

## Option A — Ollama (recommended)

```bash
# Install via Homebrew
brew install ollama

# Or direct install
curl -fsSL https://ollama.com/install.sh | sh

# Start the server
ollama serve &

# Pull Hermes 3 (8B, ~5 GB)
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF

# Interactive chat
ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

Ollama auto-detects Apple Silicon and uses Metal for GPU offloading.

## Option B — LM Studio (GUI)

1. Download from https://lmstudio.ai
2. Open LM Studio → Search bar → type `hermes`
3. Download `NousResearch/Hermes-3-Llama-3.1-8B-GGUF`
4. Click **Load Model** → Chat or enable the local server on port 1234

LM Studio's local server is OpenAI-API-compatible — use it as a drop-in replacement.

## Option C — Python direct (llama-cpp-python)

```bash
# Install with Metal support
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# Download a GGUF model
huggingface-cli download NousResearch/Hermes-3-Llama-3.1-8B-GGUF \
  Hermes-3-Llama-3.1-8B.Q4_K_M.gguf --local-dir ./models
```

Then use the [basic-chat Python example](../../examples/basic-chat/python/).

## Verify GPU is being used

```bash
# For Ollama
ollama ps
# Should show "100% GPU" for Apple Silicon

# For llama-cpp-python — check logs for:
# "Metal: Found device: Apple M..."
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `ollama: command not found` | Re-open terminal after install, or add `/usr/local/bin` to PATH |
| Model downloads slowly | Use `OLLAMA_MODELS=~/models ollama pull ...` to change storage location |
| Out of memory | Use a smaller quantization: `Q4_K_M` instead of `Q8_0` |
| Metal errors on M1 | Update to macOS 13+ |
