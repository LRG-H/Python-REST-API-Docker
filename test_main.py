from fastapi.testclient import TestClient
from main import app
from typing import Optional
from fastapi import FastAPI, HTTPException
from model import TodoItem

client = TestClient(app)
fake_db = [
    {
        "id": 1,
        "title": "Finish homework for Pexon",
        "priority": 1
    },
    {
        "id": 2,
        "title": "Check homework for Pexon",
        "priority": 2
    },
    {
        "id": 3,
        "title": "White unit test for homework",
        "priority": 3
    },
    {
        "id": 4,
        "title": "push homework to repository",
        "priority": 4
    },
    {
        "id": 5,
        "title": "Create Dockerfile for homework",
        "priority": 5
    }
]
# app = FastAPI()

# class TodoItem(BaseModel):
#     id: int
#     title: str
#     description: Optional[str] = None

#     @classmethod
#     def setUpClass(cls):
#         print('setupClass')

#     @classmethod
#     def tearDownClass(cls):
#         print('teardownclass')

#     def setUp(self):
#         print('setUp')
#         self.todo_1 = TodoItem('Remember to finish the Pexon homework')

# def test_get_all():
#     response = client.get("/todos")
#     assert response.status_code == 404
#     assert response.json() == TODOS[0:limit]

@app.get("/todos", response_model=TodoItem)
async def test_read_todos():
    if todo.id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db

# def test_get_by_id():
#     response = client.get("/todos/{id}")
#     assert response.status_code == 422
#     assert response.json() == TODOS[todo_id - 1]

@app.get("/todos/{id}", response_model=TodoItem)
async def read_todo(id: int):
    if todo.id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return fake_db[todo.id]

# def test_post():
#     response = client.post("/todos")
#     assert response.status_code == 422
#     assert response.json() == item

@app.post("/todos", response_model=TodoItem)
async def create_item(item: TodoItem,):
    if todo.id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[todo.id] = todo
    return todo

# def test_put():
#     response = client.put("/todos/{id}")
#     assert response.status_code == 200
#     assert response.json() ==