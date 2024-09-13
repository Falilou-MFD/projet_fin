from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.profile_model import *
from crud.profile_crud import *
from schemas.profile_schema import *
from database import SessionLocal, engine
from .. import crud_def as crud
from typing import List
from .. import crud, schemas

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/profiles/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)

@app.get("/profiles/", response_model=List[schemas.Profile])
def read_profiles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_profiles(db=db, skip=skip, limit=limit)

@app.get("/profiles/{profile_id}", response_model=schemas.Profile)
def read_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.get_profile(db=db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@app.put("/profiles/{profile_id}", response_model=schemas.Profile)
def update_profile(profile_id: int, profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    db_profile = crud.update_profile(db=db, profile_id=profile_id, profile=profile)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile

@app.delete("/profiles/{profile_id}", response_model=schemas.Profile)
def delete_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.delete_profile(db=db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile