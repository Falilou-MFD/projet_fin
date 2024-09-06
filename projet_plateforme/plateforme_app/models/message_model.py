from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    discussion_id = Column(Integer, ForeignKey('discussions.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    discussion = relationship("Discussion", back_populates="messages")