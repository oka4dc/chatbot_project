# app/api/routes.py
from fastapi import APIRouter, HTTPException
from api.schema import ChatRequest
import openai
import os

# Initialize router
router = APIRouter()

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")


# Chatbot route
@router.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=request.message,
            max_tokens=50
        )
        answer = response.choices[0].text.strip()
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Chatbot error occurred.")
