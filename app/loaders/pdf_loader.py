from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_pdfs(pdf_paths: list[str]) -> list[Document]:
    """
    Loads multiple PDFs and returns all documents.
    """

    documents = []

    for pdf in pdf_paths:
        loader = PyPDFLoader(pdf)
        documents.extend(loader.load())

    return documents