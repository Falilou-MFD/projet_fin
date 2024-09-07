from sqlalchemy.orm import Session
from models.profile_model import Profile
from schemas.profile_schema import ProfileCreate

def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profile_by_id(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()

def get_all_profiles(db: Session):
    return db.query(Profile).all()

def update_profile(db: Session, profile_id: int, updated_profile: ProfileCreate):
    profile = get_profile_by_id(db, profile_id)
    if profile:
        for key, value in updated_profile.dict().items():
            setattr(profile, key, value)
        db.commit()
        db.refresh(profile)
    return profile

def delete_profile(db: Session, profile_id: int):
    profile = get_profile_by_id(db, profile_id)
    if profile:
        db.delete(profile)
        db.commit()
    return profile
