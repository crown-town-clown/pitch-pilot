# project.py model 

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    title = Column(String, nullable=False)
    status = Column(String, default="planning", nullable=False)
    deadline = Column(Date, nullable=True)
    description = Column(Text, nullable=True)

    client = relationship("Client", back_populates="projects")
    proposals = relationship("Proposal", back_populates="project")
    invoices = relationship("Invoice", back_populates="project")
    
    