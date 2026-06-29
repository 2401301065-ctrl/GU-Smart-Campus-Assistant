import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing in environment variables")

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.3,
        # Yeh line add karni hai taaki global endpoint se connect ho sake:
        client_options={"api_endpoint": "https://generativelanguage.googleapis.com"}
    )
    return llm

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