from client.fake_services import FakeLLMService, FakeEmbeddingService
from app.services.retrieval import RetrievalService

def test_retrieval_pipeline():
    retrieval = RetrievalService(FakeEmbeddingService(), FakeLLMService())

    result = retrieval.query("Where am I overspending?")

    assert result["question"] == "Where am I overspending?"
    assert len(result["chunks"]) == 2
    assert "Answer based on" in result["response"]