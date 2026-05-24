# Hermes Swift App (macOS + iOS)

Native SwiftUI app with streaming responses via Ollama.

## Setup

1. Open Xcode → File → New Project → App (SwiftUI)
2. Replace `ContentView.swift` with `HermesChat.swift`
3. In `Info.plist`, add:
   ```xml
   <key>NSAppTransportSecurity</key>
   <dict>
     <key>NSAllowsLocalNetworking</key>
     <true/>
   </dict>
   ```
4. Set `OLLAMA_HOST` environment variable in the scheme, or hardcode your server IP

## Running

- **macOS**: Run directly in Xcode (⌘R)
- **iOS Simulator**: Select an iPhone target → Run
- **Physical iPhone**: Requires a free or paid Apple Developer account

## Connecting to Ollama

The app connects to `http://$OLLAMA_HOST:11434`. Make sure:
- Ollama is running with `OLLAMA_HOST=0.0.0.0 ollama serve`
- Both devices are on the same Wi-Fi network
- macOS firewall allows port 11434

## Distribution

- **macOS**: Archive in Xcode → Distribute → Developer ID (for notarization)
- **iOS**: Archive → TestFlight or App Store (requires paid Apple Developer account, $99/yr)
