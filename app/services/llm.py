from app.services.metrics import metrics_service


class LLMService:
    def __init__(self, client):
        self.client = client

    def generate(self, query, chunks):
        context = "\n".join(chunks)

        prompt = f"""
        You are a financial assistant.

        Context:
        {context}

        Question:
        {query}

        If context is not relevant, say you don't have enough data.
        Give actionable insights.
        """

        stream_response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}],
            stream=True
        )

        usage = stream_response.usage
        metrics_service.log({
            "input_tokens":usage.prompt_tokens,
            "output_tokens":usage.completetion_tokens,
            "total_tokens":usage.total_tokens
        })

        for chunk in stream_response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
