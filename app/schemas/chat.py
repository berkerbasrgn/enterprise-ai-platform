from pydantic import BaseModel, Field, field_validator
from typing import Optional
import uuid

class ChatRequest(BaseModel):
    message : str
    conversation_id : Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    max_tokens : Optional[int] = Field(default=1000, ge=1, le=4000)


    @field_validator('message')
    @classmethod
    def message_not_empty(cls, v):
        if not v.strip():
            raise ValueError('message can not be empty')
        return v
    
class ChatResponse(BaseModel):
    response: str
    conversation_id : str
    tokens_used : Optional[int] = None