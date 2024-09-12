from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ForumUserBase(BaseModel):
    username: str
    email: str

class ForumUserCreate(ForumUserBase):
    password: str

class ForumUser(ForumUserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True