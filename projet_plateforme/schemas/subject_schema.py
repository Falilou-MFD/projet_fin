from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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