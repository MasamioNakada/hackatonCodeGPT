import crud
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, HTTPBasicCredentials, HTTPBasic
from sqlalchemy.orm import Session
from database import SessionLocal
from pydantic import BaseModel

router = APIRouter(prefix="/users")

class Conversation(BaseModel):
    username:str
    conversation_id:str
    role:str
    content:str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    users = crud.get_all_user(db)
    return users

@router.post("/conversations")
async def add_conversation(data:Conversation,db:Session = Depends(get_db)):
    res = crud.add_conversation(db,data.dict(exclude_none=True))
    return res

@router.get("/conversations")
async def get_allconv(db:Session = Depends(get_db)):
    res = crud.get_all_conversation(db)
    return res

