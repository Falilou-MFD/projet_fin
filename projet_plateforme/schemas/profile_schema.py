from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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