from app.core.logging import logger



class ChatService:
    async def process_message(self, message:str) -> str:
        # Placeholder for actual AI processing logic
        logger.info(f"Processing message: {message}")
        return f"you said: {message}"
    

    ## ilerde burda Azure Openai call, rag, vectorsearch , agent workflow
    #  gibi bir entegrasyon yapabiliriz.