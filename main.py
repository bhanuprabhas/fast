from fastapi import FastAPI

app_first = FastAPI()

@app_first.get('/')
def home():
    return {'name':'bhanu'} 

# @app_first.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

@app_first.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}


from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app_first.post("/items/")
def create_item(item: Item):
    return item


from fastapi import HTTPException

@app_first.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id >= 42:
        raise HTTPException(status_code=418, detail="Item not found")
    return {"item_id": item_id}