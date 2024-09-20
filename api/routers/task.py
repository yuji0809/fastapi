from fastapi import APIRouter
import api.shemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [
        task_schema.Task(id=1, title="Task 1"),
    ]

@router.post("/tasks")
async def create_task():
    # POSTメソッドの処理
    pass

@router.put("/tasks/{task_id}")
async def update_tasks():
    # UPDATEメソッドの処理
    pass

@router.delete("/tasks/{task_id}")
async def delete_task():
    # DELETEメソッドの処理
    pass
