from sqlalchemy import Column, Integer, String
from database import Base

class TodoItem(Base):
    __tablename__ = "todo_items"
    id = Column(Integer, primary_key=True, index=True)
    task = Column(String, index=True)
    description = Column(String)
    is_completed = Column(Integer, default=0)  # 0 for incomplete, 1 for complete