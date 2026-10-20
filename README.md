# Mini-RAG-Local-AI-with-Ollama

A local AI assistant built with Python, Flask, and Ollama. The goal of this project is to explore how large language models (LLMs) can run directly on a personal computer without depending on external AI APIs.

Beyond running a language model locally, the project focuses on building a practical application that can answer questions, remember conversations, retrieve information from documents, and provide structured responses.

## Project Overview

This project started as a practical exploration of local AI and gradually evolved into a document-based AI assistant.

The main idea is simple: instead of sending requests to a cloud service, the application communicates with an LLM running locally through Ollama.

The project covers several aspects of working with local models, including prompt engineering, model comparison, conversation memory, document retrieval, and performance evaluation.

## Features

- **Local LLM inference:** Run language models directly on a local machine using Ollama.
- **Web interface:** Interact with the assistant through a simple Flask application.
- **Conversation memory:** Maintain previous messages to support follow-up questions.
- **Document-based Q&A:** Ask questions about locally stored course materials.
- **Mini-RAG pipeline:** Retrieve relevant document content using a TF-IDF-based approach before generating answers.
- **Structured responses:** Generate JSON outputs using predefined schemas.
- **Model comparison:** Compare different local models based on response quality, execution time, and resource consumption.
- **Performance monitoring:** Measure response time, generated tokens, and inference speed.
- **Code assistance:** Experiment with code generation, debugging, and code review.
- **Multimodal experiments (optional):** Explore image understanding using a compatible vision model.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Ollama | Local LLM management and inference |
| Qwen / Gemma | Language models used for experimentation |
| Flask | Web application and backend |
| REST API | Communication with the local Ollama server |
| TF-IDF | Document retrieval |
| HTML, CSS, JavaScript | Web interface |
| Pandas / Matplotlib | Benchmark analysis and visualization |
| psutil | System resource monitoring |

## How It Works

The assistant combines a local language model with a lightweight document retrieval system.

When a user submits a question, the application searches the available documents for relevant information. The retrieved text is then included in the prompt sent to Ollama.

The language model uses this context to generate a response, which is displayed in the web interface.

**Application flow:**

```text
User
  |
  v
Flask Web Interface
  |
  v
Python Backend
  |
  +----> Conversation History
  |
  +----> Local Document Retriever
  |             |
  |             v
  |       Relevant Context
  |             |
  +-------------+
  |
  v
Ollama REST API
  |
  v
Local Language Model
  |
  v
Generated Response
  |
  v
Web Interface
```

The document retrieval component uses a lightweight TF-IDF approach rather than a vector database. This keeps the implementation simple and makes it easier to understand how Retrieval-Augmented Generation works.

## Project Structure

```text
LocalAI_Lab/
|
├── source/
│   ├── app.py
│   ├── chatbot.py
│   ├── rag.py
│   ├── benchmark.py
│   └── templates/
│       └── index.html
|
├── documents/
│   ├── ai.txt
│   ├── ml.txt
│   ├── rl.txt
│   └── ...
|
├── screenshots/
│
├── report.pdf
└── README.md
```

## Getting Started

### 1. Prerequisites

Make sure you have the following installed:

- Python 3.10 or newer
- Ollama
- pip
- At least 8 GB RAM recommended, depending on the model

A dedicated GPU can improve inference performance, but it is not required.

### 2. Install Ollama

Download Ollama from:

https://ollama.com/download

For Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Verify the installation:

```bash
ollama --version
```

Start the Ollama service if it is not already running:

```bash
ollama serve
```

### 3. Download the Models

Download the models used in the experiments:

```bash
ollama pull qwen3.5
ollama pull gemma3
```

The models can be replaced with smaller alternatives depending on the available hardware.

Check downloaded models:

```bash
ollama list
```

### 4. Install Python Dependencies

```bash
pip install flask requests pandas matplotlib psutil
```

### 5. Run the Application

Navigate to the source directory:

```bash
cd LocalAI_Lab/source
```

Start the Flask server:

```bash
python app.py
```

Open the application in your browser:

http://127.0.0.1:5001

The assistant should now be accessible locally.

## Additional Experiments

### Console Chatbot

The project also includes a command-line chatbot with conversation history.

```bash
python chatbot.py
```

### Model Benchmarking

To compare two local models:

```bash
python benchmark.py qwen3.5 gemma3
```

The benchmark is designed to explore differences in inference speed, memory requirements, and response quality.

Actual performance depends on the selected models and the hardware used.

### Document Retrieval

The RAG module retrieves relevant information from text files stored in the `documents/` directory.

The assistant is instructed to answer using the provided context and indicate when the requested information is unavailable.

This helps reduce unsupported answers, although it does not completely eliminate hallucinations.


## Conclusion

This project demonstrates how a local language model can be integrated into a complete Python application.

By combining Ollama, Flask, conversation history, and document retrieval, it provides a foundation for building AI assistants that operate locally without requiring a cloud inference service.

It also highlights the practical trade-offs involved in choosing and deploying language models on consumer hardware.

## License

Created for educational and experimental purposes.
