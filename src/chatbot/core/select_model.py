from ..utils import setup_logging
from ..config import AVAILABLE_MODELS

class SelectModel:
    def __init__(self):
        self.model = None
        self.logger = setup_logging()

    def select_model(self):
        self.logger.info("Available models : ")
        for idx, model in enumerate(AVAILABLE_MODELS, start=1):
            print(f"{idx}. {model}")

        while True:
            try:
                choice = int(input("Select a model (enter number) : "))
                if 1 <= choice <= len(AVAILABLE_MODELS):
                    self.model = AVAILABLE_MODELS[choice - 1]
                    self.logger.info(f"Selected model : {self.model}")
                    print(f"Selected model : {self.model}")
                    return self.model
                else:
                    self.logger.warning("Invalid choice. Please select a valid number.")
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                self.logger.error("Please enter a valid number.")
                print("Please enter a valid number.")
