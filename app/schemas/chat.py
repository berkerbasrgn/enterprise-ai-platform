from pydantic_settings import BaseSettings

class ChatRequest(BaseSettings):
    message: str

class ChatResponse(BaseSettings):
    response: str