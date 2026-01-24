from ..config import GROQ_API_KEY
from ..utils import setup_logging
from .select_model import SelectModel
from langchain_groq import ChatGroq
from .chat_memory import memory_manager
from .prompts import chatbot_prompt

class ChatBot:
    def __init__(self):
        self.logger = setup_logging()
        self.logger.info("ChatBot initialized.")
        self.model = SelectModel().select_model()
        self.prompt = chatbot_prompt

    def generate_response(self, user_input: str, session_id: str = "default") -> str:
        if not self.model:
            self.logger.error("Model not selected.")
            raise ValueError("Model not selected.")

        self.logger.info(f"[{session_id}], User input : {user_input}")

        try:
            llm = ChatGroq(
                api_key = GROQ_API_KEY,
                model = self.model,
                temperature = 0.7,
                max_tokens = 1024,
            )

            chain = self.prompt | llm

            conversation_chain = memory_manager.create_runnable_with_memory(
                chain,
                input_messages_key="input",
                history_key="history"
            )

            response = conversation_chain.invoke(
                {
                    "input": user_input,
                },
                config={"configurable": {"session_id": session_id}}
            )

            assistant_reply = response.content
            self.logger.info(f"Assistant response : {assistant_reply}")
            return assistant_reply

        except Exception as e:
            self.logger.error(f"Error generating response : {str(e)}")
            return "Sorry, an error occurred. Please try again."

    def start_conversation(self):
        print("\nChatBot : Hello! Let's chat. Type 'exit' to end the conversation.\n")

        session_id = "default"

        while True:
            try:
                user_input = input("You : ")
                if user_input.lower() == 'exit':
                    self.logger.info(f"[{session_id}], Conversation ended.")
                    print("Conversation ended.")
                    break

                response = self.generate_response(
                    user_input=user_input,
                    session_id=session_id
                )
                print(f"\nChatBot : {response}\n")

            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                self.logger.error(f"Keyboard Interrupted!")
                break

            except Exception as e:
                print(f"\nError: {e}")
                self.logger.error(f"Error : {str(e)}")
