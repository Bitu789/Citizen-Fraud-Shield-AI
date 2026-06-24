from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fraud_detector import detect_scam

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "FraudShield AI Running"}

@app.post("/check")
def check(message: Message):
    result = detect_scam(message.text)
    return result