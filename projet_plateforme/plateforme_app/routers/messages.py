from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.message_model import *
from crud.message_crud import *
from schemas.message_schema import *
from database import SessionLocal, engine
import crud_def as crud


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/{discussion_id}", response_model=list[Message])
def fetch_discussion_messages(discussion_id: int, db: Session = Depends(get_db)):
    return crud.get_discussion_messages(db, discussion_id=discussion_id)
