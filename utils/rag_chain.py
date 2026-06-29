from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# ---------------------------
# LLM FUNCTION
# ---------------------------
def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )
    return llm


# ---------------------------
# PROMPT FUNCTION
# ---------------------------
def get_prompt():
    prompt = ChatPromptTemplate.from_template("""
You are Geeta University Assistant AI.

Answer user questions ONLY using the provided context.

Context:
{context}

Question:
{question}

Answer clearly and simply:
""")
    return prompt