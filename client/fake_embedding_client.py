
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