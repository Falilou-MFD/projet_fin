from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AdminBase(BaseModel):
    num_admin: str
    name: str
    email: str

class AdminCreate(AdminBase):
    pass

class Admin(AdminBase):
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
