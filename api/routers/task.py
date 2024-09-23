from fastapi import APIRouter
import api.shemas.task as task_schema

router = APIRouter()

@router.get("/tasks", response_model=list[task_schema.Task])
async def list_tasks():
    return [
        task_schema.Task(id=1, title="Task 1"),
    ]

@router.post("/tasks", response_model=task_schema.TaskCreateResponse)
async def create_task(task_body: task_schema.TaskCreate):
    # (id=1, **task_body.dict()) の部分は、task_bodyの内容を展開して、id=1を追加している
    # (id=1, title=tast_body.title, done=task_body.done) と同義
    return task_schema.TaskCreateResponse(id=1, **task_body.dict())

@router.put("/tasks/{task_id}", response_model=task_schema.TaskCreateResponse)
async def update_tasks(task_id: int, task_body: task_schema.TaskCreate):
    # UPDATEメソッドの処理
    return task_schema.TaskCreateResponse(id=task_id, **task_body.dict())

@router.delete("/tasks/{task_id}", response_model=None)
async def delete_task(task_id: int):
    # DELETEメソッドの処理
    return
