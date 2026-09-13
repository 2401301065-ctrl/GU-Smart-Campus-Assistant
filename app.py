import streamlit as st

from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embeddings
from utils.vectorstore import create_vectorstore
from utils.retriever import get_retriever
from utils.rag_chain import get_llm, get_prompt


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Geeta University AI Assistant",
    page_icon="🎓",
    layout="wide"
)


# =========================
# TITLE
# =========================

st.title("🎓 Geeta University AI Assistant")
st.write("Ask anything about Geeta University!")


# =========================
# INITIALIZE RAG SYSTEM
# =========================

@st.cache_resource
def initialize():

    # Load PDF/document files
    documents = load_documents()

    # Split documents into smaller chunks
    chunks = split_documents(documents)

    # Create embeddings
    embeddings = get_embeddings()

    # Create/update vector database
    create_vectorstore(chunks, embeddings)

    # Create retriever
    retriever = get_retriever(embeddings)

    # Get LLM
    llm = get_llm()

    # Get prompt
    prompt = get_prompt()

    return retriever, llm, prompt


# Initialize the complete system
retriever, llm, prompt = initialize()


# =========================
# USER INPUT
# =========================

question = st.text_input(
    "Ask your question",
    placeholder="e.g. What is the admission process at Geeta University?"
)


# =========================
# ASK BUTTON
# =========================

if st.button("Ask"):

    if question:

        # Retrieve relevant documents
        docs = retriever.invoke(question)

        # Combine retrieved document content
        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        # Create final prompt
        formatted_prompt = prompt.format(
            context=context,
            question=question
        )

        # Generate answer using the configured LLM
        response = llm.invoke(formatted_prompt)

        # Display answer
        st.subheader("Answer")

        if hasattr(response, "content"):
            st.write(response.content)
        else:
            st.write(response)

    else:
        st.warning("Please enter a question first.")