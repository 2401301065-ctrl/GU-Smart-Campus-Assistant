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

        response = chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        st.subheader("Answer")

        st.write(response.content)

        st.subheader("Retrieved Sources")

        for i, doc in enumerate(docs, 1):
            st.markdown(f"### Source {i}")
            st.write(doc.page_content[:400])