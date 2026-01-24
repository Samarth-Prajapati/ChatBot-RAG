from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chatbot_prompt = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a friendly and helpful assistant. "
    )),
    MessagesPlaceholder(variable_name = "history"),
    ("human", "{input}")
])