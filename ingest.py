from dotenv import load_dotenv
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY missing")

pdfs = [
    "papers/paper1.pdf",
    "papers/paper2.pdf",
    "papers/paper3.pdf"
]

print("Loading PDFs...")

documents = []

for pdf in pdfs:
    loader = PyPDFLoader(pdf)
    docs = loader.load()

    # add source metadata for citations
    for d in docs:
        d.metadata["source"] = pdf

    documents.extend(docs)

print("Splitting chunks...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Total chunks: {len(chunks)}")

print("Creating embeddings + vector DB...")

db = Chroma.from_documents(
    documents=chunks,
    embedding=OpenAIEmbeddings(),
    persist_directory="chroma_db"
)

print("DONE: Vector DB created")