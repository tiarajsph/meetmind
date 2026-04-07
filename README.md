# 🧠 MeetMind

**Turning Conversations into Actionable Intelligence**

---

## 📌 The Problem

Meetings often generate large volumes of unstructured conversation, making it difficult to track responsibilities, action items, and deadlines. As a result, important tasks are missed, ownership becomes unclear, and productivity drops.

---

## 💡 The Solution

MeetMind is an AI-powered system that transforms meeting transcripts into actionable insights.

It allows users to:

* Upload meeting transcripts
* Extract actionable tasks (who, what)
* Ask questions about the meeting
* Receive **accurate, source-backed answers**

Instead of relying fully on LLM-generated responses, MeetMind uses a **retrieval-first approach** to ensure answers are grounded in actual transcript data, minimizing hallucinations.

---

## ⚙️ Tech Stack

### Languages

* Python
* JavaScript
* HTML/CSS

### Backend

* FastAPI

### AI / ML

* Sentence Transformers (`all-MiniLM-L6-v2`)
* FAISS (vector similarity search)
* Ollama (TinyLlama for extraction)

### Frontend

* Vanilla HTML, CSS, JavaScript

---

## 🛠 Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/meetmind.git
cd meetmind
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv
```

Activate virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Run Backend

```bash
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 4. Run Frontend

```bash
cd frontend
python -m http.server 5500
```

Open in browser:

```
http://localhost:5500
```

---

## 🎥 Demo

https://drive.google.com/file/d/1jZ3EE7wMbybyvxiW55ueauuFUxwxiPbu/view?usp=sharing

---

## 🚀 Features

* 📄 Upload meeting transcripts
* 🔍 Semantic search using FAISS
* 💬 Chat-based querying over transcripts
* 🧠 Action extraction from conversations
* 📌 Source-backed answers (anti-hallucination)
* ⚡ Fast local AI processing

---

## 🔒 Design Philosophy

MeetMind is built with a strong focus on **accuracy and trust**.

Instead of depending entirely on LLM-generated answers:

* Retrieval is used to find relevant context
* Answers are extracted deterministically
* Every response is backed by source evidence

This ensures:

* Reduced hallucination
* Transparent reasoning
* Reliable outputs

---

## 🌟 Future Improvements

* Structured JSON-based action item extraction
* Support for multiple meetings
* Enhanced UI with highlighted evidence
* Deployment (Vercel + Render)

---

## 📦 Repository Structure

```
meetmind/
├── backend/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── main.py
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
```

---

## 🙌 Conclusion

MeetMind bridges the gap between conversations and execution by turning raw meeting discussions into clear, actionable intelligence—while ensuring reliability through grounded AI.
