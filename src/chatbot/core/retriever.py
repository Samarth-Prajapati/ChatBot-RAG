from langchain_community.vectorstores import Chroma
from ..utils import setup_logging

logger = setup_logging()

default_k = 6
default_search_type = "similarity"

def get_retriever(
    vector_db: Chroma,
    k: int = default_k,
    search_type: str = default_search_type,
):
    print(f"Retrieving retriever : {search_type}")
    logger.info(f"Retrieving retriever : {search_type}")
    return vector_db.as_retriever(
        search_type = search_type,
        search_kwargs = {"k": k}
    )