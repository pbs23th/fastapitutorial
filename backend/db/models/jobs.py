from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    date_posted = Column(Date, default=func.now())
    username = Column(String(10), nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="jobs")

