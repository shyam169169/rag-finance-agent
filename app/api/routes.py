from fastapi import APIRouter, UploadFile, File, Depends
from fastapi.responses import StreamingResponse
from app.services.ingestion import process_csv
from app.services.retrieval import RetrievalService
from app.services.rate_limiter import RateLimiter

router=APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    return await process_csv(file)

@router.post("/query-stream")
async def query_stream(question: str, retrieval=Depends(RetrievalService), rate_limiter=Depends(RateLimiter)):
    if not rate_limiter.allow("current_user_id")
        return {"error": "Rate limit exceeded"}
    stream_response = retrieval.query(question)
    return StreamingResponse(stream_response, media_type="text/plain")
