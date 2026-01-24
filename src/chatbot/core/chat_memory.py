from typing import Dict, Optional
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

class ConversationMemoryManager:
    def __init__(self):
        self._store: Dict[str, BaseChatMessageHistory] = {}

    def get_session_history(self, session_id: str) -> BaseChatMessageHistory:
        if session_id not in self._store:
            self._store[session_id] = ChatMessageHistory()
        return self._store[session_id]

    def get_history(self, session_id: str) -> Optional[BaseChatMessageHistory]:
        return self._store.get(session_id)

    def clear_session(self, session_id: str) -> None:
        self._store.pop(session_id, None)

    def create_runnable_with_memory(self, chain, input_messages_key="input", history_key="history"):
        return RunnableWithMessageHistory(
            chain,
            self.get_session_history,
            input_messages_key=input_messages_key,
            history_messages_key=history_key,
        )

memory_manager = ConversationMemoryManager()