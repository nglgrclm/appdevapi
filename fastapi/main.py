from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine
from models import TodoItem, Base

# Create tables in the database
Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model to use in FastAPI request and response
class TodoItemCreate(BaseModel):
    task: str
    description: str
class TodoItemOut(TodoItemCreate):
    id: int
    is_completed: int
    class Config:
        orm_mode = True

# Endpoint to fetch all todo items
@app.get("/todos", response_model=List[TodoItemOut])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoItem).all()
    return todos

# Endpoint to add a new todo item
@app.post("/todos", response_model=TodoItemOut)
def add_todo(todo: TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = TodoItem(task=todo.task, description=todo.description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo