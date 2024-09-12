from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.subject_model import *
from crud.subject_crud import *
from schemas.subject_schema import *
from database import SessionLocal, engine
import crud_def as crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subjects", response_model=Subject)
def create_subject(subject: SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@app.get("/subjects/{id}", response_model=Subject)
def fetch_single_subject(id: int, db: Session = Depends(get_db)):
    return crud.get_subject(db, id=id)
