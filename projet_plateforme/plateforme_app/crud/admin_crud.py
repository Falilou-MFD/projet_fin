from sqlalchemy.orm import Session
from models.admin_model import Admin
from schemas.admin_schema import AdminCreate

def create_admin(db: Session, admin: AdminCreate):
    db_admin = Admin(**admin.dict())
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_admin_by_num(db: Session, num_admin: str):
    return db.query(Admin).filter(Admin.num_admin == num_admin).first()

def get_all_admins(db: Session):
    return db.query(Admin).all()

def update_admin(db: Session, num_admin: str, updated_admin: AdminCreate):
    admin = get_admin_by_num(db, num_admin)
    if admin:
        for key, value in updated_admin.dict().items():
            setattr(admin, key, value)
        db.commit()
        db.refresh(admin)
    return admin

def delete_admin(db: Session, num_admin: str):
    admin = get_admin_by_num(db, num_admin)
    if admin:
        db.delete(admin)
        db.commit()
    return admin
