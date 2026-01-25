# ChatBot + RAG Project

A Python-based conversational AI system with Retrieval-Augmented Generation (RAG) capabilities, powered by Groq API and LangChain. This is a **command-line interface (CLI) application** with no frontend or GUI.

## Features

- **Interactive ChatBot**: Engage in natural conversations with memory retention across sessions
- **RAG System**: Query and interact with your documents using advanced retrieval techniques
- **Multiple File Format Support**: PDF, DOCX, PPTX, XLSX, TXT, MD, HTML, CSV, JSON, XML
- **Vector Database**: Persistent storage using ChromaDB
- **Conversation Memory**: Session-based chat history management
- **Multiple Model Selection**: Choose from various Groq models
- **Local Embeddings**: HuggingFace embeddings running on CPU
- **CLI-Based**: Pure command-line interface for all interactions

## Project Structure

```
ChatBot/
├── .venv/                          # Virtual environment
├── src/                            # Source code directory
│   ├── chatbot/                    # Chatbot package
│   │   ├── config/                 # Configuration module
│   │   │   ├── __init__.py
│   │   │   ├── models.py           # Available models configuration
│   │   │   └── settings.py         # General settings
│   │   ├── core/                   # Core functionality
│   │   │   ├── __init__.py
│   │   │   ├── chat_memory.py      # Conversation memory management
│   │   │   ├── chatbot.py          # Core chatbot implementation
│   │   │   ├── data_ingestion.py   # Document loading and chunking
│   │   │   ├── embeddings.py       # HuggingFace embeddings setup
│   │   │   ├── prompts.py          # System prompts for chatbot and RAG
│   │   │   ├── rag.py              # RAG system implementation
│   │   │   ├── retriever.py        # Vector database retrieval
│   │   │   ├── select_model.py     # Model selection interface
│   │   │   └── vector_db.py        # ChromaDB vector store management
│   │   ├── utils/                  # Utility functions
│   │   │   ├── __init__.py
│   │   │   └── logger.py           # Logging utilities
│   │   ├── vectordb/               # ChromaDB storage directory
│   │   └── __init__.py
│   └── app.py                      # Main application entry point
├── testing_documents/              # Sample documents for testing
├── tests/                          # Test files
│   └── __init__.py
├── project_logs/                   # Application logs directory
├── .env                            # Environment variables (API keys)
├── .gitignore                      # Git ignore file
├── poetry.lock                     # Poetry lock file
├── pyproject.toml                  # Poetry dependencies and project config
└── README.md                       # This file
```

## Prerequisites

- Python 3.13
- Poetry (for dependency management)
- Groq API Key
- Operating System: Windows, macOS, or Linux

## Installation

### 1. Clone the Repository

**All Platforms:**
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create Virtual Environment

**Windows (Command Prompt):**
```cmd
python -m venv .venv
```

**Windows (PowerShell):**
```powershell
python -m venv .venv
```

**macOS/Linux:**
```bash
python3 -m venv .venv
```

### 3. Activate Virtual Environment

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Using Poetry (Recommended):

**All Platforms:**
```bash
poetry install
```

Or using pip (if you have a requirements.txt):

**All Platforms:**
```bash
pip install -r requirements.txt
```

### 5. Set Up Environment Variables

**Windows (Command Prompt):**
```cmd
set GROQ_API_KEY=your_groq_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

**macOS/Linux:**
```bash
export GROQ_API_KEY=your_groq_api_key_here
```

**Or create a `.env` file (All Platforms):**
```env
GROQ_API_KEY=your_groq_api_key_here
```

## Configuration

Update `config.py` with your available models:

```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

AVAILABLE_MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-70b-versatile",
    "mixtral-8x7b-32768",
    # Add more models as needed
]
```

## Usage

> **Note**: This is a command-line application. All interactions happen in your terminal/command prompt.

### ChatBot Mode (CLI)

For simple conversational AI without document context:

```python
from chatbot import ChatBot

bot = ChatBot()
bot.start_conversation()
```

**Interactive CLI Session:**
```
ChatBot : Hello! Let's chat. Type 'exit' to end the conversation.

You : Hello!
ChatBot : Hi! How can I help you today?

You : What can you do?
ChatBot : I can have conversations with you and remember our chat history!

You : exit
Conversation ended.
```

### RAG Mode (CLI)

For question-answering over your documents:

```python
from rag import RAG

# Initialize RAG
rag = RAG(
    embeddings_model="sentence-transformers/all-MiniLM-L6-v2",
    collection_name="my_documents"
)

# Start conversation with a document
rag.start_conversation(
    source_path="path/to/your/document.pdf",
    loader_type="pdf"
)
```

**Interactive CLI Session:**
```
You : What is this document about?
ChatBot : This document discusses...

You : Can you summarize the main points?
ChatBot : The main points are...

You : exit
Conversation ended.
```

**Programmatic Usage:**

```python
# Index documents
rag.index_documents(
    source_path="document.pdf",
    loader_type="pdf"
)

# Get the chain
chain = rag.get_chain()

