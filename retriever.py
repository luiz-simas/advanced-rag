class VectorRetriever:
    def __init__(self, collection_name="pubmed_jak2_docs"):
        self.collection_name = collection_name

    def search(self, query: str, top_k: int = 3):
        # Simulação de busca vetorial local
        return [
            {"page_content": f"Trecho relevante sobre: {query} obtido na base vetorial.", "metadata": {"source": "PubMed_JAK2_Doc.pdf"}}
        ]
