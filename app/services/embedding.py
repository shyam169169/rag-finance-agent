import faiss
import numpy as np

class EmbeddingService:
    def __init__(self, embedding_client, dim=1536):
        """
        embedding_client: OpenAI or mock
        dim: embedding vector size
        """
        self.client = embedding_client
        self.dim = dim
        self.index = faiss.IndexFlatL2(dim)
        self.chunks = []

    def get_embedding(self, text:str):
        """convert text into embeddings"""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        
        return response.data[0].embedding

    def add_chunks(self, chunks):
        """
        Store chunks and their embeddings in vector
        """
        if not chunks:
            return
        embeddings = [self.get_embedding(chunk) for chunk in chunks]
        vectors = np.array(embeddings).astype("float32")
        
        self.index.add(vectors)
        self.chunks.extend(chunks)
    
    def search(self, query: str, k: int = 5, threshold: float = 0.5):
        """
        Retrieve top-k similar chunks.
        """
        if not self.chunks:
            return []
        
        query_embedding = self.get_embedding(query)
        query_vector = np.array([query_embedding]).astype("float32")

        distances, indices = self.index.search(query_vector, k)

        results = []
        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(self.chunks) and dist < threshold:
                results.append(self.chunks[idx])

        return results
