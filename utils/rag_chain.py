import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")

    print("API Key exists:", api_key is not None)
    print("API Key length:", len(api_key) if api_key else 0)

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=api_key,
        temperature=0.3,
    )

    return llm