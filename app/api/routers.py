from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from app.services.core.ingestion import process_csv
from app.services.core.retrieval import RetrievalService
from app.services.optimize.rate_limiter import RateLimiter
from app.services.metrics import metrics_service
from app.api.dependencies import embedding_service, get_retrieval_service

router=APIRouter()


@router.get("/health")
def get_health():
    return "200 OK"

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    chunks = await process_csv(file)
    print (chunks)
    embedding_service.add_chunks(chunks)


@router.get("/chunks")
def get_chunks():
    return embedding_service.get_chunks()

@router.post("/query")
def query_stream(question: str, retrievalService:RetrievalService=Depends(get_retrieval_service)):
   ## if not rate_limiter.allow("current_user_id"):
    ##    return {"error": "Rate limit exceeded"}
    print(question)
    response = retrievalService.query(question)
    return response

@router.get("/metrics")
def get_metrics():
    return metrics_service.get_all_logs()
