from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Profile(Base):
    __tablename__ = "profils"
    id = Column(Integer, primary_key=True, index=True)
    num_etu = Column(Integer, ForeignKey('etudiants.num_etu'))
    annee_exp = Column(String)
    competences = Column(String)
    specialisation = Column(String)
    chemin_cv = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)