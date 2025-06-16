import chromadb
import streamlit as st

from src.rag_chain import create_rag_chain

if __name__ == "__main__":
  chromadb.api.client.SharedSystemClient.clear_system_cache()
  rag_chain = create_rag_chain()

  st.set_page_config(page_title="RAG Chatbot", layout="centered")
  st.title("Harvard Student Handbook Q&A")

  if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! How can I help you?"}]

  # Display Chat History
  for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
      st.markdown(msg["content"])

  user_input = st.chat_input("Please enter your question here")

  if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
      with st.spinner("Thinking..."):
        response = rag_chain.invoke(user_input)
        st.markdown(response)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})
