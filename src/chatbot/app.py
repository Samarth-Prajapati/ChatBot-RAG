from chatbot.core import ChatBot
from chatbot.utils.logger import setup_logging
from chatbot.core import RAG

if __name__ == "__main__":
    logger = setup_logging()
    logger.info('Application started')

    while True:
        print("1. ChatBot\n2. RAG\n3. Exit\n")
        choice = input("Enter your choice : ")

        if choice == "1":
            bot = ChatBot()
            bot.start_conversation()

        elif choice == "2":
            absolute_path = input("Enter the absolute path of the file : ")
            extension = input("\nEnter the extension of the file : ")
            bot = RAG()
            bot.start_conversation(absolute_path, extension.lower())

        elif choice == "3":
            print("Thank you for using this application")
            break

        else:
            print("Invalid choice")

    # bot = RAG()
    # bot.start_conversation("/Users/samarth/Desktop/Projects/ChatBot+RAG/ChatBot/testing_documents/Resume_Samarth.pdf", "pdf")

    logger.info('Application finished')