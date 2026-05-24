#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF}"

echo "=== Hermes Setup for Linux ==="

# Install Ollama
if ! command -v ollama &>/dev/null; then
  echo "Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
fi

# Enable and start systemd service
if command -v systemctl &>/dev/null; then
  sudo systemctl enable --now ollama
  sleep 2
else
  ollama serve &
  sleep 2
fi

# Detect GPU
if command -v nvidia-smi &>/dev/null; then
  echo "NVIDIA GPU detected:"
  nvidia-smi --query-gpu=name,memory.total --format=csv,noheader
elif ls /dev/kfd 2>/dev/null; then
  echo "AMD GPU detected (ROCm)"
else
  echo "No GPU detected — running on CPU"
fi

# Pull model
echo "Pulling model: $MODEL"
ollama pull "$MODEL"

echo ""
echo "Done! Run: ollama run $MODEL"
echo "API available at: http://localhost:11434"
