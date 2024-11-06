# app/main.py
from fastapi import FastAPI
from app.api.route import router as chat_router
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = FastAPI()

# Include the router from routes.py
app.include_router(chat_router)
