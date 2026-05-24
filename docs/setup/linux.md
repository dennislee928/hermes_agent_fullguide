# Hermes on Linux

## Requirements

- Ubuntu 20.04+ / Debian 11+ / Arch / Fedora / any modern distro
- 8 GB RAM minimum
- NVIDIA GPU + CUDA for acceleration, or AMD GPU + ROCm

## Option A — Ollama (recommended)

```bash
# Universal install script
curl -fsSL https://ollama.com/install.sh | sh

# Ollama runs as a systemd service automatically
systemctl status ollama

# Pull and run
ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF
```

### NVIDIA GPU setup

```bash
# Install CUDA (Ubuntu)
sudo apt install nvidia-cuda-toolkit

# Or via NVIDIA's official repo (recommended for latest CUDA)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt update && sudo apt install cuda-toolkit

# Verify
nvidia-smi
ollama ps  # should show GPU after pulling a model
```

### AMD GPU (ROCm) setup

```bash
# Ubuntu 22.04
sudo apt install rocm-hip-sdk

# Set env var for Ollama to use ROCm
export OLLAMA_GPU=rocm
ollama serve
```

## Option B — Docker Compose

See [configs/docker-compose.yml](../../configs/docker-compose.yml) for a full stack with Ollama + Open WebUI.

```bash
cd configs
docker compose up -d
# Open WebUI available at http://localhost:3000
```

## Option C — Package managers

```bash
# Arch Linux (AUR)
yay -S ollama

# Nix
nix-env -iA nixpkgs.ollama

# Flatpak (for LM Studio)
flatpak install flathub ai.lmstudio.LMStudio
```

## Option D — llama-cpp-python

```bash
# CPU only
pip install llama-cpp-python

# CUDA
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install llama-cpp-python

# ROCm
CMAKE_ARGS="-DLLAMA_HIPBLAS=on" pip install llama-cpp-python

# Download model
huggingface-cli download NousResearch/Hermes-3-Llama-3.1-8B-GGUF \
  Hermes-3-Llama-3.1-8B.Q4_K_M.gguf --local-dir ./models
```

## Run as a persistent service

```bash
# Ollama is already a systemd service after install
sudo systemctl enable --now ollama

# Check logs
journalctl -u ollama -f
```

## Troubleshooting

| Problem | Fix |
|---|---|
| Permission denied on `/dev/kfd` (AMD) | `sudo usermod -aG render $USER` then re-login |
| CUDA out of memory | Use `Q4_K_M` quantization; set `CUDA_VISIBLE_DEVICES=0` |
| Ollama port 11434 in use | `sudo lsof -i :11434` to find and kill the conflict |
| Slow download | Set `OLLAMA_ORIGINS=*` and use a model mirror if needed |
