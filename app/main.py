from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="AI financial copilot")
app.include_router(router)