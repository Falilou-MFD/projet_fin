from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()



class Admin(Base):
    __tablename__ = "administrations"
    num_admin = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    mdp = Column(String)
    prenom = Column(String)
    nom = Column(String)
    poste = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)