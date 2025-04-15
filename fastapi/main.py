from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine
from models import TodoItem, Base
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware


# Create tables in the database
Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://appdevtodoapp.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

# Endpoint to fetch a single todo item by ID
@app.get("/todos/{todo_id}", response_model=TodoItemOut)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return todo

# Endpoint to update a todo item
@app.put("/todos/{todo_id}", response_model=TodoItemOut)
def update_todo(todo_id: int, todo: TodoItemCreate, db: Session = Depends(get_db)):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    db_todo.task = todo.task
    db_todo.description = todo.description
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Endpoint to delete a todo item
@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = db.query(TodoItem).filter(TodoItem.id == todo_id).first()
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo item not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo item deleted successfully"}