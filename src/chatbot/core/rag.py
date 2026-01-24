from typing import Optional
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from .embeddings import hf_embeddings
from .vector_db import get_or_create_chroma
from .data_ingestion import load_and_split
from .retriever import get_retriever
from .chat_memory import memory_manager
from ..utils import setup_logging
from ..config import GROQ_API_KEY
from .prompts import rag_prompt

logger = setup_logging()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

class RAG:
    def __init__(
        self,
        embeddings_model: Optional[str] = None,
        collection_name: str = "default_rag_collection",
    ):
        self.embeddings = hf_embeddings(embeddings_model)
        self.collection_name = collection_name
        self.vector_db = None
        self.retriever = None
        self.llm = None

    def index_documents(
        self,
        source_path: str,
        loader_type: str,
        **loader_kwargs
    ):
        splits = load_and_split(source_path, loader_type, **loader_kwargs)
        self.vector_db = get_or_create_chroma(
            docs = splits,
            embedding = self.embeddings,
            collection_name = self.collection_name,
        )
        self.retriever = get_retriever(self.vector_db)

    def load_existing_index(self):
        self.vector_db = get_or_create_chroma(
            embedding = self.embeddings,
            collection_name = self.collection_name,
        )
        self.retriever = get_retriever(self.vector_db)

    def _setup_llm(self):
        model_name = "llama-3.3-70b-versatile"
        # if "openai" in model_name.lower():
        #     from langchain_openai import ChatOpenAI
        #     self.llm = ChatOpenAI(model=model_name)
        if model_name:
            self.llm = ChatGroq(
                api_key = GROQ_API_KEY,
                model = model_name,
                temperature = 0.7,
                max_tokens = 2048
            )
            logger.info(f"Using model : {model_name}")
            print(f"Using model : {model_name}")
        else:
            logger.error(f"Model {model_name} not supported")
            raise ValueError(f"Model {model_name} not supported yet in RAG")

    def get_chain(self):
        if not self.llm:
            self._setup_llm()
        if not self.retriever:
            logger.error(f"Retriever {self.retriever} not supported")
            raise ValueError("Index must be loaded first (call load_existing_index or index_documents)")

        rag_chain = (
            {
                "context": lambda x: format_docs(self.retriever.invoke(x["question"])),
                "question": lambda x: x["question"]
            }
            | rag_prompt
            | self.llm
            | StrOutputParser()
        )
        logger.info(f"Chain Created Successfully")

        return memory_manager.create_runnable_with_memory(
            rag_chain,
            input_messages_key = "question",
            history_key = "history",
        )

    def start_conversation(self, source_path: str, loader_type: str):
        self.index_documents(source_path, loader_type)
        while True:
            try:
                user_input = input("You : ")
                if user_input.lower() == 'exit':
                    logger.info(f"Conversation ended.")
                    print("Conversation ended.")
                    break
                chain = self.get_chain()
                response = chain.invoke(
                    {
                        "question": user_input
                    },
                    config = {
                        "configurable": {
                            "session_id": "samarth_session_001"
                        }
                    }
                )
                print(f"\nChatBot : {response}\n")

            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                logger.error(f"Keyboard Interrupted!")
                break

            except Exception as e:
                print(f"\nError: {e}")
                logger.error(f"Error : {str(e)}")
