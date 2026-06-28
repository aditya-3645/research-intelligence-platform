from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document


def create_vector_store(documents: list[Document], embedding_model):
    """
    Creates a FAISS vector store from document chunks.
    """

    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embedding_model
    )

    return vector_store