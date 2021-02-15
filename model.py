from pydantic import BaseModel, Field

class TodoItem(BaseModel):
    title: str = Field(..., description='Name of todo item', max_length=180)
    id: int