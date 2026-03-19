import pytest
from client.fake_embedding_client import FakeEmbeddingClient
from app.services.embedding import EmbeddingService

def test_embeddings():
    service = EmbeddingService(FakeEmbeddingClient())

    chunks = ["coffee expense : 10", "coffee expense : 20", "grocery shopping"]
    service.add_chunks(chunks)

    results = service.search("coffee", k = 2)

    assert results is not None
    assert len(results) == 2
    assert "coffee" in results[0]


def test_search_empty_str():
    service = EmbeddingService(FakeEmbeddingClient())
    
    results = service.search("coffee")
    assert results == []

    service.add_chunks([])
    results = service.search("coffee")
    assert results == []

def test_embeddings():
    service = EmbeddingService(FakeEmbeddingClient())

    chunks = ["coffee", "tea", "grocery shopping"]
    service.add_chunks(chunks)

    results = service.search("board", k = 1, threshold=.01)
    assert results == []

def test_get_embeddings():
    service = EmbeddingService(FakeEmbeddingClient())
    embedding1=  service.get_embedding("coffee")
    embedding2=  service.get_embedding("tea")

    assert embedding1 != embedding2