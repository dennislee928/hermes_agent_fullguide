import { useState } from "react";
import CodeBlock from "./CodeBlock.jsx";

const platforms = [
  {
    id: "macos",
    label: "macOS",
    icon: "",
    steps: [
      {
        title: "Install Ollama",
        code: `# Via Homebrew
brew install ollama

# Or direct script
curl -fsSL https://ollama.com/install.sh | sh`,
      },
      {
        title: "Pull Hermes 3",
        code: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
      },
      {
        title: "Chat",
        code: `ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
      },
      {
        title: "Or use the one-command installer",
        code: `bash scripts/setup/install_macos.sh`,
      },
    ],
    note: "Apple Silicon (M1/M2/M3) uses Metal GPU acceleration automatically.",
  },
  {
    id: "windows",
    label: "Windows",
    icon: "🪟",
    steps: [
      {
        title: "Install Ollama",
        code: `winget install Ollama.Ollama`,
      },
      {
        title: "Pull Hermes 3",
        code: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
      },
      {
        title: "Chat",
        code: `ollama run hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
      },
      {
        title: "Or use the PowerShell installer",
        code: `powershell -ExecutionPolicy Bypass -File scripts\\setup\\install_windows.ps1`,
      },
    ],
    note: "NVIDIA CUDA is auto-detected. Install CUDA Toolkit for GPU acceleration.",
  },
  {
    id: "linux",
    label: "Linux",
    icon: "🐧",
    steps: [
      {
        title: "Install Ollama",
        code: `curl -fsSL https://ollama.com/install.sh | sh
# Runs as a systemd service automatically`,
      },
      {
        title: "Pull Hermes 3",
        code: `ollama pull hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF`,
      },
      {
        title: "Check GPU & get model recommendation",
        code: `bash scripts/setup/check_gpu.sh`,
      },
      {
        title: "Or run the full stack with Docker",
        code: `cd configs && docker compose up -d
# Open WebUI → http://localhost:3000`,
      },
    ],
    note: "NVIDIA CUDA and AMD ROCm both supported. Run check_gpu.sh to auto-detect.",
  },
  {
    id: "ios",
    label: "iOS",
    icon: "",
    steps: [
      {
        title: "On-device (LLM Farm app)",
        code: `# Install LLM Farm from App Store
# Download a small model on your Mac:
huggingface-cli download NousResearch/Hermes-2-Pro-Mistral-7B-GGUF \\
  Hermes-2-Pro-Mistral-7B.Q3_K_M.gguf
# AirDrop the .gguf file to your iPhone
# Open LLM Farm → + → select file → set template: ChatML`,
      },
      {
        title: "Connect to local Ollama (better quality)",
        code: `# On your Mac — allow network connections:
OLLAMA_HOST=0.0.0.0 ollama serve

# Install Enchanted app from App Store
# Settings → Server URL → http://<your-mac-ip>:11434`,
      },
    ],
    note: "iPhone 15 Pro (8 GB) can run 7B Q4 models. Older devices need smaller quantizations.",
  },
  {
    id: "android",
    label: "Android",
    icon: "🤖",
    steps: [
      {
        title: "On-device (PocketPal AI app)",
        code: `# Install PocketPal AI from Google Play or GitHub Releases
# Tap Models → search "hermes" → Download
# Works offline on Snapdragon 8 Gen 2+ devices`,
      },
      {
        title: "Connect to local Ollama",
        code: `# On your PC/Mac:
OLLAMA_HOST=0.0.0.0 ollama serve

# On Android — open Chrome and go to:
# http://<server-ip>:3000  (Open WebUI)
# Or install Catai app → set Ollama server URL`,
      },
    ],
    note: "12 GB RAM devices can run 7B Q4. 8 GB devices should use 7B Q3 or 3B Q4.",
  },
];

export default function SetupGuide() {
  const [active, setActive] = useState("macos");
  const platform = platforms.find(p => p.id === active);

  return (
    <section id="setup" className="section" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        <div style={{ marginBottom: 48 }}>
          <div className="section-label">Installation</div>
          <h2 className="section-title">Set up on any OS</h2>
          <p className="section-sub">One-command installs for every major platform.</p>
        </div>

        {/* OS tabs */}
        <div style={{ display: "flex", gap: 4, marginBottom: 32, flexWrap: "wrap" }}>
          {platforms.map(p => (
            <button
              key={p.id}
              onClick={() => setActive(p.id)}
              style={{
                padding: "8px 18px", borderRadius: "var(--radius-sm)",
                border: "1px solid",
                borderColor: active === p.id ? "var(--blue)" : "var(--border)",
                background: active === p.id ? "var(--blue-glow)" : "transparent",
                color: active === p.id ? "var(--blue)" : "var(--text2)",
                fontWeight: 600, fontSize: 14, cursor: "pointer", transition: "all 0.15s",
                display: "flex", alignItems: "center", gap: 6,
              }}
            >
              {p.icon} {p.label}
            </button>
          ))}
        </div>

        {/* Steps */}
        <div style={{ display: "grid", gap: 16 }}>
          {platform.steps.map((step, i) => (
            <div key={i} className="card" style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                <span style={{
                  width: 24, height: 24, borderRadius: "50%",
                  background: "var(--blue-glow)", border: "1px solid var(--blue)",
                  display: "flex", alignItems: "center", justifyContent: "center",
                  fontSize: 12, fontWeight: 700, color: "var(--blue)", flexShrink: 0,
                }}>{i + 1}</span>
                <span style={{ fontWeight: 600, fontSize: 15 }}>{step.title}</span>
              </div>
              <CodeBlock code={step.code} />
            </div>
          ))}

          {platform.note && (
            <div style={{
              padding: "12px 16px", borderRadius: "var(--radius-sm)",
              background: "rgba(79,110,247,0.06)", border: "1px solid rgba(79,110,247,0.2)",
              fontSize: 13, color: "var(--text2)", display: "flex", gap: 8, alignItems: "flex-start",
            }}>
              <span style={{ color: "var(--blue)", fontWeight: 700, flexShrink: 0 }}>ℹ</span>
              {platform.note}
            </div>
          )}
        </div>
      </div>
    </section>
  );
}
