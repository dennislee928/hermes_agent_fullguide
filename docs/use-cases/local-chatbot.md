# Use Case: Local Chatbot

Build a terminal or web chatbot backed by Hermes running entirely on your machine.

## Why Hermes for chatbot?

- Strong instruction following from Hermes-3 training
- ChatML format gives precise control over persona and context
- 8K context window handles long conversations
- Runs offline — no API keys, no data leaving your machine

## Architecture

```
User input → Python client → Ollama HTTP API → Hermes model → streamed response
```

## Quickstart

```bash
# Pull the model
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF

# Create a named model with custom system prompt
ollama create hermes3 -f configs/Modelfile.hermes3

# Run examples
cd examples/basic-chat/python
pip install -r requirements.txt
python chat.py
```

## Code

See [examples/basic-chat/python/chat.py](../../examples/basic-chat/python/chat.py) — includes:
- Streaming responses
- Conversation history
- System prompt injection
- Ctrl+C graceful exit

TypeScript version: [examples/basic-chat/typescript/chat.ts](../../examples/basic-chat/typescript/chat.ts)

## Web UI (zero code)

```bash
cd configs
docker compose up -d
# Open http://localhost:3000
# Select your hermes3 model from the dropdown
```

## Customizing the persona

Edit `configs/Modelfile.hermes3` SYSTEM block, then:

```bash
ollama create my-assistant -f configs/Modelfile.hermes3
ollama run my-assistant
```

## Key parameters

| Parameter | Effect | Recommended |
|---|---|---|
| `temperature` | Creativity vs consistency | 0.7 for chat, 0.1 for facts |
| `num_ctx` | Context window (tokens) | 8192 |
| `top_p` | Nucleus sampling | 0.9 |
| `repeat_penalty` | Reduce repetition | 1.1 |
