import os
from dotenv import load_dotenv
from ..utils import setup_logging

load_dotenv()

logger = setup_logging()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    logger.error("GROQ_API_KEY not found in environment variables.")
    raise ValueError("GROQ_API_KEY not found in environment variables.")

LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGCHAIN_TRACING_V2 = os.getenv("LANGCHAIN_TRACING_V2", "false").lower() == "true"
LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "ChatBot_RAG")

if LANGCHAIN_TRACING_V2 and not LANGSMITH_API_KEY:
    logger.warning("LANGSMITH_API_KEY not found in environment variables.")
    print("LANGCHAIN_TRACING_V2 is true but LANGSMITH_API_KEY is missing → tracing disabled.")
