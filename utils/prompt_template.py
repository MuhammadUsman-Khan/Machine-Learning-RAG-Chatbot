def get_prompt(context, question, history_text):

    prompt = f"""
    You are a helpful AI assistant for answering questions from a Machine Learning PDF book.

    Use:
    1. Chat history
    2. Retrieved PDF context

    to answer accurately.

    Chat History:
    {history_text}

    PDF Context:
    {context}

    Question:
    {question}

    Answer:
    """

    return prompt