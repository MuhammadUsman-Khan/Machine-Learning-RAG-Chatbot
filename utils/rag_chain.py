from langchain_google_genai import ChatGoogleGenerativeAI
from utils.prompt_template import get_prompt
import os
from dotenv import load_dotenv

from utils.vector_store import load_vector_store

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_question(question, chat_history):

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    relevant_docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    recent_history = chat_history[-6:]


    history_text = ""

    for msg in recent_history:

        role = msg["role"]

        content = msg["content"]

        history_text += f"{role}: {content}\n"

    prompt = get_prompt(context, question, history_text)

    response = llm.invoke(prompt)

    return response.content