def chunk_text(text: str, chunk_size=8, overlap=2):
    lines = text.split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    chunks = []
    start = 0
    chunk_id = 0

    while start < len(lines):
        end = start + chunk_size
        chunk_lines = lines[start:end]

        chunk_str = "\n".join(chunk_lines)

        chunks.append({
            "chunk_id": chunk_id,
            "text": chunk_str
        })

        start += chunk_size - overlap
        chunk_id += 1

    return chunks