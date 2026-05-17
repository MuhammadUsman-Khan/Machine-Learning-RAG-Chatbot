# 🤖 Machine Learning RAG Chatbot

> **Ask questions directly from a Machine Learning Book PDF using AI**
>
> A Retrieval-Augmented Generation (RAG) chatbot powered by **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, **Gemini LLM**, **SQLite Chat History**, and an interactive Streamlit UI.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-7B2D8B?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Gemini](https://img.shields.io/badge/Gemini-LLM-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![SQLite](https://img.shields.io/badge/SQLite-Chat%20History-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)](https://github.com/MuhammadUsman-Khan/Machine-Learning-RAG-Chatbot)

---

## 🔗 Quick Links

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuhammadUsman-Khan/Machine-Learning-RAG-Chatbot)
[![View Profile](https://img.shields.io/badge/GitHub-MuhammadUsman--Khan-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuhammadUsman-Khan)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com)

---

## 📋 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [🏗️ Architecture](#️-architecture)
- [📁 Project Structure](#-project-structure)
- [🔬 How It Works](#-how-it-works)
- [🛠️ Tech Stack](#️-tech-stack)
- [⚙️ Installation & Setup](#️-installation--setup)
- [📖 Usage](#-usage)
- [✨ Key Features](#-key-features)
- [🧠 Chat Memory System](#-chat-memory-system)
- [🚀 Future Improvements](#-future-improvements)
- [👤 Author](#-author)

---

## 🎯 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that lets users have intelligent conversations with a Machine Learning Book PDF. Instead of hallucinating answers, the chatbot retrieves the most relevant passages from the document first, then feeds them to a Gemini LLM to generate grounded and context-aware responses.

The application also supports:
- Persistent vector storage using ChromaDB
- Chat history memory using SQLite
- Renaming chats
- Context-aware follow-up questions
- Streamlit chat interface

**Problem**: Large language models do not automatically know the content of private PDFs or books.

**Solution**: Use RAG — convert PDF chunks into embeddings, retrieve relevant chunks for every query, and provide them to the LLM as factual context.

---

## 🏗️ Architecture

```
User Query
    │
    ▼
┌─────────────────────────────────────────────────────┐
│                  Streamlit UI (app.py)               │
└──────────────────────┬──────────────────────────────┘
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
  [Process PDF]              [Ask Question]
          │                         │
          ▼                         ▼
  pdf_loader.py             vector_store.py
  (Load & Split PDF)       (Load ChromaDB)
          │                         │
          ▼                         ▼
  vector_store.py            rag_chain.py
  (Embeddings + Store)   (Retrieve + Prompt + LLM)
                                    │
                                    ▼
                           SQLite Chat Database
                                    │
                                    ▼
                             Answer to User
```

---

## 📁 Project Structure

```
Machine-Learning-RAG-Chatbot/
│
├── chroma_db/                 # Persistent Chroma vector database
│
├── data/
│   └── ML_Book.pdf            # Source PDF document
│
├── utils/
│   ├── db.py                  # SQLite database operations
│   ├── pdf_loader.py          # Load & split PDF into chunks
│   ├── prompt_template.py     # Prompt template for RAG
│   ├── rag_chain.py           # Retrieval + Gemini response generation
│   └── vector_store.py        # ChromaDB vector store operations
│
├── chat_history.db            # SQLite database file
├── app.py                     # Main Streamlit application
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
├── .gitignore
└── README.md
```

---

## 🔬 How It Works

### Step 1: PDF Loading & Chunking
```
ML_Book.pdf → PyPDFLoader → Text Chunks (with overlap)
```
- The PDF is loaded using `PyPDFLoader` from LangChain
- Text is split into overlapping chunks using `RecursiveCharacterTextSplitter`
- Chunk overlap preserves context between sections

### Step 2: Embedding & Vector Storage
```
Text Chunks → HuggingFace Embeddings → ChromaDB (persisted locally)
```
- Each text chunk is converted into dense vector embeddings
- Embeddings are generated using HuggingFace sentence-transformers
- ChromaDB stores vectors for semantic similarity search
- The database persists locally, preventing repeated processing

### Step 3: Retrieval-Augmented Generation
```
User Question → Similarity Search → Relevant Chunks → Gemini LLM → Answer
```
- User questions are embedded and matched against stored vectors
- ChromaDB retrieves the most semantically similar chunks
- Retrieved context is injected into the prompt via a LangChain prompt template
- Gemini generates grounded answers from the document context

### Step 4: Chat Memory System
```
Conversation → SQLite Database → Persistent Chat History
```
- All conversations are stored in SQLite via `db.py`
- Previous messages can be used as conversational memory
- Only recent messages are passed to the LLM for efficient context management
- Chats can be renamed dynamically

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | LangChain | RAG pipeline orchestration |
| **LLM** | Gemini (Google Generative AI) | Answer generation |
| **Embeddings** | HuggingFace Sentence Transformers | Semantic text encoding |
| **Vector Store** | ChromaDB | Similarity search & retrieval |
| **Database** | SQLite | Chat history storage |
| **PDF Parsing** | PyPDF | Extract text from PDF |
| **UI** | Streamlit | Interactive web interface |
| **Config** | python-dotenv | API key management |

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.8+
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadUsman-Khan/Machine-Learning-RAG-Chatbot.git
cd Machine-Learning-RAG-Chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 4. Add Your PDF

Place your PDF in the `data/` folder:

```
data/ML_Book.pdf
```

### 5. Run the App

```bash
streamlit run app.py
```

---

## 📖 Usage

### Step 1 — Process the PDF

On first launch, click **"Process PDF"** to:
- Load and chunk the PDF
- Generate HuggingFace embeddings
- Store vectors in ChromaDB (persisted locally)

> ✅ If the vector database already exists, the PDF will **not** be processed again.

### Step 2 — Ask Questions

Example questions:

```
What is supervised learning?
Explain overfitting in machine learning.
What is gradient descent?
Difference between classification and regression?
```

### Step 3 — Continue Conversations

The chatbot remembers recent conversation history, enabling follow-up questions like:

```
Can you explain that with an example?
What are its advantages?
```

---

## ✨ Key Features

### 📄 PDF-Grounded Responses
Answers are generated using retrieved document chunks rather than generic LLM knowledge.

### 🔍 Semantic Search
HuggingFace sentence-transformer embeddings enable meaning-based retrieval, not just keyword matching.

### 💾 Persistent Vector Database
ChromaDB persists the index to disk — PDF processing happens only once, making all subsequent queries instant.

### 🧠 Conversation Memory
Recent chat history is passed to the LLM for contextual follow-up questions.

### 🗄️ SQLite Chat Storage
All chats and messages are saved permanently in a lightweight SQLite database.

### ✏️ Rename Chats
Users can rename conversations dynamically inside the app.

### 🌐 Interactive Streamlit UI
Modern chatbot interface with real-time responses.

### 🧩 Modular Code Structure
Clean separation of responsibilities across the `utils/` package:
- `pdf_loader.py` — document ingestion
- `vector_store.py` — embedding & retrieval
- `rag_chain.py` — LLM interaction
- `prompt_template.py` — prompt construction
- `db.py` — SQLite chat history operations

---

## 🧠 Chat Memory System

The chatbot includes a lightweight memory system using SQLite.

### Features
- Persistent chat storage across sessions
- Multiple saved conversations
- Recent-history memory passed to LLM
- Rename chats dynamically
- Fast retrieval

### Why Only Recent History?

Passing the entire conversation history to the LLM increases token usage, cost, and latency. Instead, only the most recent messages are included — giving the model enough context for follow-up questions without bloating the prompt.

---

## 🚀 Future Improvements

### Short-term
- [ ] Upload any PDF directly from UI
- [ ] Display retrieved source chunks alongside the answer
- [ ] Stream LLM responses token-by-token
- [ ] Add dark/light mode toggle

### Medium-term
- [ ] Multi-PDF support
- [ ] Reranking with cross-encoders
- [ ] LangSmith tracing integration
- [ ] Hybrid search (BM25 + vectors)

### Long-term
- [ ] Cloud deployment (Streamlit Cloud / HuggingFace Spaces)
- [ ] Multi-user authentication
- [ ] OCR support for scanned PDFs
- [ ] Voice interaction

---

## 👤 Author

**Muhammad Usman Khan**

- 🎓 BS Artificial Intelligence Student
- 💼 AI Engineering Intern
- 🤖 GenAI | RAG | LLMs | Machine Learning | NLP
- 🔗 [GitHub](https://github.com/MuhammadUsman-Khan)
- 🏆 [Kaggle](https://www.kaggle.com/muhammadusmankhan0)
- 💼 [LinkedIn](https://www.linkedin.com)

### Connect & Collaborate

This project is part of my portfolio of AI and machine learning projects. If you find it useful:

- ⭐ Star the repository
- 🍴 Fork and build upon it
- 💬 Share feedback via Issues
- 🤝 Collaborate on related projects

---

## 📄 License

This project is open-source and free to use for educational and personal purposes.

---

## 🙏 Acknowledgments

- **LangChain** for the RAG framework and tooling
- **Google** for the Gemini LLM API
- **HuggingFace** for open-source embedding models
- **ChromaDB** for the lightweight vector store
- **Streamlit** for making ML apps easy to deploy

---

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-7B2D8B?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![SQLite](https://img.shields.io/badge/SQLite-Chat%20History-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

---

Made by **Muhammad Usman Khan**

[⬆ Back to Top](#-machine-learning-rag-chatbot)
