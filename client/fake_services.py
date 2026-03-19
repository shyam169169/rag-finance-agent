
class FakeEmbeddingClient:
    class embeddings:
        @staticmethod
        def create(model, input):
            base = sum(ord(c) for c in input) % 100
            vector = [base / 100.0] * 1536

            return type("obj", (), {
                "data": [
                    type("obj", (), {"embedding": vector})
                ]
            })
    

class FakeEmbeddingService:
    def search(self, query, k=5):
        return ["coffee expense", "grocery shopping"]


class FakeLLMService:
    def generate(self, query, chunks):
        return f"Answer based on {len(chunks)} chunks"