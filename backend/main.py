from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes.upload import router as upload_router
from backend.routes import chat

app = FastAPI()

# ✅ CORS CONFIG (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for dev; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROUTES
app.include_router(upload_router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "MeetMind API Running"}