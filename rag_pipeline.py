import requests
from config import OLLAMA_URL, MODEL_NAME
from retriever import VectorRetriever

class AdvancedRAG:
    def __init__(self):
        self.retriever = VectorRetriever()

    def query(self, user_prompt: str) -> str:
        docs = self.retriever.search(user_prompt)
        context = "\n\n".join([d["page_content"] for d in docs])

        system_prompt = "Você é um assistente RAG especializado em medicina e bioinformática."
        full_prompt = f"Contexto:\n{context}\n\nPergunta:\n{user_prompt}\n\nResposta:"

        try:
            res = requests.post(
                f"{OLLAMA_URL}/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": full_prompt,
                    "system": system_prompt,
                    "stream": False
                }
            )
            if res.status_code == 200:
                return res.json().get("response", "")
            return f"Erro na chamada do Ollama: Status {res.status_code}"
        except Exception as e:
            return f"Erro de conexão local: {str(e)}"
