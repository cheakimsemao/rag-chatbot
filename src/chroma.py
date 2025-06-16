import os
import shutil

from datetime import datetime
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

def save_to_chroma_db(chunks: list[Document], chroma_path: str):
  """
  Save the given list of Document objects to a Chroma database.
  
  Args:
    chunks (list[Document]): List of Document objects representing text chunks to save.
    chroma_path (string): A string of the Chroma path
  
  Returns:
    None
  """

  # Check if the database already exists
  if os.path.exists(chroma_path):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = f"{chroma_path}/backup_db_{timestamp}"
    shutil.move(chroma_path, backup_path)
    print(f"Existing Chroma database moved to backup: {backup_path}")
    
  embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

  # Create a new Chroma database from the documents using OpenAI embeddings
  Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory=chroma_path
  )

  print(f"Saved {len(chunks)} chunks to {chroma_path}.")