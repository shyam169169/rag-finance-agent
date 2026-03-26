
from app.services.metrics import MetricsService


class LLMService:
    def __init__(self, client, metrics_service: MetricsService):
        self.client = client
        self.metrics_service = metrics_service

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

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        print(response)

        print (response.choices[0].message.content)

        usage = response.usage

        metrics = {
            "input_tokens":usage.prompt_tokens,
            "output_tokens":usage.completion_tokens,
            "total_tokens":usage.total_tokens
        }

        print (metrics)

        self.metrics_service.log(metrics)

        return {
            "answer": response.choices[0].message.content,
            "metrics": metrics
        }
        
