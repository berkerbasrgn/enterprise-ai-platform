from fastapi import APIRouter
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = await chat_service.process_message(request.message)
    return ChatResponse(response=response)