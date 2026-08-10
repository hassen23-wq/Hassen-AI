import logging
import time
from collections import deque
from functools import lru_cache

from google import genai

from config import GEMINI_API_KEY
from prompt import get_system_prompt
from rag_engine import retrieve_context


# ---------------- LOGGING ----------------

logger = logging.getLogger(__name__)


# ---------------- GEMINI CLIENT ----------------

client = genai.Client(
    api_key=GEMINI_API_KEY
)


# ---------------- CHAT HISTORY ----------------

# Keep only the last 10 messages
chat_history = deque(maxlen=10)


# ---------------- RAG CACHE ----------------

@lru_cache(maxsize=100)
def get_context(query: str):
    return retrieve_context(query)


# ---------------- CHATBOT ----------------

def ask_gemini(message: str, language: str = "fr"):

    start_time = time.time()

    # Retrieve relevant STAR documentation
    context = get_context(message)

    # Save user message
    chat_history.append(
        f"Client: {message}"
    )

    conversation = "\n".join(chat_history)

    prompt = f"""
{get_system_prompt()}

=====================
LANGUAGE
=====================

{language}

=====================
STAR DOCUMENTATION
=====================

{context}

=====================
CONVERSATION
=====================

{conversation}

=====================
QUESTION
=====================

{message}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    reply = response.text.strip() if response.text else (
        "Je suis désolé, je ne peux pas répondre à cette question avec les informations disponibles."
    )

    # Save assistant response
    chat_history.append(
        f"Assistant: {reply}"
    )

    execution_time = round(
        time.time() - start_time,
        2
    )

    logger.info(
        f"Gemini response generated in {execution_time} sec"
    )

    return reply