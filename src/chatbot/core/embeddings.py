from langchain_huggingface import HuggingFaceEmbeddings
from ..utils import setup_logging

logger = setup_logging()

DEFAULT_EMBEDDINGS_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

def hf_embeddings(model_name: str = None):
    model_name = model_name or DEFAULT_EMBEDDINGS_MODEL
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name,
        model_kwargs = {"device": "cpu"},
        encode_kwargs = {"normalize_embeddings": True},
    )
    print("Hugging Face Embeddings loaded")
    logger.info(f"HuggingFace Embeddings loaded : {model_name}")
    return embeddings