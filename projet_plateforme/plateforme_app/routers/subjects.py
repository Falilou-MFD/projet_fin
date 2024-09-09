from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from projet_plateforme.plateforme_app.database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/subjects", response_model=schemas.Subject)
def create_subject(subject: schemas.SubjectCreate, db: Session = Depends(get_db)):
    return crud.create_subject(db=db, subject=subject)

@app.get("/subjects/{id}", response_model=schemas.Subject)
def fetch_single_subject(id: int, db: Session = Depends(get_db)):
    return crud.get_subject(db, id=id)