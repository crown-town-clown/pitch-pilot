# client.py model 

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String, nullable=False)
    email = Column(String)
    company = Column(String)
    notes = Column(Text)

    user = relationship("User", back_populates="clients")
    projects = relationship("Project", back_populates="client", cascade="all, delete-orphan")