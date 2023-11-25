import os
import uvicorn
import crud
import models
from routers import users
from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine

load_dotenv()
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    uvicorn.run(
        app, host=os.getenv("DEFAULT_HOST"), port=int(os.getenv("DEFAULT_PORT"))
    )
