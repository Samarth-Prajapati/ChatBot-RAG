from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chatbot_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a friendly and helpful assistant. "
    )),
    MessagesPlaceholder(variable_name = "history"),
    ("human", "{input}")
])

rag_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a friendly and helpful assistant.\n"
        "Use the following pieces of context to answer the question. "
        "If you don't know the answer, just say you don't know.\n\n"
        "{context}"
    )),
    ("placeholder", "{history}"),
    ("human", "{question}")
])