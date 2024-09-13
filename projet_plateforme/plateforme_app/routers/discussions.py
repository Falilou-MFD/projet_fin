from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.discussion_model import *
from crud.discussion_crud import *
from schemas.discussion_schema import *
from database import SessionLocal, engine
from .. import crud_def as crud

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db


@app.put("/discussions/{id}", response_model=schemas.Discussion)
def update_discussion_endpoint(id: int, updated_discussion: schemas.DiscussionCreate, db: Session = Depends(get_db)):
    discussion = crud.update_discussion(db, discussion_id=id, updated_discussion=updated_discussion)
    if discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return discussion

@app.delete("/discussions/{id}", response_model=schemas.Discussion)
def delete_discussion_endpoint(id: int, db: Session = Depends(get_db)):
    discussion = crud.delete_discussion(db, discussion_id=id)
    if discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return discussion
