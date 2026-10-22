import streamlit as st
from rag_pipeline import AdvancedRAG

st.set_page_config(page_title="Advanced RAG - System", layout="wide")
st.title("🤖 System Advanced RAG (Local Llama & Qdrant)")

rag = AdvancedRAG()

query = st.text_input("Digite sua consulta na base de conhecimento:")

if st.button("Buscar e Gerar Resposta"):
    if query:
        with st.spinner("Buscando vetores e consultando Llama local..."):
            resposta = rag.query(query)
            st.markdown("### Resposta do RAG:")
            st.write(resposta)
    else:
        st.warning("Por favor, digite uma pergunta.")
