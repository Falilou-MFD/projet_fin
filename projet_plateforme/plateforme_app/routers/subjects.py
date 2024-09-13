from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.subject_model import *
from crud.subject_crud import *
from schemas.subject_schema import *
from database import SessionLocal, engine
from .. import crud_def as crud
from typing import List
from .. import crud, schemas
from ..database import get_db

app = FastAPI()

@app.post("/subjects/", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@app.get("/subjects/", response_model=List[schemas.Subject])
def read_subjects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_subjects(db=db, skip=skip, limit=limit)

@app.get("/subjects/{subject_id}", response_model=schemas.Subject)
def read_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = crud.get_subject(db=db, subject_id=subject_id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

@app.put("/subjects/{subject_id}", response_model=schemas.Subject)
def update_subject(subject_id: int, subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    db_subject = crud.update_subject(db=db, subject_id=subject_id, subject=subject)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject

@app.delete("/subjects/{subject_id}", response_model=schemas.Subject)
def delete_subject(subject_id: int, db: Session = Depends(get_db)):
    db_subject = crud.delete_subject(db=db, subject_id=subject_id)
    if db_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    return db_subject