# Query the document
response = chain.invoke(
    {"question": "What is this document about?"},
    config={"configurable": {"session_id": "user_123"}}
)
print(response)
```

## Supported File Formats

| Extension | Loader Type | Description |
|-----------|-------------|-------------|
| `.pdf` | `pdf` | PDF documents |
| `.docx` | `docx` | Word documents |
| `.pptx` | `pptx` | PowerPoint presentations |
| `.xlsx` | `xlsx` | Excel spreadsheets |
| `.txt` | `txt` | Plain text files |
| `.md` | `md` | Markdown files |
| `.html` | `html` | HTML files |
| `.csv` | `csv` | CSV files |
| `.json` | `json` | JSON files |
| `.xml` | `xml` | XML files |

## Key Components

### Chat Memory
- Session-based conversation history
- Persistent across multiple interactions
- Easy session management and clearing

### Data Ingestion
- Automatic document loading
- Text chunking (1000 characters with 200 overlap)
- Metadata enrichment

### Embeddings
- Default: `sentence-transformers/all-MiniLM-L6-v2`
- CPU-based computation
- Normalized embeddings for better similarity search

### Vector Database
- ChromaDB for persistent storage
- Collection-based organization
- Automatic directory creation

### Retriever
- Similarity search (default)
- Configurable k value (default: 6)
- Integrated with LangChain

## Configuration Options

### Text Splitting
```python
chunk_size = 1000
chunk_overlap = 200
```

### Retrieval
```python
default_k = 6  # Number of documents to retrieve
default_search_type = "similarity"
```

### LLM Parameters
```python
temperature = 0.7
max_tokens = 1024  # ChatBot
max_tokens = 2048  # RAG
```

## Error Handling

The system includes comprehensive error handling:
- Logging of all operations
- Graceful error messages
- Keyboard interrupt handling (Ctrl+C)
- Validation of inputs

## Logging

Logs are automatically generated for:
- Model selection
- Document loading
- Vector database operations
- User interactions
- Errors and warnings

## Troubleshooting

### Common Issues

**1. Import Errors**

**All Platforms:**
```bash
# Ensure all dependencies are installed
poetry install
```

**2. Groq API Key Not Found**

**Windows (Command Prompt):**
```cmd
echo %GROQ_API_KEY%
```

**Windows (PowerShell):**
```powershell
echo $env:GROQ_API_KEY
```

**macOS/Linux:**
```bash
echo $GROQ_API_KEY
```

**3. ChromaDB Errors**

**Windows (Command Prompt):**
```cmd
rmdir /s /q vectordb\chroma_db
```

**Windows (PowerShell):**
```powershell
Remove-Item -Recurse -Force vectordb\chroma_db
```

**macOS/Linux:**
```bash
rm -rf vectordb/chroma_db
```

**4. Virtual Environment Not Activating (Windows PowerShell)**

If you get an execution policy error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**5. Model Selection Issues**
- Ensure the model name is correct in `config.py`
- Check Groq API documentation for available models

**6. Python Command Not Found (macOS/Linux)**
- Use `python3` instead of `python`
- Ensure Python 3.13 is installed: `python3 --version`

## Platform-Specific Notes

### Windows
- Use backslashes (`\`) for file paths or raw strings: `r"C:\path\to\file.pdf"`
- Command Prompt and PowerShell have different syntax for environment variables

### macOS/Linux
- Use forward slashes (`/`) for file paths: `/path/to/file.pdf`
- May need to use `python3` instead of `python`
- Ensure proper file permissions for scripts

### All Platforms
- Ensure your terminal supports UTF-8 encoding for proper text display
- Keep your virtual environment activated while running the application

## Advanced Usage

### Custom Embeddings Model
```python
rag = RAG(embeddings_model="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
```

### Multiple Collections
```python
rag_docs = RAG(collection_name="documents")
rag_research = RAG(collection_name="research_papers")
```

### Session Management
```python
# Clear a specific session
memory_manager.clear_session("user_123")

# Get session history
history = memory_manager.get_history("user_123")
```

## Running the Application

### Simple ChatBot

Create a file `run_chatbot.py`:
```python
from chatbot import ChatBot

if __name__ == "__main__":
    bot = ChatBot()
    bot.start_conversation()
```

**Run:**
```bash
python run_chatbot.py
```

### RAG System

Create a file `run_rag.py`:
```python
from rag import RAG

if __name__ == "__main__":
    rag = RAG(collection_name="my_docs")
    rag.start_conversation(
        source_path="document.pdf",
        loader_type="pdf"
    )
```

**Run:**
```bash
python run_rag.py
```

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- **LangChain**: Framework for LLM applications
- **Groq**: Fast LLM inference
- **ChromaDB**: Vector database
- **HuggingFace**: Embeddings models
- **Python Community**: Various document loaders and utilities

## Support

For issues, questions, or contributions, please open an issue on GitHub.

---

**Note**: 
- This is a **command-line application** with no GUI or web interface.
- Make sure to keep your API keys secure and never commit them to version control.
- Always use environment variables or `.env` files for sensitive information.
- Test your setup with a small document first before processing large files.