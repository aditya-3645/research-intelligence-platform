import streamlit as st

from app.utils.file_handler import save_uploaded_files
from app.loaders.pdf_loader import load_pdfs
from app.chunking.text_chunker import chunk_documents
from app.embeddings.embedding_model import get_embedding_model
from app.vectorstore.faiss_store import create_vector_store
from app.retrieval.retriever import create_retriever
from app.llm.gemini_llm import get_llm
from app.rag_pipeline import ask_question


def run_app():

    st.set_page_config(
        page_title="Research Intelligence Platform",
        page_icon="📚",
        layout="wide"
    )

    st.title("📚 Research Intelligence Platform")

    uploaded_files = st.file_uploader(
        "Upload PDF Research Papers",
        type="pdf",
        accept_multiple_files=True
    )

    question = st.text_input("Ask your question")

    if st.button("Generate Answer"):

        if not uploaded_files:
            st.warning("Please upload at least one PDF.")
            return

        if not question:
            st.warning("Please enter a question.")
            return

        with st.spinner("Processing..."):

            pdf_paths = save_uploaded_files(uploaded_files)

            documents = load_pdfs(pdf_paths)

            chunks = chunk_documents(documents)

            embedding_model = get_embedding_model()

            vector_store = create_vector_store(
                chunks,
                embedding_model
            )

            retriever = create_retriever(vector_store)

            llm = get_llm()

            answer = ask_question(
                retriever,
                llm,
                question
            )

        st.success("Answer Generated!")

        st.write(answer)