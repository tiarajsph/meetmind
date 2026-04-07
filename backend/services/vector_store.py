import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

index = None
chunk_store = []


def build_index(chunks):
    global index, chunk_store

    if not chunks:
        return

    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    chunk_store = chunks


def search(query, top_k=3):
    global index, chunk_store

    if index is None:
        return []

    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)

    seen = set()
    results = []

    for i in indices[0]:
        if i < len(chunk_store):
            text = chunk_store[i]["text"]
            if text not in seen:
                results.append(text)
                seen.add(text)

    return results