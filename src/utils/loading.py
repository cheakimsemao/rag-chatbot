from langchain_community.document_loaders import PyPDFDirectoryLoader

def load_docs(doc_path: str):
  """
  Load PDF documents from the specified directory using PyPDFDirectoryLoader.
  
  Args:
    doc_path (string): A string of the document path
  
  Returns:
    List of Document objects: Loaded PDF documents represented as Langchain document objects.
  """
  
  # Initialize PDF loader with specified directory
  document_loader = PyPDFDirectoryLoader(doc_path) 
  # Load PDF documents and return them as a list of Document objects
  return document_loader.load()
