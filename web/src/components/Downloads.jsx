const GITHUB = "https://github.com/Dennislee/hermes_agent_fullguide";
const RELEASES = `${GITHUB}/releases/latest`;

const apps = [
  {
    name: "Hermes Desktop",
    framework: "Electron",
    icon: "🖥️",
    desc: "Full-featured chat app. Connects to local Ollama. Lists all your models.",
    platforms: [
      { os: "Windows", icon: "🪟", ext: ".exe", label: "Download .exe", href: `${RELEASES}` },
      { os: "macOS", icon: "", ext: ".dmg", label: "Download .dmg", href: `${RELEASES}` },
      { os: "Linux", icon: "🐧", ext: ".AppImage", label: "Download .AppImage", href: `${RELEASES}` },
    ],
    buildCmd: "cd desktop-apps/electron && npm install && npm run build:mac",
    tag: "Electron",
    tagClass: "tag-blue",
  },
  {
    name: "Hermes Desktop (Lite)",
    framework: "Tauri",
    icon: "⚡",
    desc: "Same features, 10× smaller binary. Built with Rust + WebView. Faster startup.",
    platforms: [
      { os: "Windows", icon: "🪟", ext: ".exe", label: "Download .exe", href: `${RELEASES}` },
      { os: "macOS", icon: "", ext: ".dmg", label: "Download .dmg", href: `${RELEASES}` },
      { os: "Linux", icon: "🐧", ext: ".deb", label: "Download .deb", href: `${RELEASES}` },
    ],
    buildCmd: "cd desktop-apps/tauri && npm install && npm run tauri:build",
    tag: "Tauri",
    tagClass: "tag-green",
  },
  {
    name: "Hermes Mobile",
    framework: "React Native",
    icon: "📱",
    desc: "iOS + Android app. Connects to your home Ollama server over Wi-Fi.",
    platforms: [
      { os: "iOS", icon: "", ext: ".ipa", label: "Download .ipa", href: `${RELEASES}` },
      { os: "Android", icon: "🤖", ext: ".apk", label: "Download .apk", href: `${RELEASES}` },
    ],
    buildCmd: "cd desktop-apps/react-native && npm install && eas build --platform all",
    tag: "React Native",
    tagClass: "tag-purple",
  },
  {
    name: "Hermes for iOS/macOS",
    framework: "SwiftUI",
    icon: "",
    desc: "Native SwiftUI app with streaming. Best performance on Apple platforms.",
    platforms: [
      { os: "macOS", icon: "", ext: ".app", label: "Build in Xcode", href: `${GITHUB}/tree/main/desktop-apps/swift` },
      { os: "iOS", icon: "", ext: ".ipa", label: "Build in Xcode", href: `${GITHUB}/tree/main/desktop-apps/swift` },
    ],
    buildCmd: "# Open Xcode → desktop-apps/swift/HermesChat.swift",
    tag: "Swift",
    tagClass: "tag-yellow",
  },
];

export default function Downloads() {
  return (
    <section id="downloads" className="section" style={{ borderTop: "1px solid var(--border)" }}>
      <div className="container">
        <div style={{ marginBottom: 48 }}>
          <div className="section-label">Download</div>
          <h2 className="section-title">Desktop & mobile apps</h2>
          <p className="section-sub">
            Pre-built binaries from GitHub Releases, or build from source in one command.
          </p>
        </div>

        {/* GitHub release banner */}
        <a href={RELEASES} target="_blank" rel="noopener" style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          padding: "16px 24px", borderRadius: "var(--radius)",
          background: "linear-gradient(135deg, rgba(79,110,247,0.12) 0%, rgba(167,139,250,0.08) 100%)",
          border: "1px solid rgba(79,110,247,0.3)", marginBottom: 32,
          textDecoration: "none", transition: "border-color 0.15s",
        }}
        onMouseEnter={e => e.currentTarget.style.borderColor = "rgba(79,110,247,0.6)"}
        onMouseLeave={e => e.currentTarget.style.borderColor = "rgba(79,110,247,0.3)"}
        >
          <div>
            <div style={{ fontWeight: 700, color: "var(--text)", marginBottom: 4 }}>
              Latest Release on GitHub
            </div>
            <div style={{ fontSize: 13, color: "var(--text2)" }}>
              All platform binaries — .exe, .dmg, .AppImage, .apk, .ipa — in one GitHub Release
            </div>
          </div>
          <span style={{ fontSize: 20 }}>→</span>
        </a>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(320px, 1fr))", gap: 20 }}>
          {apps.map(app => (
            <div key={app.name} className="card" style={{ display: "flex", flexDirection: "column", gap: 16 }}>
              <div style={{ display: "flex", alignItems: "flex-start", justifyContent: "space-between" }}>
                <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                  <span style={{ fontSize: 28 }}>{app.icon}</span>
                  <div>
                    <div style={{ fontWeight: 700, fontSize: 15 }}>{app.name}</div>
                    <div style={{ fontSize: 12, color: "var(--text3)" }}>{app.framework}</div>
                  </div>
                </div>
                <span className={`tag ${app.tagClass}`}>{app.tag}</span>
              </div>

              <p style={{ fontSize: 13, color: "var(--text2)", lineHeight: 1.6 }}>{app.desc}</p>

              <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                {app.platforms.map(p => (
                  <a key={p.os} href={p.href} target="_blank" rel="noopener"
                    className="btn btn-secondary"
                    style={{ justifyContent: "space-between", padding: "10px 16px", fontSize: 13 }}
                  >
                    <span>{p.icon} {p.os}</span>
                    <span style={{ color: "var(--text3)", fontFamily: "monospace", fontSize: 12 }}>{p.ext}</span>
                  </a>
                ))}
              </div>

              <div style={{ borderTop: "1px solid var(--border)", paddingTop: 12 }}>
                <div style={{ fontSize: 11, color: "var(--text3)", marginBottom: 6, fontWeight: 700, letterSpacing: "0.05em" }}>BUILD FROM SOURCE</div>
                <div className="code-block mono" style={{ fontSize: 12, padding: "10px 14px" }}>
                  {app.buildCmd}
                </div>
              </div>
            </div>
          ))}
        </div>

        {/* Build your own CTA */}
        <div style={{
          marginTop: 40, padding: "32px", borderRadius: "var(--radius)",
          background: "var(--bg2)", border: "1px solid var(--border)", textAlign: "center",
        }}>
          <div style={{ fontSize: 24, marginBottom: 12 }}>🚀</div>
          <h3 style={{ fontWeight: 700, fontSize: 18, marginBottom: 8 }}>Build & release your own</h3>
          <p style={{ color: "var(--text2)", fontSize: 14, marginBottom: 20, maxWidth: 480, margin: "0 auto 20px" }}>
            Push a git tag to trigger GitHub Actions — automatically builds .exe, .dmg, .AppImage, .apk, and .ipa and publishes a GitHub Release.
          </p>
          <div className="code-block mono" style={{ maxWidth: 360, margin: "0 auto 20px", fontSize: 13 }}>
            git tag v1.0.0 && git push --tags
          </div>
          <a href={`${GITHUB}/tree/main/pipelines`} target="_blank" rel="noopener" className="btn btn-secondary">
            View CI/CD pipelines →
          </a>
        </div>
      </div>
    </section>
  );
}
