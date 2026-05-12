from app.services.chat_service import ChatService

def get_chat_service() -> ChatService:
    return ChatService()

#her kullanici ayni anda requet atarsa 100 tane ChatService objecti oolur, bunu ilerde duzenle

