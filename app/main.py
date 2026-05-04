from fastapi import FastAPI
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.routes.llm_routes import router as llm_router

app = FastAPI(title="LLM Healthcare Integration")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

app.include_router(llm_router, prefix="/llm", tags=["LLM"])

@app.get("/")
def root():
    return {"message": "LLM Healthcare API Running"}
