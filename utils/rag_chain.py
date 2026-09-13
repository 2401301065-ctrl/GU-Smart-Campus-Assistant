import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env
load_dotenv()
print("API:", os.getenv("GOOGLE_API_KEY"))


def get_llm():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is missing. Please add it to your .env file "
            "or Streamlit Secrets if deploying."
        )

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=api_key,
        temperature=0.3,
    )

    return llm


def get_prompt():
    prompt = ChatPromptTemplate.from_template("""
You are Geeta University Assistant AI.

You are a helpful AI assistant for Geeta University.

Rules:
1. Answer ONLY using the provided context.
2. If the answer is not available in the context, reply:
   "I couldn't find that information in the university knowledge base."
3. Be polite, concise, and accurate.
4. Format answers neatly using bullet points whenever appropriate.

Context:
{context}

Question:
{question}

Answer:
""")

    return prompt