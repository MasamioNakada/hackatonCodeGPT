from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from contextlib import contextmanager
import models
from database import SessionLocal, engine

def get_all_user(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def add_conversation(db: Session, conversation:dict):
    db_conversation = models.Conversation(**conversation)
    db.add(db_conversation)
    db.commit()
    db.refresh(db_conversation)
    return db_conversation

def get_all_conversation(db: Session):
    return db.query(models.Conversation).all()
