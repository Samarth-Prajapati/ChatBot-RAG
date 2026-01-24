from chatbot.core import ChatBot
from chatbot.utils.logger import setup_logging

if __name__ == "__main__":
    logger = setup_logging()
    logger.info('Application started')
    bot = ChatBot()
    bot.start_conversation()