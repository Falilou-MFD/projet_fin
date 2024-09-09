from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models import message_model
from projet_plateforme.plateforme_app.crud import message_crud
from projet_plateforme.plateforme_app.schemas import message_schema
from . import message_model, schemas, crud
from projet_plateforme.plateforme_app.database import SessionLocal, engine

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/messages", response_model=schemas.Message)
def create_message(message: schemas.MessageCreate, db: Session = Depends(get_db)):
    return crud.create_message(db=db, message=message)

@app.get("/messages/{discussion_id}", response_model=list[schemas.Message])
def fetch_discussion_messages(discussion_id: int, db: Session = Depends(get_db)):
    return crud.get_discussion_messages(db, discussion_id=discussion_id)