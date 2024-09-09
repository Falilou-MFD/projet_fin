from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Schéma pour Student
class StudentBase(BaseModel):
    num_etu: str
    name: str
    email: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
