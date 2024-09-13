from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Discussion(Base):
    __tablename__ = "discussions"
    id = Column(Integer, primary_key=True, index=True)
    id_utilisateur = Column(Integer, ForeignKey('utilisateurs.id'))
    titre = Column(String)
    sous_titre = Column(String)
    contenu = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)