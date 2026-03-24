import time
from app.services.metrics import metrics_service
class RetrievalService:
    def __init__(self, embedding_service, llm_service):

        """
        embedding_service: handles vector search
        llm_service: handles response generation
        """
        self.embedding_service = embedding_service
        self.llm_service = llm_service

    def query(self, question: str):
        start = time.time()
        """
        Full RAG pipeline:
        Query → Retrieve → Generate
        """
        #step 1: Retrieve relevant chunks
        chunks = self.embedding_service.search(question)
        retrieval_time = time.time() - start

        llm_start = time.time()
        #step 2: Generate the response using LLM and stream the response
        response = self.llm_service.generate(question, chunks)

        llm_time = time.time() - llm_start
        metrics_service.log({
            "retrieval_time": retrieval_time,
            "llim_time": llm_time
        })
        
        return response

        # return {
        #     "question": question,
        #     "chunks": chunks,
        #     "response": response
        # }
