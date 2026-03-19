
class RetrievalService:
    def __init__(self, embedding_service, llm_service):

        """
        embedding_service: handles vector search
        llm_service: handles response generation
        """
        self.embedding_service = embedding_service
        self.llm_service = llm_service

    def query(self, question: str):
        """
        Full RAG pipeline:
        Query → Retrieve → Generate
        """
        #step 1: Retrieve relevant chunks
        chunks = self.embedding_service.search(question)

        #step 2: Generate the response using LLM
        response = self.llm_service.generate(question, chunks)

        return {
            "question": question,
            "chunks": chunks,
            "response": response
        }
