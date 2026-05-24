# Hermes Setup for Windows
# Run as: powershell -ExecutionPolicy Bypass -File install_windows.ps1

param(
  [string]$Model = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"
)

Write-Host "=== Hermes Setup for Windows ===" -ForegroundColor Cyan

# Install Ollama via winget
if (-not (Get-Command ollama -ErrorAction SilentlyContinue)) {
  Write-Host "Installing Ollama via winget..."
  winget install Ollama.Ollama --accept-source-agreements --accept-package-agreements
  # Refresh PATH
  $env:PATH = [System.Environment]::GetEnvironmentVariable("PATH", "Machine") + ";" + `
              [System.Environment]::GetEnvironmentVariable("PATH", "User")
}

# Start Ollama in background
Start-Process -FilePath "ollama" -ArgumentList "serve" -WindowStyle Hidden
Start-Sleep -Seconds 3

# Detect GPU
$gpu = Get-WmiObject Win32_VideoController | Select-Object -First 1 Name
Write-Host "GPU: $($gpu.Name)"
if ($gpu.Name -match "NVIDIA") {
  Write-Host "NVIDIA GPU detected — CUDA acceleration will be used" -ForegroundColor Green
} elseif ($gpu.Name -match "AMD") {
  Write-Host "AMD GPU detected — ROCm may be available" -ForegroundColor Yellow
} else {
  Write-Host "No discrete GPU detected — running on CPU" -ForegroundColor Yellow
}

# Pull model
Write-Host "Pulling model: $Model"
ollama pull $Model

Write-Host ""
Write-Host "Done! Run: ollama run $Model" -ForegroundColor Green
Write-Host "API available at: http://localhost:11434"
