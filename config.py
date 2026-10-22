import os

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "llama3"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333
COLLECTION_NAME = "pubmed_jak2_docs"
DOCS_DIR = os.path.join(os.path.dirname(__file__), "data", "documents")

os.makedirs(DOCS_DIR, exist_ok=True)
