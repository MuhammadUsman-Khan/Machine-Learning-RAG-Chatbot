# 🤖 Machine Learning RAG Chatbot

> **Ask questions directly from a Machine Learning Book PDF using AI**
>
> A Retrieval-Augmented Generation (RAG) chatbot powered by **LangChain**, **ChromaDB**, **HuggingFace Embeddings**, and **Gemini LLM** with an interactive Streamlit UI.

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-RAG%20Framework-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-7B2D8B?style=for-the-badge&logo=databricks&logoColor=white)](https://www.trychroma.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Embeddings-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![Gemini](https://img.shields.io/badge/Gemini-LLM-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)](https://github.com/MuhammadUsman-Khan/Machine-Learning-RAG-Chatbot)

---

## 🔗 Quick Links

[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuhammadUsman-Khan/Machine-Learning-RAG-Chatbot)
[![View Profile](https://img.shields.io/badge/GitHub-MuhammadUsman--Khan-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/MuhammadUsman-Khan)

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
- [🚀 Future Improvements](#-future-improvements)
- [👤 Author](#-author)

---

## 🎯 Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline that lets you have an intelligent conversation with a Machine Learning Book PDF. Instead of hallucinating answers, the chatbot retrieves the most relevant passages from the document first, then feeds them to a Gemini LLM to generate grounded, accurate responses.

**Problem**: Large language models lack knowledge of specific documents or domain PDFs.

**Solution**: Use RAG — embed the PDF into a vector store, retrieve relevant chunks on each query, and pass them as context to the LLM for factual, document-grounded answers.

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
  [Process PDF Button]        [Ask Question]
          │                         │
          ▼                         ▼
  pdf_loader.py            vector_store.py
  (PyPDF → Docs)        (Load ChromaDB)
          │                         │
          ▼                         ▼
  vector_store.py           rag_chain.py
  (Embed + Store         (Retrieve → Prompt
   in ChromaDB)            → Gemini LLM)
                                    │
                                    ▼
                             Answer to User
```

---

## 📁 Project Structure

```
Machine-Learning-RAG-Chatbot/
│
├── data/
│   └── ML_Book.pdf            # Source PDF document
│
├── utils/
│   ├── pdf_loader.py          # Load & split PDF into chunks
│   ├── vector_store.py        # Create & load ChromaDB vector store
│   └── rag_chain.py           # RAG chain: retrieve + prompt + LLM
│
├── app.py                     # Streamlit application entry point
├── requirements.txt           # Python dependencies
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
- Text is split into overlapping chunks to preserve context across page boundaries

### Step 2: Embedding & Vector Store
```
Text Chunks → HuggingFace Embeddings → ChromaDB (persisted locally)
```
- Each chunk is converted into a dense vector using a HuggingFace sentence-transformer model
- Vectors are stored in ChromaDB for fast semantic retrieval
- The store is persisted on disk — no re-processing needed on subsequent runs

### Step 3: Retrieval-Augmented Generation
```
User Query → Similarity Search → Top-K Chunks → Gemini LLM → Answer
```
- The user's question is embedded and matched against stored vectors
- The most semantically similar chunks are retrieved
- A LangChain prompt template combines the retrieved context + question
- Gemini LLM generates a grounded answer using only the retrieved context

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | LangChain | RAG pipeline orchestration |
| **LLM** | Gemini (Google Generative AI) | Answer generation |
| **Embeddings** | HuggingFace `sentence-transformers` | Semantic text encoding |
| **Vector Store** | ChromaDB | Similarity search & retrieval |
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

> ✅ You only need to do this **once**. The vector store is saved to disk.

### Step 2 — Ask Questions

Type any question related to the ML book in the text input:

```
Ask Question: What is the difference between supervised and unsupervised learning?
```

The chatbot will:
1. Embed your question
2. Retrieve the most relevant PDF passages
3. Pass them to Gemini LLM as context
4. Return a grounded, document-based answer

---

## ✨ Key Features

### 📄 PDF-Grounded Answers
Responses are based strictly on retrieved document chunks — no hallucination from the LLM's generic training data.

### 🔍 Semantic Search
HuggingFace sentence-transformer embeddings enable meaning-based retrieval, not just keyword matching.

### 💾 Persistent Vector Store
ChromaDB persists the index to disk, so the PDF is only processed once — making subsequent queries instant.

### 🧩 Modular Architecture
The `utils/` package separates concerns cleanly:
- `pdf_loader.py` — document ingestion
- `vector_store.py` — embedding & retrieval
- `rag_chain.py` — LLM interaction

### 🌐 Interactive UI
Streamlit provides a simple, browser-based interface with no frontend coding required.

---

## 🚀 Future Improvements

### Short-term
- [ ] Support uploading **any PDF** via UI (not just hardcoded path)
- [ ] Display retrieved source chunks alongside the answer
- [ ] Add conversation memory (multi-turn chat history)
- [ ] Stream LLM responses token-by-token

### Medium-term
- [ ] Support multiple PDFs simultaneously
- [ ] Add a reranker (cross-encoder) for more precise retrieval
- [ ] Swap embedding models via UI dropdown
- [ ] Evaluate retrieval quality with RAGAS framework

### Long-term
- [ ] Deploy to cloud (Streamlit Cloud / HuggingFace Spaces)
- [ ] Add authentication for multi-user access
- [ ] Extend to support other document formats (DOCX, TXT, URLs)

---

## 👤 Author

**Muhammad Usman Khan**

- 🎓 BS Artificial Intelligence Student
- 💼 AI Engineering Intern
- 🤖 GenAI | LLM | RAG | Machine Learning
- 🔗 [GitHub](https://github.com/MuhammadUsman-Khan)
- 🏆 [Kaggle](https://www.kaggle.com/muhammadusmankhan0)

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
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

---

Made by **Muhammad Usman Khan**

[⬆ Back to Top](#-machine-learning-rag-chatbot)
