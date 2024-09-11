from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AdminBase(BaseModel):
    num_admin: str
    name: str
    email: str

class AdminCreate(AdminBase):
    password = str

class Admin(AdminBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class DiscussionBase(BaseModel):
    title: str
    content: str

class DiscussionCreate(DiscussionBase):
    pass

class Discussion(DiscussionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class ForumUserBase(BaseModel):
    username: str
    created_at : datetime


class ForumUserCreate(ForumUserBase):
    password = str

class ForumUser(ForumUserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class MessageBase(BaseModel):
    content: str
    discussion_id: int

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ProfileBase(BaseModel):
    bio: str
    student_id: int

class ProfileCreate(ProfileBase):
    pass

class Profile(ProfileBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Schéma pour Student
class StudentBase(BaseModel):
    num_etu: str
    name: str
    email: str

class StudentCreate(StudentBase):
    password = str

class Student(StudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class SubjectBase(BaseModel):
    title: str
    description: str

class SubjectCreate(SubjectBase):
    pass

class Subject(SubjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str
