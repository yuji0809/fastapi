from pydantic import BaseModel, Field

# Task Schema
# フィールド名: フィールドの型, Field(デフォルト値, example="example", description="description")
class Task(BaseModel):
    id: int
    title: str | None = Field(None, example="Task Title")
    done: bool = Field(False, example=False, description="Task is done or not")
