from fastapi import APIRouter, UploadFile, File
from app.services.ingestion import process_csv
from app.services.retrieval import query_rag

router=APIRouter()

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    return await process_csv(file)

@router.post("/query")
async def query(question: str):
    return await query_rag(question)
