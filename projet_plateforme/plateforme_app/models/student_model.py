from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Student(Base):
    __tablename__ = "etudiants"
    num_etu = Column(Integer, primary_key=True, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    mdp = Column(String)
    prenom = Column(String)
    nom = Column(String)
    dob = Column(String)
    niveau = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)