from app.services.metrics.metrics import metrics_service
from app.services.core.llm import LLMService
from app.services.persistance.embedding import EmbeddingService
from app.services.core.retrieval import RetrievalService
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

openai_client = OpenAI(api_key=openai_api_key)
embedding_service = EmbeddingService(openai_client)
llm_service = LLMService(openai_client, metrics_service)
retrieval_service = RetrievalService(
    embedding_service=embedding_service,
    llm_service=llm_service
)

async def get_retrieval_service():
    return retrieval_service