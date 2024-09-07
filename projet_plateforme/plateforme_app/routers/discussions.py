from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/discussions", response_model=schemas.Discussion)
def create_discussion(discussion: schemas.DiscussionCreate, db: Session = Depends(get_db)):
    return crud.create_discussion(db=db, discussion=discussion)

@app.get("/discussions/{id}", response_model=schemas.Discussion)
def fetch_single_discussion(id: int, db: Session = Depends(get_db)):
    return crud.get_discussion(db, id=id)