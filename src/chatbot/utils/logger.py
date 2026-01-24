import logging
from pathlib import Path

def setup_logging():
    log_path = Path(__file__).resolve().parents[2] / "project_logs/chatbot_rag.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s - %(levelname)s - %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        filename = str(log_path),
        filemode = "a"
    )
    return logging.getLogger(__name__)