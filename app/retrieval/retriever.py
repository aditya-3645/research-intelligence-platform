from langchain_core.vectorstores import VectorStoreRetriever


def create_retriever(vector_store, k: int = 3) -> VectorStoreRetriever:
    """
    Creates a retriever from the FAISS vector store.
    """

    retriever = vector_store.as_retriever(
        search_kwargs={"k": k}
    )

    return retriever