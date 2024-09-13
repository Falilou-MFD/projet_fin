from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class StudentBase(BaseModel):
    email: str
    mdp: str
    prenom: str
    nom: str
    dob: str
    niveau: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    num_etu: int
    creation: datetime

    class Config:
        orm_mode = True





# from pydantic import BaseModel

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str | None = None

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str
