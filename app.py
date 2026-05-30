import streamlit as st
from rag import ask

st.title("📄 AI Research Paper RAG System")

question = st.text_input("Ask your question")

if st.button("Ask"):

    if question.strip() == "":
        st.warning("Enter a question")
    else:
        answer, docs = ask(question)

        st.subheader("🧠 Answer")
        st.write(answer)

        st.subheader("📚 Sources")

        for i, doc in enumerate(docs):
            st.markdown(f"**Source {i+1}:** {doc.metadata.get('source')}")
            st.write(doc.page_content[:300])
            st.write("---")