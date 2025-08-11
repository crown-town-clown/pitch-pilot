# invoice.py model 

from sqlalchemy import Column, Integer, ForeignKey, Date, Float, Boolean, Text
from sqlalchemy.orm import relationship
from database import Base

class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    amount = Column(Float, nullable=False)
    due_date = Column(Date, nullable=True)
    paid = Column(Boolean, default=False)
    description = Column(Text, nullable=True)

    project = relationship("Project", back_populates="invoices")