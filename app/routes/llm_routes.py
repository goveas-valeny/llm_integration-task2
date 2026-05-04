from fastapi import APIRouter, Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.services.llm_service import call_llm
from app.models.schemas import LLMRequest

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)

@router.post("/analyze")
@limiter.limit("5/minute")
async def analyze_patient(request: Request, payload: LLMRequest):
    try:
        response = await call_llm(payload.prompt)
        return {"response": response}
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
