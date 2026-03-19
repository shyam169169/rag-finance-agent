

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

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content