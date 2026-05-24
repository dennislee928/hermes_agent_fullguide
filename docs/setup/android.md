# Hermes on Android

## Option A — PocketPal AI (easiest, on-device)

[PocketPal AI](https://github.com/a-ghorbani/pocketpal-ai) runs GGUF models on-device using llama.cpp.

1. Install from Google Play or GitHub Releases
2. Tap **Models** → search `hermes` → download
3. Chat fully offline

Tested on Snapdragon 8 Gen 2+ and Dimensity 9200+ devices.

**RAM guidelines:**
| RAM | Max model |
|---|---|
| 12 GB+ | 7B Q4 |
| 8 GB | 7B Q3 or 3B Q4 |
| 6 GB | 3B Q4 only |

## Option B — MLC Chat (GPU-accelerated via Vulkan)

[MLC LLM](https://github.com/mlc-ai/mlc-llm) compiles models for Vulkan — runs on most Android devices with Adreno/Mali GPUs.

1. Install MLC Chat from [GitHub Releases](https://github.com/mlc-ai/mlc-llm/releases)
2. The app includes pre-compiled Hermes variants
3. For custom models, use the [MLC compile pipeline](https://mlc.ai/mlc-llm/docs/)

## Option C — Connect to a local Ollama server (best quality)

Same approach as iOS — run Ollama on your PC/Mac and connect from Android.

**On your server:**
```bash
OLLAMA_HOST=0.0.0.0 ollama serve
```

**On Android — use Open WebUI (browser-based):**
1. Navigate to `http://<server-ip>:3000` in Chrome
2. Works as a PWA — add to home screen for app-like experience

**Or use Ollama-compatible Android apps:**
- **Catai** — open-source, supports remote Ollama servers
- **LLMChat** — supports OpenAI-compatible endpoints

## Option D — Termux (power users)

Run Ollama natively on Android via [Termux](https://termux.dev).

```bash
# In Termux
pkg update && pkg install golang git cmake
git clone https://github.com/ollama/ollama
cd ollama && go build .

# Pull and run (ARM-only models)
./ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
./ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

Note: No Vulkan GPU acceleration via Termux — CPU only.

## Building a custom Android app

See [desktop-apps/react-native/](../../desktop-apps/react-native/) for a React Native app that connects to an Ollama server with streaming support.

Key endpoint: `http://<server-ip>:11434/api/chat`

## Troubleshooting

| Problem | Fix |
|---|---|
| App crashes on load | Model too large for device RAM — use smaller quantization |
| Can't connect to server | Check both devices are on same Wi-Fi; disable Android battery optimization for the app |
| Vulkan not working | Device may not support Vulkan compute — fall back to CPU |
