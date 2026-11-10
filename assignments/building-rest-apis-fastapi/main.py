from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str
    description: str
    completed: bool


class Task(TaskCreate):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Task Manager API"}


@app.get("/tasks", response_model=list[Task])
def list_tasks() -> list[Task]:
    # TODO: Return all tasks.
    raise NotImplementedError


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    # TODO: Return the task or raise HTTPException with status 404.
    raise NotImplementedError


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    # TODO: Assign a unique ID, save the task, and return it.
    raise NotImplementedError


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    # TODO: Replace the task data or raise HTTPException with status 404.
    raise NotImplementedError


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    # TODO: Delete the task or raise HTTPException with status 404.
    raise NotImplementedError
