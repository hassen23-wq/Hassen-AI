import os

from dotenv import load_dotenv



# =========================
# Load Environment
# =========================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


ENV_PATH = os.path.join(
    BASE_DIR,
    ".env"
)


load_dotenv(
    ENV_PATH
)



# =========================
# Configuration
# =========================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)


GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)


ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development"
)



DEBUG = os.getenv(
    "DEBUG",
    "false"
).lower() == "true"



# =========================
# Validation
# =========================

def validate_config():


    if not GEMINI_API_KEY:

        raise ValueError(
            """
GEMINI_API_KEY is missing.

Please add it to your .env file:
GEMINI_API_KEY=your_api_key_here
"""
        )



validate_config()