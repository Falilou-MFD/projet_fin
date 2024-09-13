from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    id_utilisateur = Column(Integer, ForeignKey('utilisateurs.id'))
    id_discussion = Column(Integer, ForeignKey('discussions.id'))
    contenu = Column(String)
    creation = Column(DateTime, default=datetime.utcnow)
