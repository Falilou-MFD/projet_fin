from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Subject(Base):
    __tablename__ = "sujets"
    id = Column(Integer, primary_key=True, index=True)
    chemin = Column(String)
    module= Column(String)
    niveau = Column(String)
    enseignant = Column(String)
    annee_pub = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)