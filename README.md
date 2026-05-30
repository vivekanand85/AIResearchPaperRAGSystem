📚 RAG System for Question Answering (PDF-Based)

A Retrieval-Augmented Generation (RAG) system that allows users to ask questions based on uploaded research papers (PDFs). The system retrieves relevant context from documents and generates accurate answers using an LLM.

🚀 Features
📄 Load and process multiple PDF research papers
🔎 Semantic search using embeddings
🧠 Context-aware answers using RAG pipeline
🗂 Vector storage with ChromaDB
💬 Question-answer interface (Streamlit / CLI)
⚡ Fast retrieval and response generation
🏗️ Project Structure
Ragssytemforqa/
│── app.py              # UI (Streamlit or frontend entry)
│── rag.py              # Core RAG pipeline (retrieval + LLM)
│── ingest.py           # PDF loading + embedding + vector DB creation
│── .gitignore
│── requirements.txt
│── pdfs/               # Research papers (input data)
│── chroma_db/          # Vector database (ignored in git)
⚙️ Tech Stack
Python 🐍
LangChain 🦜
OpenAI / LLM API 🤖
ChromaDB 🧠
PyPDF 📄
Streamlit (UI)
📦 Installation
git clone https://github.com/your-username/rag-system-qa.git
cd rag-system-qa

pip install -r requirements.txt
🔑 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

⚠️ Never push .env to GitHub.

▶️ How to Run
1. Ingest PDFs (Create Vector DB)
python ingest.py
2. Run the RAG System
python app.py
💬 Example Questions
What is multi-head attention?
Explain transformer architecture
What is few-shot learning?
Summarize this paper
🧠 How It Works
PDFs are loaded and split into chunks
Text is converted into embeddings
Stored in ChromaDB vector database
User query is embedded
Similar chunks are retrieved
LLM generates final answer using context
⚠️ Notes
Ensure API key is set correctly in .env
Do not commit venv/, .env, or chroma_db/
Run ingest.py before asking questions
📌 Future Improvements
Upload PDFs via UI
Add chat history memory
Improve retrieval ranking
Deploy on cloud (Render / Streamlit Cloud)
👨‍💻 Author

Built as part of AI learning project for Retrieval-Augmented Generation (RAG) systems.
