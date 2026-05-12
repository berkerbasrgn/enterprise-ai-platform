from sqlalchemy import Column, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import uuid
# Çünkü SQLAlchemy'nin tüm modelleri takip etmesi lazım. Hangi tabloları oluşturacağını, hangilerini güncelleyeceğini bilmesi lazım
# base artik tum modellerin atasi
Base = declarative_base()

class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    message = Column(Text, nullable=False)
    response = Column(Text, nullable=False)
    created_at= Column(DateTime, default=datetime.utcnow)