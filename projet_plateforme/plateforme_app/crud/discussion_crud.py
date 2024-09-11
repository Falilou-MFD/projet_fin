from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.discussion_model import Discussion
from projet_plateforme.plateforme_app.schemas.discussion_schema import DiscussionCreate

def create_discussion(db: Session, discussion: DiscussionCreate):
    db_discussion = Discussion(**discussion.dict())
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def get_discussion_by_id(db: Session, discussion_id: int):
    return db.query(Discussion).filter(Discussion.id == discussion_id).first()

def get_all_discussions(db: Session):
    return db.query(Discussion).all()

def update_discussion(db: Session, discussion_id: int, updated_discussion: DiscussionCreate):
    discussion = get_discussion_by_id(db, discussion_id)
    if discussion:
        for key, value in updated_discussion.dict().items():
            setattr(discussion, key, value)
        db.commit()
        db.refresh(discussion)
    return discussion

def delete_discussion(db: Session, discussion_id: int):
    discussion = get_discussion_by_id(db, discussion_id)
    if discussion:
        db.delete(discussion)
        db.commit()
    return discussion
