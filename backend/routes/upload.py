from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from backend.utils.text_cleaner import clean_text
from backend.utils.chunker import chunk_text
from backend.services.extractor import extract_actions
from backend.services.vector_store import build_index

router = APIRouter()

UPLOAD_DIR = "data/transcripts"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # 1. Validate file type
    if not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .txt files supported")

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # 2. Read file content
    content = await file.read()

    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="File must be UTF-8 encoded")

    # 3. Save original file
    with open(file_path, "wb") as f:
        f.write(content)

    # 4. Clean text
    cleaned_text = clean_text(text)

    # 5. Chunk text
    chunks = chunk_text(cleaned_text)

    # 🚨 6. BUILD VECTOR INDEX (THIS WAS MISSING)
    build_index(chunks)

    # 7. Extract actions
    all_actions = []

    for chunk in chunks:
        try:
            result = extract_actions(chunk["text"])
        except Exception as e:
            result = f"Error: {str(e)}"

        all_actions.append({
            "chunk_id": chunk["chunk_id"],
            "actions": result
        })

    # 8. Return response
    return {
        "filename": file.filename,
        "num_chunks": len(chunks),
        "preview_chunk": chunks[0] if chunks else None,
        "preview_actions": all_actions[:2],
        "all_actions": all_actions
    }