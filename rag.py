from dotenv import load_dotenv
import os

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

load_dotenv()

embeddings = OpenAIEmbeddings()

db = Chroma(
    persist_directory="chroma_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


def ask(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        [f"Source: {d.metadata.get('source')}\n{d.page_content}" for d in docs]
    )

    prompt = f"""
You are a helpful AI research assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{question}

Instructions:
- Give clear explanation
- If possible, include paper reference (source filename)
- If not in context, say "Not found in documents"

Answer:
"""

    response = llm.invoke(prompt)

    return response.content, docs