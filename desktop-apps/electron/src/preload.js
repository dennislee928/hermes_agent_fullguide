const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("hermes", {
  chat: (model, messages) => ipcRenderer.invoke("chat", { model, messages }),
  listModels: () => ipcRenderer.invoke("list-models"),
});
