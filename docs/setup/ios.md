# Hermes on iOS

iOS has tight memory limits and no background process access, so there are two approaches: run the model on-device (small models only) or connect to a local/remote Ollama server.

## Option A — On-device via LLM Farm (recommended for offline use)

[LLM Farm](https://github.com/guinmoon/LLMFarm) is a free iOS app that runs GGUF models locally.

1. Install **LLM Farm** from the App Store
2. Download a small Hermes GGUF model to your Mac, then AirDrop or use Files to transfer it:
   ```bash
   # On Mac — download a small quantization
   huggingface-cli download NousResearch/Hermes-2-Pro-Mistral-7B-GGUF \
     Hermes-2-Pro-Mistral-7B.Q3_K_M.gguf
   ```
3. In LLM Farm → tap **+** → choose your `.gguf` file
4. Set the chat template to **ChatML** (Hermes uses ChatML format)
5. Chat offline

**Memory limits by device:**
| Device | Max model size |
|---|---|
| iPhone 15 Pro (8 GB) | 7B Q4 (~4 GB) |
| iPhone 14 (6 GB) | 7B Q3 (~3 GB) |
| iPhone 13 and older | 3B models only |

## Option B — Pocketpal AI

[PocketPal AI](https://github.com/a-ghorbani/pocketpal-ai) supports Hermes models and has a polished UI.

1. Install from App Store → tap **Models** → search `hermes`
2. Downloads and runs locally — no server needed

## Option C — Connect to a local Ollama server (best quality)

Run Hermes on your Mac/PC and connect from iPhone over your home network.

**On your Mac/Linux/Windows machine:**
```bash
# Allow connections from your network
OLLAMA_HOST=0.0.0.0 ollama serve

# Or set it permanently
launchctl setenv OLLAMA_HOST 0.0.0.0   # macOS
```

**On iOS — use Enchanted app:**
1. Install [Enchanted](https://github.com/AugustDev/enchanted) from the App Store
2. Settings → Server URL → `http://<your-mac-ip>:11434`
3. Select your Hermes model and chat

**Find your Mac's IP:**
```bash
ipconfig getifaddr en0   # macOS Wi-Fi
```

## Option D — Remote API (cloud Ollama or any OpenAI-compatible endpoint)

Any iOS app that supports OpenAI-compatible APIs will work with a remote Ollama instance.

Apps: **Enchanted**, **OpenCat**, **ChatKit**, **Sidekick**

Server URL format: `http://<server-ip>:11434/v1`

## Building a custom iOS app

See [desktop-apps/swift/](../../desktop-apps/swift/) for a SwiftUI app skeleton that connects to an Ollama server using streaming.

Key API call:
```swift
// POST to http://localhost:11434/api/chat
// Body: { "model": "hermes3", "messages": [...], "stream": true }
```
