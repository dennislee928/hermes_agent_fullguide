#!/usr/bin/env bash
# Detect GPU and print recommended Hermes model + quantization

echo "=== GPU Detection ==="

OS="$(uname -s)"

if [[ "$OS" == "Darwin" ]]; then
  # macOS — check for Apple Silicon
  CHIP=$(sysctl -n machdep.cpu.brand_string 2>/dev/null || echo "unknown")
  MEM_GB=$(( $(sysctl -n hw.memsize) / 1073741824 ))
  echo "Platform: macOS"
  echo "Chip: $CHIP"
  echo "RAM: ${MEM_GB} GB"

  if echo "$CHIP" | grep -q "Apple"; then
    echo "Acceleration: Apple Metal (unified memory)"
    if (( MEM_GB >= 32 )); then
      echo "Recommended: Hermes-3-Llama-3.1-70B Q4_K_M"
    elif (( MEM_GB >= 16 )); then
      echo "Recommended: Hermes-3-Llama-3.1-8B Q8_0"
    else
      echo "Recommended: Hermes-3-Llama-3.1-8B Q4_K_M"
    fi
  else
    echo "Acceleration: CPU only (Intel Mac)"
    echo "Recommended: Hermes-2-Pro-Mistral-7B Q4_K_M"
  fi

elif [[ "$OS" == "Linux" ]]; then
  echo "Platform: Linux"

  if command -v nvidia-smi &>/dev/null; then
    echo "GPU type: NVIDIA (CUDA)"
    nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
    VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits | head -1)
    echo "VRAM: ${VRAM} MiB"
    if (( VRAM >= 40000 )); then
      echo "Recommended: Hermes-3-Llama-3.1-70B Q4_K_M"
    elif (( VRAM >= 8000 )); then
      echo "Recommended: Hermes-3-Llama-3.1-8B Q8_0"
    else
      echo "Recommended: Hermes-3-Llama-3.1-8B Q4_K_M"
    fi

  elif ls /dev/kfd 2>/dev/null; then
    echo "GPU type: AMD (ROCm)"
    rocm-smi --showproductname 2>/dev/null || echo "(install rocm-smi for details)"
    echo "Recommended: Hermes-3-Llama-3.1-8B Q4_K_M"

  else
    echo "GPU type: None (CPU only)"
    RAM_GB=$(( $(grep MemTotal /proc/meminfo | awk '{print $2}') / 1048576 ))
    echo "RAM: ${RAM_GB} GB"
    echo "Recommended: Hermes-2-Pro-Mistral-7B Q3_K_M"
  fi

else
  echo "Platform: $OS (unsupported by this script)"
fi

echo ""
echo "Ollama pull command:"
echo "  ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"
