from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class ForumUser(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    mdp = Column(String)
    prenom = Column(String)
    nom = Column(String)
    role = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)