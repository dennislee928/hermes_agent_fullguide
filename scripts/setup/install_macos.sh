#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF}"

echo "=== Hermes Setup for macOS ==="

# Install Homebrew if missing
if ! command -v brew &>/dev/null; then
  echo "Installing Homebrew..."
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Ollama
if ! command -v ollama &>/dev/null; then
  echo "Installing Ollama..."
  brew install ollama
fi

# Start Ollama service
brew services start ollama
sleep 2

# Pull the model
echo "Pulling model: $MODEL"
ollama pull "$MODEL"

# Detect GPU
if system_profiler SPDisplaysDataType 2>/dev/null | grep -q "Metal"; then
  echo "Apple Metal GPU detected — model will run accelerated"
else
  echo "No Metal GPU detected — running on CPU"
fi

echo ""
echo "Done! Run: ollama run $MODEL"
