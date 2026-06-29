from langchain_core.prompts import ChatPromptTemplate

def get_prompt():
    prompt = ChatPromptTemplate.from_template("""
    You are Geeta University Assistant AI.
    Answer user questions based only on provided context.

    Context: {context}
    Question: {question}

    Answer:
    """)
    return prompt