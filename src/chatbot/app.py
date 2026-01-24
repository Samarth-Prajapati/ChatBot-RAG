from chatbot.core import ChatBot
from chatbot.utils.logger import setup_logging
from chatbot.core import RAG

if __name__ == "__main__":
    logger = setup_logging()
    logger.info('Application started')

    # bot = ChatBot()
    # bot.start_conversation()

    bot = RAG()
    bot.start_conversation("/Users/samarth/Desktop/Projects/ChatBot+RAG/ChatBot/testing_documents/README.md", "md")
