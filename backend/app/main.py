from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class HealthCheck(BaseModel):
    status: str

@app.get("/health", response_model=HealthCheck)
def health_check():
    return HealthCheck(status="OK")


@app.post("/chat")
def chat(request: ChatRequest):
    return {
        "message": f"Received message: {request.message}"
    }