from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os

def get_embeddings_model(docs):
    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

def create_vector_store(docs):
    embeddings = get_embeddings_model(docs)

    vector_store = Chroma.from_documents(documents = docs,embedding = embeddings, persist_directory = 'chroma_db')

    return vector_store

def load_vector_store():
    embeddings = get_embeddings_model(None)

    vector_store = Chroma(persist_directory = 'chroma_db', embedding_function = embeddings)

    return vector_store