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
    
    def get_chunks(self):
        return self.chunks

    def get_embeddings(self, chunks):
        """convert text into embeddings"""
        response = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=chunks
        )

        embeddings = [d.embedding for d in response.data]
        
        return embeddings

    def add_chunks(self, chunks):
        """
        Store chunks and their embeddings in vector
        """
        if not chunks:
            return
        embeddings = self.get_embeddings(chunks)
        vectors = np.array(embeddings).astype("float32")
        
        self.index.add(vectors)
        self.chunks.extend(chunks)
    
    def search(self, query: str, k: int = 5, threshold: float = 0.5):
        """
        Retrieve top-k similar chunks.
        """
        if not self.chunks:
            print("No chunks to search")
            return []
        
        query_embedding = self.get_embeddings(query)
        query_vector = np.array(query_embedding).astype("float32")

        print("Query vector shape:", query_vector.shape)

        index_search_results = self.index.search(query_vector, k)
        if len(index_search_results) == 2:
            distances, indices = index_search_results
        else:
            raise ValueError(f"Unexpected FAISS output: {index_search_results}")
        
        return [self.chunks[i] for i in indices[0] if 0 <= i < len(self.chunks)]