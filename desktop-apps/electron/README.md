# Hermes Electron App

Cross-platform desktop chat app (Windows `.exe`, macOS `.dmg`, Linux `.AppImage`).

## Dev

```bash
npm install
npm start
```

Requires Ollama running on `localhost:11434`.

## Build distributables

```bash
npm run build:win    # → dist/*.exe
npm run build:mac    # → dist/*.dmg
npm run build:linux  # → dist/*.AppImage
```

## CI

See [../../pipelines/github-actions/build-electron.yml](../../pipelines/github-actions/build-electron.yml).
Push a tag (`v1.0.0`) to trigger a GitHub Release with all three binaries.
