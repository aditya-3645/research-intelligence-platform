import os
from pathlib import Path


UPLOAD_DIR = "data/uploads"


def save_uploaded_files(uploaded_files):
    """
    Saves uploaded PDF files locally and returns their paths.
    """

    os.makedirs(UPLOAD_DIR, exist_ok=True)

    pdf_paths = []

    for file in uploaded_files:
        file_path = Path(UPLOAD_DIR) / file.name

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        pdf_paths.append(str(file_path))

    return pdf_paths