from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # Import the Base class from database.py

class TodoItem(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    description = Column(String)
    is_completed = Column(Boolean, default=False)  # This is the new field