import re

def clean_text(text: str) -> str:
    # Remove timestamps [00:12:34]
    text = re.sub(r"\[\d{2}:\d{2}:\d{2}\]", "", text)

    # ❌ DO NOT REMOVE SPEAKER LABELS

    # Remove filler words
    fillers = r"\b(um|uh|like|you know|basically|actually)\b"
    text = re.sub(fillers, "", text, flags=re.IGNORECASE)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()