const BASE_URL = "http://127.0.0.1:8000";

function addMessage(text, type, sources = []) {
  const chat = document.getElementById("chatContainer");

  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", type);
  msgDiv.innerText = text;

  if (type === "bot" && sources.length > 0) {
    const srcDiv = document.createElement("div");
    srcDiv.classList.add("sources");
    srcDiv.innerText = "Sources:\n" + sources.join("\n");
    msgDiv.appendChild(srcDiv);
  }

  chat.appendChild(msgDiv);
  chat.scrollTop = chat.scrollHeight;
}

async function uploadFile() {
  const file = document.getElementById("fileInput").files[0];
  if (!file) return alert("Select a file");

  const formData = new FormData();
  formData.append("file", file);

  document.getElementById("uploadStatus").innerText = "Uploading...";

  try {
    await fetch(`${BASE_URL}/upload`, {
      method: "POST",
      body: formData
    });

    document.getElementById("uploadStatus").innerText = "✅ Uploaded";
  } catch {
    document.getElementById("uploadStatus").innerText = "❌ Failed";
  }
}

async function askQuestion() {
  const queryBox = document.getElementById("query");
  const query = queryBox.value.trim();
  if (!query) return;

  addMessage(query, "user");
  queryBox.value = "";

  addMessage("Thinking...", "bot");

  try {
    const res = await fetch(`${BASE_URL}/chat`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });

    const data = await res.json();

    document.getElementById("chatContainer").lastChild.remove();
    addMessage(data.answer, "bot", data.sources);

  } catch {
    document.getElementById("chatContainer").lastChild.remove();
    addMessage("Error fetching response", "bot");
  }
}

document.getElementById("query").addEventListener("keydown", function(e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();
    askQuestion();
  }
});