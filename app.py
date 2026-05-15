import streamlit as st
from utils.pdf_loader import load_pdf
from utils.vector_store import (
    create_vector_store,
    load_vector_store
)
from utils.rag_chain import ask_question

st.set_page_config(
    page_title="ML PDF Chatbot",
    page_icon=":books:"
)

st.title("Machine Learning PDF Chatbot")


if st.button("Process PDF"):

    docs = load_pdf(
        "data/ML_Book.pdf"
    )

    create_vector_store(docs)

    st.success("PDF Processed Successfully")


question = st.text_input(
    "Ask Question"
)

if question:

    vector_store = load_vector_store()

    answer = ask_question(
        question,
        vector_store
    )

    st.write(answer)