"""
Streaming terminal chatbot using Hermes via Ollama.
Run: python chat.py [--model hermes3] [--system "your system prompt"]
"""

import argparse
import json
import sys
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
DEFAULT_MODEL = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"
DEFAULT_SYSTEM = "You are Hermes, a helpful AI assistant. Think step by step."


def stream_chat(model: str, messages: list[dict]) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={"model": model, "messages": messages, "stream": True},
        stream=True,
        timeout=120,
    )
    response.raise_for_status()

    full_response = ""
    for line in response.iter_lines():
        if not line:
            continue
        chunk = json.loads(line)
        token = chunk.get("message", {}).get("content", "")
        print(token, end="", flush=True)
        full_response += token
        if chunk.get("done"):
            break

    print()
    return full_response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--system", default=DEFAULT_SYSTEM)
    args = parser.parse_args()

    messages = [{"role": "system", "content": args.system}]

    print(f"Hermes Chat ({args.model})")
    print("Type 'quit' or press Ctrl+C to exit.\n")

    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            sys.exit(0)

        if user_input.lower() in ("quit", "exit", "q"):
            print("Goodbye!")
            sys.exit(0)

        if not user_input:
            continue

        messages.append({"role": "user", "content": user_input})

        print("Hermes: ", end="", flush=True)
        reply = stream_chat(args.model, messages)
        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
