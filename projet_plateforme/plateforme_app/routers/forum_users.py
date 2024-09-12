from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from ..models.forum_user_model import *
from ..crud.forum_user_crud import *
from ..database import SessionLocal, engine
from .. import crud_def as crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/forum/users", response_model=ForumUser)
def create_forum_user(forum_user: ForumUserCreate, db: Session = Depends(get_db)):
    return crud.create_forum_user(db=db, forum_user=forum_user)

@app.get("/forum/users/{id}", response_model=ForumUser)
def fetch_forum_user(id: int, db: Session = Depends(get_db)):
    return crud.get_forum_user(db, id=id)
