const { app, BrowserWindow, ipcMain } = require("electron");
const path = require("path");
const http = require("http");

const OLLAMA_HOST = process.env.OLLAMA_HOST || "localhost";
const OLLAMA_PORT = 11434;

function createWindow() {
  const win = new BrowserWindow({
    width: 900,
    height: 700,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
      contextIsolation: true,
    },
    titleBarStyle: "hiddenInset",
  });

  win.loadFile(path.join(__dirname, "index.html"));
}

ipcMain.handle("chat", async (_, { model, messages }) => {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ model, messages, stream: false });
    const req = http.request(
      { host: OLLAMA_HOST, port: OLLAMA_PORT, path: "/api/chat", method: "POST",
        headers: { "Content-Type": "application/json", "Content-Length": Buffer.byteLength(body) } },
      (res) => {
        let data = "";
        res.on("data", (chunk) => (data += chunk));
        res.on("end", () => resolve(JSON.parse(data).message.content));
      }
    );
    req.on("error", reject);
    req.write(body);
    req.end();
  });
});

ipcMain.handle("list-models", async () => {
  return new Promise((resolve, reject) => {
    http.get(`http://${OLLAMA_HOST}:${OLLAMA_PORT}/api/tags`, (res) => {
      let data = "";
      res.on("data", (c) => (data += c));
      res.on("end", () => resolve(JSON.parse(data).models?.map((m) => m.name) ?? []));
    }).on("error", reject);
  });
});

app.whenReady().then(createWindow);
app.on("window-all-closed", () => { if (process.platform !== "darwin") app.quit(); });
app.on("activate", () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });
