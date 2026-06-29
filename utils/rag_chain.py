import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate  # Added import

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing in environment variables")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.3
    )
    return llm

# Add this function so app.py can find it!
def get_prompt():
    template = """You are an intelligent campus assistant for Geeta University. 
    Use the provided piece of context to answer the student's question honestly and clearly.
    If you don't know the answer, say that you don't know.

    Context:
    {context}

    Question: 
    {question}

    Helpful Answer:"""
    
    return ChatPromptTemplate.from_template(template)