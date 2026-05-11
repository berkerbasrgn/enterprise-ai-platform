from fastapi import APIRouter, Depends
from app.services.chat_service import ChatService
from app.schemas.chat import ChatRequest, ChatResponse
from app.core.dependencies import get_chat_service

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/chat", response_model = ChatResponse)
async def chat(
    request: ChatRequest,
    chat_service:ChatService = Depends(get_chat_service)
):
    response = await chat_service.process_message(request.message)
    return ChatResponse(response=response)