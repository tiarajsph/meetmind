from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.vector_store import search

router = APIRouter()

class ChatRequest(BaseModel):
    query: str


KEYWORDS = ["send", "schedule", "review", "compile", "prepare"]

import re

def extract_answer(query, chunks):
    query = query.lower()

    keyword_map = {
        "send": ["send"],
        "review": ["review"],
        "compile": ["compile"],
        "schedule": ["schedule"],
        "prepare": ["prepare"]
    }

    target_keywords = []
    for key, vals in keyword_map.items():
        if key in query:
            target_keywords = vals
            break

    if not target_keywords:
        return "I don't know", []

    matches = []

    for chunk in chunks:
        # 🔥 split using SPEAKER PATTERN instead of newline
        lines = re.split(r'(?=[A-Z][a-z]+:)', chunk)

        for line in lines:
            if ":" not in line:
                continue

            speaker, text = line.split(":", 1)
            text_lower = text.lower()

            if any(k in text_lower for k in target_keywords):
                if "will" in text_lower or "i'll" in text_lower:
                    matches.append((speaker.strip(), line.strip()))

    if not matches:
       return "Not found in the transcript", ["No relevant evidence found"]

    return matches[0][0], [matches[0][1]]

@router.post("/chat")
def chat(req: ChatRequest):
    query = req.query

    # 🔍 retrieve chunks
    retrieved_chunks = search(query)

    # ❗ remove duplicates (important)
    retrieved_chunks = list(set(retrieved_chunks))

    # 🧠 extract answer
    answer, sources = extract_answer(query, retrieved_chunks)

    return {
        "answer": answer,
        "sources": sources
    }