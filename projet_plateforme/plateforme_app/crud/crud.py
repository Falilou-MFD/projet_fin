from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.admin_model import Admin
from projet_plateforme.plateforme_app.schemas.admin_schema import AdminCreate
from projet_plateforme.plateforme_app.auth import get_password_hash

def create_admin(db: Session, admin: AdminCreate):
    hashed_password = get_password_hash(admin.password)  # Hacher le mot de passe
    db_admin = models.Admin(
        num_admin=admin.num_admin,
        name=admin.name,
        email=admin.email,
        hashed_password=hashed_password  # Enregistrer le mot de passe haché
        )
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


from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.forum_user_model import ForumUser
from projet_plateforme.plateforme_app.schemas.forum_user_schema import ForumUserCreate

def create_forum_user(db: Session, forum_user: schemas.ForumUserCreate):
    hashed_password = get_password_hash(forum_user.password)  # Hacher le mot de passe
    db_forum_user = models.ForumUser(
        username=forum_user.username,
        hashed_password=hashed_password  # Enregistrer le mot de passe haché
    )
    db.add(db_forum_user)
    db.commit()
    db.refresh(db_forum_user)
    return db_forum_user

def get_forum_user_by_id(db: Session, user_id: int):
    return db.query(ForumUser).filter(ForumUser.id == user_id).first()

def get_all_forum_users(db: Session):
    return db.query(ForumUser).all()

def update_forum_user(db: Session, user_id: int, updated_forum_user: ForumUserCreate):
    forum_user = get_forum_user_by_id(db, user_id)
    if forum_user:
        for key, value in updated_forum_user.dict().items():
            setattr(forum_user, key, value)
        db.commit()
        db.refresh(forum_user)
    return forum_user

def delete_forum_user(db: Session, user_id: int):
    forum_user = get_forum_user_by_id(db, user_id)
    if forum_user:
        db.delete(forum_user)
        db.commit()
    return forum_user


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


from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.profile_model import Profile
from projet_plateforme.plateforme_app.schemas.profile_schema import ProfileCreate

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


from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.student_model import Student
from projet_plateforme.plateforme_app.schemas.student_schema import StudentCreate

def create_student(db: Session, student: schemas.StudentCreate):
    hashed_password = get_password_hash(student.password)  # Hacher le mot de passe
    db_student = models.Student(
        num_etu=student.num_etu,
        name=student.name,
        email=student.email,
        hashed_password=hashed_password  # Enregistrer le mot de passe haché
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student_by_num_etu(db: Session, num_etu: str):
    return db.query(Student).filter(Student.num_etu == num_etu).first()

def get_all_students(db: Session):
    return db.query(Student).all()

def update_student(db: Session, num_etu: str, updated_student: StudentCreate):
    student = get_student_by_num_etu(db, num_etu)
    if student:
        for key, value in updated_student.dict().items():
            setattr(student, key, value)
        db.commit()
        db.refresh(student)
    return student

def delete_student(db: Session, num_etu: str):
    student = get_student_by_num_etu(db, num_etu)
    if student:
        db.delete(student)
        db.commit()
    return student



from sqlalchemy.orm import Session
from projet_plateforme.plateforme_app.models.subject_model import Subject
from projet_plateforme.plateforme_app.schemas.subject_schema import SubjectCreate

def create_subject(db: Session, subject: SubjectCreate):
    db_subject = Subject(**subject.dict())
    db.add(db_subject)
    db.commit()
    db.refresh(db_subject)
    return db_subject

def get_subject_by_id(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()

def get_all_subjects(db: Session):
    return db.query(Subject).all()

def update_subject(db: Session, subject_id: int, updated_subject: SubjectCreate):
    subject = get_subject_by_id(db, subject_id)
    if subject:
        for key, value in updated_subject.dict().items():
            setattr(subject, key, value)
        db.commit()
        db.refresh(subject)
    return subject

def delete_subject(db: Session, subject_id: int):
    subject = get_subject_by_id(db, subject_id)
    if subject:
        db.delete(subject)
        db.commit()
    return subject
