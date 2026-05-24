 ---
  Repo Plan: hermes_agent_fullguide

  Structure

  hermes_agent_fullguide/
  ├── README.md                          # Overview + quick-start
  │
  ├── docs/setup/                        # OS-specific install guides
  │   ├── macos.md                       # Homebrew + Ollama + LM Studio
  │   ├── windows.md                     # winget/scoop + Ollama + LM Studio
  │   ├── linux.md                       # apt/pacman + Ollama + Docker
  │   ├── ios.md                         # Offline via LLM Farm / server-mode
  │   └── android.md                     # MLC-LLM / server-mode
  │
  ├── docs/use-cases/                    # Real use cases with working code
  │   ├── local-chatbot.md
  │   ├── rag-pipeline.md
  │   ├── code-assistant.md
  │   ├── document-qa.md
  │   ├── function-calling.md
  │   └── autonomous-agent.md
  │
  ├── scripts/setup/                     # One-command installers
  │   ├── install_macos.sh
  │   ├── install_windows.ps1
  │   ├── install_linux.sh
  │   └── check_gpu.sh                   # CUDA/Metal/ROCm detection
  │
  ├── examples/                          # Runnable code per use case
  ├── examples/                          # Runnable code per use case
  │   ├── basic-chat/python/
  │   ├── basic-chat/typescript/
  │   ├── rag/                           # LangChain + ChromaDB
  │   ├── function-calling/              # Tool use with Hermes
  │   ├── rag/                           # LangChain + ChromaDB
  │   ├── function-calling/              # Tool use with Hermes
  │   ├── agent-loop/                    # ReAct-style agent
  │   └── streaming/
  │
  ├── configs/
  │   ├── function-calling/              # Tool use with Hermes
  │   ├── agent-loop/                    # ReAct-style agent
  │   └── streaming/
  │
  ├── configs/
  │   ├── Modelfile.hermes3              # Ollama Modelfile
  │   ├── docker-compose.yml             # Ollama server + UI
  │   └── system-prompts/               # Hermes-specific prompt templates
  ├── configs/
  │   ├── Modelfile.hermes3              # Ollama Modelfile
  │   ├── docker-compose.yml             # Ollama server + UI
  │   └── system-prompts/               # Hermes-specific prompt templates
  │
  ├── desktop-apps/
  │   ├── electron/                      # Windows + Mac + Linux
  │   ├── tauri/                         # Windows + Mac + Linux (lighter)
  │   ├── react-native/                  # iOS + Android
  │   └── swift/                         # macOS + iOS native
  │
  ├── desktop-apps/
  │   ├── electron/                      # Windows + Mac + Linux
  │   ├── tauri/                         # Windows + Mac + Linux (lighter)
  │   ├── react-native/                  # iOS + Android
  │   └── swift/                         # macOS + iOS native
  │
  └── pipelines/
      ├── github-actions/
  │   ├── tauri/                         # Windows + Mac + Linux (lighter)
  │   ├── react-native/                  # iOS + Android
  │   └── swift/                         # macOS + iOS native
  │
  └── pipelines/
      ├── github-actions/
      │   ├── build-electron.yml         # Artifacts: .exe, .dmg, .AppImage
      │   ├── build-electron.yml         # Artifacts: .exe, .dmg, .AppImage
      │   ├── build-tauri.yml            # Artifacts: .exe, .dmg, .deb
      │   ├── build-tauri.yml            # Artifacts: .exe, .dmg, .deb
      │   └── build-react-native.yml    # .ipa + .apk via EAS
      │   └── build-react-native.yml    # .ipa + .apk via EAS
      └── docker/
      └── docker/
          └── Dockerfile.server          # Portable Ollama server image

  ---
  Phase breakdown
  │   ├── document-qa.md
  │   ├── function-calling.md
  │   └── autonomous-agent.md
  │
  ├── scripts/setup/                     # One-command installers
  │   ├── install_macos.sh
  │   ├── install_windows.ps1
  │   ├── install_linux.sh
  │   └── check_gpu.sh                   # CUDA/Metal/ROCm detection
  │
  ├── examples/                          # Runnable code per use case
  │   ├── basic-chat/python/
  │   ├── basic-chat/typescript/
  │   ├── rag/                           # LangChain + ChromaDB
  │   ├── function-calling/              # Tool use with Hermes
  │   ├── agent-loop/                    # ReAct-style agent
  │   └── streaming/
  │
  ├── configs/
  │   ├── Modelfile.hermes3              # Ollama Modelfile
  │   ├── docker-compose.yml             # Ollama server + UI
  │   └── system-prompts/               # Hermes-specific prompt templates
  │
  ├── desktop-apps/
  │   ├── electron/                      # Windows + Mac + Linux
  │   ├── tauri/                         # Windows + Mac + Linux (lighter)
  │   ├── react-native/                  # iOS + Android
  │   └── swift/                         # macOS + iOS native
  │
  └── pipelines/
      ├── github-actions/
      │   ├── build-electron.yml         # Artifacts: .exe, .dmg, .AppImage
      │   ├── build-tauri.yml            # Artifacts: .exe, .dmg, .deb
      │   └── build-react-native.yml    # .ipa + .apk via EAS
      └── docker/
          └── Dockerfile.server          # Portable Ollama server image

  ---
  Phase breakdown

  ┌───────┬──────────────────────────────────────────────────────────────┬──────────────────────────────┐
  │ Phase │                           Content                            │         Deliverable          │
  ├───────┼──────────────────────────────────────────────────────────────┼──────────────────────────────┤
  │ 1     │ OS setup guides + one-command scripts                        │ docs/setup/ + scripts/setup/ │
  ├───────┼──────────────────────────────────────────────────────────────┼──────────────────────────────┤
  │ 2     │ Configs (Modelfile, Docker, system prompts)                  │ configs/                     │
  ├───────┼──────────────────────────────────────────────────────────────┼──────────────────────────────┤
  │ 3     │ Use case docs + runnable examples                            │ docs/use-cases/ + examples/  │
  ├───────┼──────────────────────────────────────────────────────────────┼──────────────────────────────┤
  │ 4     │ Desktop app skeletons (Electron, Tauri, React Native, Swift) │ desktop-apps/                │
  ├───────┼──────────────────────────────────────────────────────────────┼──────────────────────────────┤
  │ 5     │ CI/CD pipelines that build distributable binaries            │ pipelines/github-actions/    │
  └───────┴──────────────────────────────────────────────────────────────┴──────────────────────────────┘