from langchain_google_genai import ChatGoogleGenerativeAI
from utils.prompt_template import get_prompt
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def ask_question(question, vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    relevant_docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in relevant_docs]
    )

    prompt = get_prompt(context, question)

    response = llm.invoke(prompt)

    return response.content