import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
from src.utils.prompt import get_prompt

def create_rag_chain():
  """
  Create a RAG chain
  """
  
  embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
  vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding_model)
  retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 5})
  prompt = get_prompt()

  load_dotenv()
  
  HUGGINGFACE_ACCESS_TOKEN = os.getenv("HUGGINGFACE_ACCESS_TOKEN")
  repo_id = "mistralai/Mistral-7B-Instruct-v0.3"
  model_kwargs = {
    "task": "text-generation",
    "top_k": 50,
    "top_p": 0.5,
    "temperature": 0.5
  }

  llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    huggingfacehub_api_token=HUGGINGFACE_ACCESS_TOKEN,
    **model_kwargs
  )
  
  model = ChatHuggingFace(llm=llm)

  rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | model
    | StrOutputParser() 
  )
  
  return rag_chain
