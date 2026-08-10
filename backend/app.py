from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import logging
import time

from chatbot import ask_gemini


# ---------------- LOGGING ----------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ---------------- FASTAPI ----------------

app = FastAPI(
    title="STAR Assurances AI API",
    description="REST API for STAR Assurances AI Assistant",
    version="1.0.0"
)


# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- MODELS ----------------

class ChatRequest(BaseModel):
    message: str
    language: str = "fr"


class ChatResponse(BaseModel):
    success: bool
    response: str


# ---------------- ROUTES ----------------

@app.get("/")
def home():
    return {
        "success": True,
        "message": "STAR Assurances AI API is running."
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    message = request.message.strip()

    if not message:
        raise HTTPException(
            status_code=400,
            detail="Veuillez saisir un message."
        )

    if request.language not in ["fr", "ar", "en"]:
        raise HTTPException(
            status_code=400,
            detail="Unsupported language."
        )

    logger.info(f"Question: {message}")
    start_time = time.time()

    try:
        response = ask_gemini(
            message=message,
            language=request.language
        )

        execution_time = round(time.time() - start_time, 2)
        logger.info(f"Response generated in {execution_time} sec")

        return ChatResponse(
            success=True,
            response=response
        )

    except Exception as e:
        logger.exception("Erreur lors de l'appel à Gemini")
        # Directement à l'intérieur du bloc except
        raise HTTPException(
            status_code=500,
            detail=f"Erreur interne : {str(e)}"
        )