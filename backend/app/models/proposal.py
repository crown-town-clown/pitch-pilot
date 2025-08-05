# proposal.py model 

from re import T
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    is_ai_generated = Column(Boolean, default=True)

    project = relationship("Project", back_populates="proposals")