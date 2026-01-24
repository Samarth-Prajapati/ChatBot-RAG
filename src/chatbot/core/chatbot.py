from ..config import GROQ_API_KEY
from ..utils import setup_logging
from .select_model import SelectModel
from langchain_groq import ChatGroq

class ChatBot:
    def __init__(self):
        self.logger = setup_logging()
        self.logger.info("ChatBot initialized.")
        self.model = SelectModel().select_model()

    def generate_response(self, user_input: str) -> str:
        if not self.model:
            self.logger.error("Model not selected.")
            raise ValueError("Model not selected.")

        self.logger.info(f"User input : {user_input}")

        try:
            response = ChatGroq(
                api_key = GROQ_API_KEY,
                model = self.model,
                temperature = 0.7,
                max_tokens = 1024,
            ).invoke(user_input)
            assistant_reply = response.content
            self.logger.info(f"Assistant response : {assistant_reply}")
            return assistant_reply
        except Exception as e:
            self.logger.error(f"Error generating response : {str(e)}")
            return "Sorry, an error occurred. Please try again."

    def start_conversation(self):
        print("\nChatBot : Hello! Let's chat. Type 'exit' to end the conversation.\n")
        while True:
            user_input = input("You : ")
            if user_input.lower() == 'exit':
                self.logger.info("Conversation ended.")
                print("Conversation ended.")
                break
            response = self.generate_response(user_input)
            print(f"\nChatBot : {response}\n")