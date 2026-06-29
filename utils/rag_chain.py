import os
from google import genai
from google.genai import types

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY is missing in environment variables")
    
    # Nayi 'aq...' wali keys ke liye official naya Client use hota hai
    client = genai.Client(api_key=api_key)
    return client

def get_prompt():
    # Hum prompt ko string format mein return karenge jo naye SDK ke sath perfectly chalega
    template = """You are an intelligent campus assistant for Geeta University. 
    Use the provided piece of context to answer the student's question honestly and clearly.
    If you don't know the answer, say that you don't know.

    Context:
    {context}

    Question: 
    {question}

    Helpful Answer:"""
    return template