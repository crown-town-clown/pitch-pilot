# proposal.py model 

from re import T
from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Proposal(Base):
    __tablename__ = "proposals"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=True)
    is_ai_generated = Column(Boolean, default=True)

    project = relationship("Project", back_populates="proposals")