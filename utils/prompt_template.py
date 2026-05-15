def get_prompt(context, question):

    prompt = f"""
    You are a helpful AI assistant.

    Answer ONLY from the provided context.

    If the answer is not in the context, say:
    "I could not find this in the book."

    Context:
    {context}

    Question:
    {question}
    """

    return prompt