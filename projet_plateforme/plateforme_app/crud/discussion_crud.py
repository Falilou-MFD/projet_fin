from sqlalchemy.orm import Session
from models.discussion_model import Discussion
from schemas.discussion_schema import DiscussionCreate
from typing import List, Optional
from ..models import Discussion
from ..schemas import DiscussionCreate

def create_discussion(db: Session, discussion: DiscussionCreate) -> Discussion:
    db_discussion = Discussion(**discussion.dict())
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def get_discussion_by_id(db: Session, discussion_id: int) -> Optional[Discussion]:
    return db.query(Discussion).filter(Discussion.id == discussion_id).first()

def get_all_discussions(db: Session) -> List[Discussion]:
    return db.query(Discussion).all()

def update_discussion(db: Session, discussion_id: int, updated_discussion: DiscussionCreate) -> Optional[Discussion]:
    discussion = get_discussion_by_id(db, discussion_id)
    if discussion:
        for key, value in updated_discussion.dict().items():
            setattr(discussion, key, value)
        db.commit()
        db.refresh(discussion)
        return discussion
    return None  # Retourne None si la discussion n'est pas trouvée

def delete_discussion(db: Session, discussion_id: int) -> Optional[Discussion]:
    discussion = get_discussion_by_id(db, discussion_id)
    if discussion:
        db.delete(discussion)
        db.commit()
        return discussion
    return None  # Retourne None si la discussion n'est pas trouvée
