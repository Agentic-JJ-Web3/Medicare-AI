from pydantic import BaseModel, Field
from datetime import datetime


class HealthCheckResponse(BaseModel):
    status: str 
    timestamp: datetime
    message:str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=1000)
    language: str = Field(default="en", pattern="^(en|fr)$")

class ChatResponse(BaseModel):
    respons: str
    language: str
    timestamp: datetime