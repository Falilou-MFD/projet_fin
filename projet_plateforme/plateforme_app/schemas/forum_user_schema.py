from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ForumUserBase(BaseModel):
    email: str
    mdp: str
    prenom: str
    nom: str
    role: str


class ForumUserCreate(ForumUserBase):
    pass

class ForumUserUpdate(BaseModel):
    email: Optional[str]
    mdp: Optional[str]
    prenom: Optional[str]
    nom: Optional[str]
    role: Optional[str]

# Schema for response
class ForumUser(ForumUserBase):
    id: int
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
