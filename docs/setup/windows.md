# Hermes on Windows

## Requirements

- Windows 10 22H2 or Windows 11
- 8 GB RAM minimum (16 GB recommended)
- NVIDIA GPU with CUDA 11.8+ for GPU acceleration (optional but recommended)

## Option A — Ollama (recommended)

```powershell
# Install via winget
winget install Ollama.Ollama

# Or download the installer from https://ollama.com/download/windows

# After install, open a new terminal:
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

Ollama auto-detects CUDA and uses your GPU if available.

## Option B — LM Studio (GUI)

1. Download from https://lmstudio.ai
2. Search for `hermes` → Download `Hermes-3-Llama-3.1-8B-GGUF`
3. Load and chat, or start the local API server (port 1234)

## Option C — Docker (CUDA)

Requires [Docker Desktop](https://www.docker.com/products/docker-desktop/) with WSL2 backend and NVIDIA Container Toolkit.

```powershell
# Enable NVIDIA support in Docker Desktop settings first
docker run -d --gpus all -p 11434:11434 -v ollama:/root/.ollama ollama/ollama

# Pull and run
docker exec -it <container_id> ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

## Option D — Python (llama-cpp-python with CUDA)

```powershell
# Install CUDA toolkit first: https://developer.nvidia.com/cuda-downloads
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu122

# Download model
huggingface-cli download NousResearch/Hermes-3-Llama-3.1-8B-GGUF `
  Hermes-3-Llama-3.1-8B.Q4_K_M.gguf --local-dir .\models
```

## Verify GPU usage

```powershell
# Check Ollama
ollama ps
# Look for "GPU" in the output

# Monitor GPU in real-time
nvidia-smi -l 1
```

## Troubleshooting

| Problem | Fix |
|---|---|
| Ollama won't start | Run as Administrator, check Windows Firewall isn't blocking port 11434 |
| CUDA not detected | Install/update NVIDIA drivers + CUDA toolkit; restart after install |
| Slow on CPU only | Install CUDA or use a smaller model (`Q3_K_M` quantization) |
| `PATH` issues | Restart terminal; Ollama installs to `%LOCALAPPDATA%\Programs\Ollama` |
