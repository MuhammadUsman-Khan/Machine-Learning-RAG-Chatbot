import streamlit as st
import os

from utils.pdf_loader import load_pdf
from utils.vector_store import create_vector_store, load_vector_store
from utils.rag_chain import ask_question

from utils.db import (
    init_db,
    create_chat,
    add_message,
    get_chats,
    get_messages, 
    rename_chat
)

init_db()


st.set_page_config(
    page_title="ML PDF Chatbot",
    page_icon="📚"
)

st.title("Machine Learning PDF Chatbot")


pdf_path = "data/ML_Book.pdf"

if not (os.path.exists("chroma_db") and os.listdir("chroma_db")):

    with st.spinner("Processing PDF..."):

        docs = load_pdf(pdf_path)
        create_vector_store(docs)

    st.success("PDF processed successfully!")

else:
    st.success("Vector DB already exists.")



chats = get_chats()

if not chats:
    create_chat("chat_1", "Chat 1")
    chats = get_chats()

chat_dict = {c[0]: c[1] for c in chats}


if "current_chat" not in st.session_state:
    st.session_state.current_chat = chats[0][0]



st.sidebar.title("Chats")


if st.sidebar.button("+ New Chat"):

    new_id = f"chat_{len(chats) + 1}"

    create_chat(new_id, f"Chat {len(chats) + 1}")

    st.session_state.current_chat = new_id

    st.rerun()


selected_chat = st.sidebar.radio(
    "Your Chats",
    options=list(chat_dict.keys()),
    format_func=lambda x: chat_dict[x],
    index=list(chat_dict.keys()).index(st.session_state.current_chat)
)

st.session_state.current_chat = selected_chat


messages = get_messages(st.session_state.current_chat)


for msg in messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask a question from the book")


if question:


    add_message(st.session_state.current_chat, "user", question)

    with st.chat_message("user"):
        st.markdown(question)


    recent_messages = get_messages(st.session_state.current_chat)[-6:]


    answer = ask_question(
        question,
        recent_messages
    )


    add_message(st.session_state.current_chat, "assistant", answer)

    with st.chat_message("assistant"):
        st.markdown(answer)

st.sidebar.subheader("✏️ Rename Chat")

new_name = st.sidebar.text_input("New chat name")

if st.sidebar.button("Rename"):

    if new_name:

        rename_chat(st.session_state.current_chat, new_name)

        st.rerun()