from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="CRUD API", version="1.0")

# --- In-Memory Data Store ---
# Initial state with 3 pre-filled tasks
tasks_db = [
    {"id": 1, "task": "Read Documentation", "status": False},
    {"id": 2, "task": "Build CRUD API", "status": True},
    {"id": 3, "task": "Add tests", "status": False}
]

# --- Schemas ---
class Task(BaseModel):
    task: str = Field(..., example="Write unit tests")
    status: bool = Field(default=False, example=False)

class TaskUpdate(BaseModel):
    task: Optional[str] = None
    status: Optional[bool] = None
 
 
# --- Helpers ---
def find_task(task_id: int):
    for t in tasks_db:
        if t["id"] == task_id:
            return t
    return None
 
def next_id():
    return max((t["id"] for t in tasks_db), default=0) + 1
 
# --- Routes ---
@app.get("/", summary="API metadata")
def get_metadata():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}
 
 
@app.get("/tasks", response_model=List[dict], summary="List all tasks")
def get_tasks():
    return tasks_db
 
 
@app.get("/tasks/{task_id}", summary="Get a single task by ID")
def get_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
 
 
@app.post("/tasks", status_code=status.HTTP_201_CREATED, summary="Create a new task")
def create_task(task: Task):
    new_task = {"id": next_id(), "task": task.task, "status": task.status}
    tasks_db.append(new_task)
    return new_task
 
 
@app.put("/tasks/{task_id}", summary="Update an existing task")
def update_task(task_id: int, update: TaskUpdate):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
 
    if update.task is not None:
        task["task"] = update.task
    if update.status is not None:
        task["status"] = update.status
 
    return task
 
 
@app.delete("/tasks/{task_id}", summary="Delete a task")
def delete_task(task_id: int):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
 
    tasks_db.remove(task)
    return {"message": f"Task {task_id} deleted successfully"}