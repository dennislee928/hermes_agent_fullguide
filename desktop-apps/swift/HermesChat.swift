/**
 * Hermes Chat — SwiftUI app for macOS and iOS
 * Connects to a local Ollama server with streaming support.
 *
 * Add this file to a new SwiftUI project. Set Info.plist:
 *   NSAppTransportSecurity → NSAllowsLocalNetworking → YES
 */

import SwiftUI

let ollamaHost = ProcessInfo.processInfo.environment["OLLAMA_HOST"] ?? "localhost"
let ollamaURL = URL(string: "http://\(ollamaHost):11434/api/chat")!
let model = "hf.co/NousResearch/Hermes-3-Llama-3.1-8B-GGUF"

struct ChatMessage: Identifiable {
    let id = UUID()
    let role: String
    var content: String
}

@MainActor
class ChatVM: ObservableObject {
    @Published var messages: [ChatMessage] = []
    @Published var input = ""
    @Published var isLoading = false

    private var history: [[String: String]] = [
        ["role": "system", "content": "You are Hermes, a helpful AI assistant."]
    ]

    func send() async {
        let text = input.trimmingCharacters(in: .whitespaces)
        guard !text.isEmpty, !isLoading else { return }

        input = ""
        isLoading = true
        messages.append(ChatMessage(role: "user", content: text))
        history.append(["role": "user", "content": text])

        let assistantIdx = messages.count
        messages.append(ChatMessage(role: "assistant", content: ""))

        do {
            let body: [String: Any] = ["model": model, "messages": history, "stream": true]
            var request = URLRequest(url: ollamaURL)
            request.httpMethod = "POST"
            request.httpBody = try JSONSerialization.data(withJSONObject: body)
            request.setValue("application/json", forHTTPHeaderField: "Content-Type")

            let (stream, _) = try await URLSession.shared.bytes(for: request)
            var fullReply = ""

            for try await line in stream.lines {
                guard let data = line.data(using: .utf8),
                      let json = try? JSONSerialization.jsonObject(with: data) as? [String: Any],
                      let msg = json["message"] as? [String: Any],
                      let token = msg["content"] as? String else { continue }
                fullReply += token
                messages[assistantIdx].content = fullReply
            }

            history.append(["role": "assistant", "content": fullReply])
        } catch {
            messages[assistantIdx].content = "Error: \(error.localizedDescription)"
        }

        isLoading = false
    }
}

struct ContentView: View {
    @StateObject private var vm = ChatVM()

    var body: some View {
        VStack(spacing: 0) {
            ScrollViewReader { proxy in
                ScrollView {
                    LazyVStack(alignment: .leading, spacing: 12) {
                        ForEach(vm.messages) { msg in
                            HStack {
                                if msg.role == "user" { Spacer() }
                                Text(msg.content)
                                    .padding(12)
                                    .background(msg.role == "user" ? Color.blue : Color(white: 0.15))
                                    .foregroundColor(.white)
                                    .cornerRadius(14)
                                    .frame(maxWidth: 320, alignment: msg.role == "user" ? .trailing : .leading)
                                if msg.role == "assistant" { Spacer() }
                            }
                            .id(msg.id)
                        }
                    }
                    .padding()
                }
                .onChange(of: vm.messages.count) { _ in
                    if let last = vm.messages.last { proxy.scrollTo(last.id, anchor: .bottom) }
                }
            }

            Divider()

            HStack(spacing: 10) {
                TextField("Message Hermes...", text: $vm.input, axis: .vertical)
                    .lineLimit(1...4)
                    .textFieldStyle(.roundedBorder)
                    .onSubmit { Task { await vm.send() } }

                Button {
                    Task { await vm.send() }
                } label: {
                    Image(systemName: "arrow.up.circle.fill")
                        .font(.system(size: 28))
                        .foregroundColor(vm.isLoading ? .gray : .blue)
                }
                .disabled(vm.isLoading)
                .buttonStyle(.plain)
            }
            .padding()
            .background(Color(white: 0.1))
        }
        .background(Color(white: 0.12))
        .preferredColorScheme(.dark)
        .navigationTitle("Hermes")
    }
}

@main
struct HermesApp: App {
    var body: some Scene {
        WindowGroup {
            NavigationStack { ContentView() }
        }
    }
}
