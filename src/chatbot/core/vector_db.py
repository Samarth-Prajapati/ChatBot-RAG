from pathlib import Path
from typing import List, Optional
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from ..utils import setup_logging

logger = setup_logging()

base_dir = Path(__file__).parent.parent
chroma_persist_dir = base_dir / "vectordb" / "chroma_db"

def get_or_create_chroma(
    docs: Optional[List[Document]] = None,
    embedding: Embeddings = None,
    collection_name: str = "default_rag_collection",
    persist_dir: Path = chroma_persist_dir,
) -> Chroma:

    persist_dir.mkdir(parents = True, exist_ok = True)

    if docs and embedding:
        vector_db = Chroma.from_documents(
            documents = docs,
            embedding = embedding,
            collection_name = collection_name,
            persist_directory = str(persist_dir),
        )
        logger.info("New chroma vector db")
        print("New chroma vector db")

    else:
        vector_db = Chroma(
            collection_name = collection_name,
            embedding_function = embedding,
            persist_directory = str(persist_dir),
        )
        logger.info("Existing chroma vector db")
        print("Existing chroma vector db")

    return vector_db