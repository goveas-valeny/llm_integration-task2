import httpx
import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

async def call_llm(prompt: str):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a healthcare assistant."},
            {"role": "user", "content": prompt}
        ]
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)
    return response.json()["choices"][0]["message"]["content"]
