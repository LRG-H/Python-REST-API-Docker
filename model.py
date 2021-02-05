from pydantic import BaseModel, Schema

class TodoItem(BaseModel):
    title: str = Schema(..., description='Name of todo item', max_length=180)