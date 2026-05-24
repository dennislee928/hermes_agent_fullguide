const GITHUB = "https://github.com/Dennislee/hermes_agent_fullguide";

const links = {
  "Guide": [
    { label: "macOS Setup", href: `${GITHUB}/blob/main/docs/setup/macos.md` },
    { label: "Windows Setup", href: `${GITHUB}/blob/main/docs/setup/windows.md` },
    { label: "Linux Setup", href: `${GITHUB}/blob/main/docs/setup/linux.md` },
    { label: "iOS Setup", href: `${GITHUB}/blob/main/docs/setup/ios.md` },
    { label: "Android Setup", href: `${GITHUB}/blob/main/docs/setup/android.md` },
  ],
  "Use Cases": [
    { label: "Local Chatbot", href: `${GITHUB}/blob/main/docs/use-cases/local-chatbot.md` },
    { label: "RAG Pipeline", href: `${GITHUB}/blob/main/docs/use-cases/rag-pipeline.md` },
    { label: "Function Calling", href: `${GITHUB}/blob/main/docs/use-cases/function-calling.md` },
    { label: "Autonomous Agent", href: `${GITHUB}/blob/main/docs/use-cases/autonomous-agent.md` },
  ],
  "Desktop Apps": [
    { label: "Electron", href: `${GITHUB}/tree/main/desktop-apps/electron` },
    { label: "Tauri", href: `${GITHUB}/tree/main/desktop-apps/tauri` },
    { label: "React Native", href: `${GITHUB}/tree/main/desktop-apps/react-native` },
    { label: "SwiftUI", href: `${GITHUB}/tree/main/desktop-apps/swift` },
  ],
  "Resources": [
    { label: "NousResearch HuggingFace", href: "https://huggingface.co/NousResearch" },
    { label: "Ollama", href: "https://ollama.com" },
    { label: "GitHub Releases", href: `${GITHUB}/releases` },
    { label: "Report an Issue", href: `${GITHUB}/issues` },
  ],
};

export default function Footer() {
  return (
    <footer style={{ borderTop: "1px solid var(--border)", background: "var(--bg2)", padding: "64px 0 40px" }}>
      <div className="container">
        <div style={{ display: "grid", gridTemplateColumns: "1fr repeat(4, auto)", gap: 48, marginBottom: 48, flexWrap: "wrap" }}>
          {/* Brand */}
          <div>
            <div style={{ fontWeight: 800, fontSize: 20, marginBottom: 12 }}>⚡ Hermes</div>
            <p style={{ fontSize: 13, color: "var(--text2)", lineHeight: 1.7, maxWidth: 200 }}>
              NousResearch Hermes LLM running locally on every platform.
            </p>
            <a href={GITHUB} target="_blank" rel="noopener" style={{
              display: "inline-flex", alignItems: "center", gap: 6,
              marginTop: 16, color: "var(--text2)", textDecoration: "none", fontSize: 13,
              transition: "color 0.15s",
            }}
            onMouseEnter={e => e.currentTarget.style.color = "var(--text)"}
            onMouseLeave={e => e.currentTarget.style.color = "var(--text2)"}
            >
              <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"/>
              </svg>
              View on GitHub
            </a>
          </div>

          {Object.entries(links).map(([section, items]) => (
            <div key={section}>
              <div style={{ fontWeight: 700, fontSize: 12, letterSpacing: "0.08em", color: "var(--text3)",
                textTransform: "uppercase", marginBottom: 16 }}>{section}</div>
              <ul style={{ listStyle: "none", display: "flex", flexDirection: "column", gap: 10 }}>
                {items.map(item => (
                  <li key={item.label}>
                    <a href={item.href} target="_blank" rel="noopener" style={{
                      color: "var(--text2)", textDecoration: "none", fontSize: 13,
                      transition: "color 0.15s",
                    }}
                    onMouseEnter={e => e.target.style.color = "var(--text)"}
                    onMouseLeave={e => e.target.style.color = "var(--text2)"}
                    >{item.label}</a>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>

        <div style={{ borderTop: "1px solid var(--border)", paddingTop: 24, display: "flex",
          alignItems: "center", justifyContent: "space-between", flexWrap: "wrap", gap: 12 }}>
          <p style={{ fontSize: 12, color: "var(--text3)" }}>
            MIT License · NousResearch Hermes models are subject to their own licenses
          </p>
          <p style={{ fontSize: 12, color: "var(--text3)" }}>
            Built with React + Vite · Runs 100% locally
          </p>
        </div>
      </div>
    </footer>
  );
}
