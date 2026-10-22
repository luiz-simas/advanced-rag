# Advanced RAG System — Local Retrieval-Augmented Generation

A fully **local** RAG (Retrieval-Augmented Generation) pipeline: ingest PDF documents, embed them into a vector database, and answer questions with **Llama 3** running on-device via Ollama — no cloud APIs, no keys, no data leaving the machine.

Originally built to query a biomedical corpus (PubMed literature on the JAK2 gene), but the pipeline is domain-agnostic: drop in any PDFs and ask.

## How it works

1. **Ingest** (`ingest.py`) — loads PDFs from `data/documents/`, splits them into chunks, embeds them with `sentence-transformers` (all-MiniLM-L6-v2), and stores the vectors in **Qdrant**.
2. **Retrieve** (`retriever.py`) — embeds the question and pulls the most relevant chunks from the Qdrant collection.
3. **Generate** (`rag_pipeline.py`) — assembles the retrieved context into a grounded prompt and calls **Llama 3** through the local Ollama API.
4. **Ask** (`app.py`) — a Streamlit chat interface on top of the pipeline.

## Run it

Prerequisites: [Ollama](https://ollama.com) running locally with `llama3` pulled, and Qdrant on `localhost:6333` (e.g., via Docker).

```bash
pip install -r requirements.txt

# 1. Put your PDFs in data/documents/
# 2. Build the vector store
python ingest.py

# 3. Start the interface
streamlit run app.py
```

## Tech

Python · LangChain · Qdrant · sentence-transformers · Ollama / Llama 3 · Streamlit · PyPDF

## Notes

Interface and system prompt are in Portuguese (pt-BR); see `README.pt-BR.md` for the original readme.
