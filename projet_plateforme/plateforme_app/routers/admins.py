from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.admin_model import *
from crud.admin_crud import *
from schemas.admin_schema import *
from database import SessionLocal, engine
import crud_def as crud


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/admins", response_model=Admin)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    return crud.create_admin(db=db, admin=admin)

@app.get("/admins/{num_admin}", response_model=Admin)
def fetch_admin_by_num(num_admin: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_num(db, num_admin=num_admin)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin
