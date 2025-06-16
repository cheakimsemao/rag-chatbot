from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document

def split_text(documents: list[Document]):
  """
  Split the text content of the given list of Document objects into smaller chunks.
  
  Args:
    documents (list[Document]): List of Document objects containing text content to split.
  
  Returns:
    list[Document]: List of Document objects representing the split text chunks.
  """
  
  # Initialize text splitter with specified parameters
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, # Size of each chunk in characters
    chunk_overlap=100, # Overlap between consecutive chunks
    length_function=len, # Function to compute the length of the text
    add_start_index=True, # Flag to add start index to each chunk
  )

  # Split documents into smaller chunks using text splitter
  chunks = text_splitter.split_documents(documents)
  print(f"Splitting {len(documents)} documents into {len(chunks)} chunks......")

  return chunks # Return the list of split text chunks