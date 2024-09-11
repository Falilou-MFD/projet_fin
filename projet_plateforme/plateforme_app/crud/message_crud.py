from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.message_model import Message
from projet_plateforme.plateforme_app.schemas.message_schema import MessageCreate

def create_message(db: Session, message: MessageCreate):
    db_message = Message(**message.dict())
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message

def get_messages_by_discussion(db: Session, discussion_id: int):
    return db.query(Message).filter(Message.discussion_id == discussion_id).all()

def update_message(db: Session, message_id: int, updated_message: MessageCreate):
    message = db.query(Message).filter(Message.id == message_id).first()
    if message:
        for key, value in updated_message.dict().items():
            setattr(message, key, value)
        db.commit()
        db.refresh(message)
    return message

def delete_message(db: Session, message_id: int):
    message = db.query(Message).filter(Message.id == message_id).first()
    if message:
        db.delete(message)
        db.commit()
    return message
