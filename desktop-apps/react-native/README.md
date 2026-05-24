# Hermes Mobile (React Native / Expo)

iOS + Android chat app that connects to a local Ollama server.

## Setup

```bash
npm install
```

Set your machine's local IP in `.env`:
```
EXPO_PUBLIC_OLLAMA_HOST=192.168.1.100
```

## Run

```bash
npx expo start       # Expo Go (dev)
npx expo run:ios     # iOS simulator
npx expo run:android # Android emulator
```

## Build for distribution (EAS)

```bash
npm install -g eas-cli
eas login
eas build --platform android   # → .apk / .aab
eas build --platform ios       # → .ipa (needs Apple Dev account)
```

## CI

See [../../pipelines/github-actions/build-react-native.yml](../../pipelines/github-actions/build-react-native.yml).
Requires `EXPO_TOKEN` secret in GitHub repository settings.
