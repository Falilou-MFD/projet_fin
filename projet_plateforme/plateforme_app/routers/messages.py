from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.message_model import *
from crud.message_crud import *
from schemas.message_schema import *
from database import SessionLocal, engine
from .. import crud_def as crud


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages/", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/", response_model=List[schemas.Message])
def read_messages(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_messages(db=db, skip=skip, limit=limit)

@app.get("/messages/{message_id}", response_model=schemas.Message)
def read_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.get_message(db=db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@app.put("/messages/{message_id}", response_model=schemas.Message)
def update_message(message_id: int, message: schemas.MessageCreate, db: Session = Depends(get_db)):
    db_message = crud.update_message(db=db, message_id=message_id, message=message)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message

@app.delete("/messages/{message_id}", response_model=schemas.Message)
def delete_message(message_id: int, db: Session = Depends(get_db)):
    db_message = crud.delete_message(db=db, message_id=message_id)
    if db_message is None:
        raise HTTPException(status_code=404, detail="Message not found")
    return db_message