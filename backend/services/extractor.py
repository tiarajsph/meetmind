import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def query_llm(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "tinyllama",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


def safe_parse(response: str):
    try:
        return json.loads(response)
    except:
        return []


def extract_actions(chunk_text: str):
    prompt = f"""
Extract action items.

Return JSON:
[
  {{
    "person": "...",
    "task": "...",
    "deadline": "..."
  }}
]

Text:
{chunk_text}
"""

    llm_output = query_llm(prompt)
    return safe_parse(llm_output)