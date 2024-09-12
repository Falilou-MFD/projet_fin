from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.profile_model import *
from crud.profile_crud import *
from schemas.profile_schema import *
from database import SessionLocal, engine
import crud_def as crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/profiles", response_model=Profile)
def create_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

@app.get("/profiles/{id}", response_model=Profile)
def fetch_single_profile(id: int, db: Session = Depends(get_db)):
    return crud.get_profile(db, id=id)
