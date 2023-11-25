from sqlalchemy import Boolean, Column, Integer, String, JSON, TIMESTAMP, Enum
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    nombre = Column(String, index=True)
    apellido = Column(String, index=True)

class Conversation(Base):
    __tablename__ = "conversations"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    conversation_id  = Column(String, index=True)
    role = Column(String, index=True)
    content = Column(String, index=True)