import streamlit as st

from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vectorstore
from utils.retriever import get_retriever
from utils.rag_chain import get_llm, get_prompt

st.set_page_config(
    page_title="Geeta University AI Assistant",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Geeta University AI Assistant")
st.write("Ask anything about Geeta University!")

# Load everything only once
@st.cache_resource
def initialize():
    documents = load_documents()
    chunks = split_documents(documents)
    embeddings = get_embeddings()

    # Create vector DB if needed
    create_vectorstore(chunks, embeddings)

    retriever = get_retriever(embeddings)

    llm = get_llm()

    prompt = get_prompt()

    return retriever, llm, prompt

retriever, llm, prompt = initialize()

question = st.text_input("Ask your question")

if st.button("Ask"):

    if question:

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        chain = prompt | llm
# Naye Google GenAI SDK ke hissaab se direct call:
client = get_llm()
prompt_template = get_prompt()

# Context aur Question ko prompt ke andar fill karna
formatted_prompt = prompt_template.format(context=retrieved_docs, question=user_query)

# Gemini se answer lena (Bina kisi authentication error ke)
response_data = client.models.generate_content(
    model='gemini-1.5-flash',
    contents=formatted_prompt,
)
response = response_data.text

    