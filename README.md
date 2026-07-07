# 📚 Research Intelligence Platform

An end-to-end **Multi-Document Retrieval-Augmented Generation (RAG)** application that enables users to upload multiple research papers, perform semantic search, and receive accurate, context-aware answers powered by **Gemini 2.5 Flash** and **FAISS**.

---

## 🚀 Features

- 📄 Upload and query multiple PDF research papers
- 🔍 Semantic search using vector embeddings and FAISS
- 🤖 Context-aware question answering using Gemini 2.5 Flash
- ✂️ Intelligent document chunking for efficient retrieval
- ⚡ Fast similarity search with FAISS Vector Database
- 🖥️ Interactive Streamlit web interface
- 🧩 Modular and scalable project architecture

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries & Frameworks
- LangChain
- Streamlit
- FAISS
- Hugging Face Sentence Transformers
- Google Gemini API
- PyPDFLoader
- python-dotenv

### AI Technologies
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Large Language Models (LLMs)

---

## 📂 Project Structure

```
research-intelligence-platform/
│
├── app/
│   ├── chunking/
│   ├── config/
│   ├── embeddings/
│   ├── llm/
│   ├── loaders/
│   ├── prompts/
│   ├── retrieval/
│   ├── ui/
│   ├── utils/
│   ├── vectorstore/
│   └── rag_pipeline.py
│
├── assets/
├── data/
├── logs/
├── tests/
├── .env.example
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/aditya-3645/research-intelligence-platform.git

cd research-intelligence-platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
.\venv\Scripts\Activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 🔄 RAG Pipeline

```
Upload PDFs
      │
      ▼
Extract Text
      │
      ▼
Chunk Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store Vectors in FAISS
      │
      ▼
User Question
      │
      ▼
Semantic Retrieval
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Grounded Answer
```

---

## 🎯 Future Improvements

- Source citations with page numbers
- Persistent FAISS vector index
- Conversation memory
- Chat-style interface
- Docker deployment
- Cloud deployment
- User authentication

---

## 👨‍💻 Author

**Aditya Dhumal**

- GitHub: https://github.com/aditya-3645
- LinkedIn: https://www.linkedin.com/in/adityadhumal2005

---

## 📜 License

This project is licensed under the MIT License.
