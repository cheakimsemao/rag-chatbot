from utils.loading import load_docs
from utils.chunking import split_text
from chroma import save_to_chroma_db 

def generate_vector_store(doc_path: str, chroma_path: str):
  """
  Generate the given documents to vector store
  
  Args:
    doc_path (string):  A string of the document path
    chroma_path (string): A string of the Chroma path
    
  Returns:
    None
  """
  
  documents = load_docs(doc_path)
  chunks = split_text(documents)
  save_to_chroma_db(chunks, chroma_path)

if __name__ == "__main__":
  DOC_PATH = "./docs" # Directory to your pdf files:
  CHROMA_PATH = "./chroma_db" # Path to the directory to save to Chroma database
  
  generate_vector_store(DOC_PATH, CHROMA_PATH)