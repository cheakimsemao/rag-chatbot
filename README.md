# RAG Chatbot

A simple chatbot built with **Retrieval-Augmented Generation (RAG)** using an open-source Hugging Face model. It retrieves answers from your own documents using **LangChain**, **ChromaDB**, and a chat interface in **Streamlit**.

---

## Features

- Chat interface using Streamlit
- RAG pipeline built with LangChain
- ChromaDB as the vector store for document retrieval
- Fully open-source setup, no OpenAI API required

---

## Tech Stack

- LangChain (v0.3)
- Streamlit
- ChromaDB (For vector storage and retrieval)
- HuggingFaceEndpoint (LLM API access)

---

## Project Structure

```txt
.
├── chroma_db/              # Local ChromaDB vector store
├── docs/                   # Source documents
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── chunking.py     # Splits documents into chunks
│   │   ├── loading.py      # Loads and processes source docs
│   │   └── prompt.py       # Custom prompt templates
│   │── __init__.py
│   │── chroma.py           # ChromaDB vector store setup
│   │── rag_chain.py        # RAG chain definition using LangChain
│   └── rag_pipeline.py     # Entrypoint to build retriever & pipeline
├── .env.example            # Sample env file
├── .gitignore
├── main.py                 # Streamlit app (Chat UI)
├── README.md
└── requirements.txt        # Python dependencies
```

---

## Prerequisites

Before running the app, make sure you have the following:

- **Python 3.9 or higher** installed  
  You can check your version with:

  ```bash
  python --version
  ```

- **Hugging Face account with an access token**  
  This is required to use the Hugging Face Inference Endpoint with LangChain.  
  - Sign up at: [https://huggingface.co](https://huggingface.co)  
  - Create an access token at: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/cheakimsemao/rag-chatbot.git
cd rag-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your Hugging Face Access Token

Create a `.env` file in the root of the project:

```env
HUGGINGFACE_ACCESS_TOKEN=your-huggingface-access-token
```

### 4. Generate Vector Stores

This chatbot uses the **[Harvard College Student Handbook 2024–2025 and 2025-2026](https://handbook.college.harvard.edu)** (Located in `docs/`) as its default knowledge base, focusing specifically on question answering related to the college information.

> **Note:** The vector store is **not included in the repository**. To use the chatbot, you must first generate the vector store locally.

#### Using the default documents

```bash
python src/rag_pipeline.py
```

#### Customizing the knowledge base

- Place your new document in the `docs/` directory
- Generate a new vector store by running the above command
- Update the system prompt in `src/utils/prompt.py` to match your new context

The chatbot will automatically use the newly generated vector store for retrieval.

### 5. Run the RAG Chatbot

```bash
streamlit run main.py
```

---

## License

MIT License

---
