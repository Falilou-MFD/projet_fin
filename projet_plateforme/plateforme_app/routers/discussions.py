from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.discussion_model import *
from crud.discussion_crud import *
from schemas.discussion_schema import *
from database import SessionLocal, engine
import crud_def as crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/discussions", response_model= Discussion)
def create_discussion(discussion:  DiscussionCreate, db: Session = Depends(get_db)):
    return crud.create_discussion(db=db, discussion=discussion)

@app.get("/discussions/{id}", response_model= Discussion)
def fetch_single_discussion(id: int, db: Session = Depends(get_db)):
    return crud.get_discussion(db, id=id)
