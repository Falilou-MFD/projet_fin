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

@app.post("/profiles", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

@app.get("/profiles/{id}", response_model=schemas.Profile)
def fetch_single_profile(id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db, id=id)