from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader, TextLoader, CSVLoader, JSONLoader,
    UnstructuredPowerPointLoader, UnstructuredExcelLoader,
    UnstructuredMarkdownLoader, UnstructuredHTMLLoader, UnstructuredXMLLoader,
)
from ..utils import setup_logging

logger = setup_logging()

supported_file_loaders = {
    "pdf":   "PyPDFLoader",
    "docx":  "Docx2txtLoader",
    "pptx":  "UnstructuredPowerPointLoader",
    "xlsx":  "UnstructuredExcelLoader",
    "txt":   "TextLoader",
    "md":    "UnstructuredMarkdownLoader",
    "html":  "UnstructuredHTMLLoader",
    "csv":   "CSVLoader",
    "json":  "JSONLoader",
    "xml":   "UnstructuredXMLLoader"
}

chunk_size = 1000
chunk_overlap = 200

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = chunk_size,
    chunk_overlap = chunk_overlap,
    length_function = len,
    add_start_index = True,
)

_LOADER_MAP = {
    "pdf":   PyPDFLoader,
    "docx":  Docx2txtLoader,
    "pptx":  UnstructuredPowerPointLoader,
    "xlsx":  UnstructuredExcelLoader,
    "txt":   TextLoader,
    "md":    UnstructuredMarkdownLoader,
    "html":  UnstructuredHTMLLoader,
    "csv":   CSVLoader,
    "json":  JSONLoader,
    "xml":   UnstructuredXMLLoader,
}

def load_and_split(
    source_path: str,
    loader_type: str = None,
    **loader_kwargs
) -> List[Document]:
    if loader_type not in supported_file_loaders:
        logger.error(f"loader_type {loader_type} not supported")
        raise ValueError(f"Unsupported loader : {loader_type}")

    loader_class = _LOADER_MAP[loader_type]
    loader = loader_class(source_path, **loader_kwargs)
    raw_docs = loader.load()

    for doc in raw_docs:
        doc.metadata.update({
            "source": source_path,
            "loader_type": loader_type,
        })

    logger.info(f"Loaded {len(raw_docs)} documents - Data Ingestion Completed")
    print(f"Loaded {len(raw_docs)} documents")
    return text_splitter.split_documents(raw_docs)