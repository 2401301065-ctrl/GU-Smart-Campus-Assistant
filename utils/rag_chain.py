import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )
    return llm


def get_prompt():
    prompt = ChatPromptTemplate.from_template(
        """
You are Geeta University's official AI Assistant.

Answer ONLY using the provided context.

If the answer is not present in the context, reply:
"I couldn't find that information in the university documents."

Context:
{context}

Question:
{question}
"""
    )

    return prompt