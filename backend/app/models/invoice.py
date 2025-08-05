# invoice.py model 

from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(DateTime, nullable=False)
    paid = Column(Boolean, default=False, nullable=False)

    project = relationship("Project", back_populates="invoices")