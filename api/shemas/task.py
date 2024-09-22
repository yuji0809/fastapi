from pydantic import BaseModel, Field

# Task Schema
# フィールド名: フィールドの型, Field(デフォルト値, example="example", description="description")
class TaskBase(BaseModel):
    title: str | None = Field(None, example="Task Title")

class TaskCreate(TaskBase):
    ## TaskBaseと同じフィールド(titile)のみなので、passしてる
    pass

class TaskCreateResponse(TaskCreate):
    id: int

    # ORMのオブジェクトをPydanticモデルに変換するための設定（簡単に言えばORMを使った時のデータ取得やらを簡単にするための設定）
    # https://pydantic-docs.helpmanual.io/usage/model_config/
    # 
    # ORMを使っている場合、データベースから取得するデータは辞書ではなく、オブジェクトで返ってくる
    # そのため、ORMのオブジェクトを辞書に変換するために、Configクラスを使っている
    class Config:
        orm_mode = True

class Task(TaskBase):
    id: int
    done: bool = Field(False, example=False, description="Task is done or not")

    class Config:
        orm_mode = True
