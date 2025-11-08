from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI(title="Simple Items API")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float


# In-memory storage for simplicity (replace with DB for enhancements)
_items: Dict[int, Item] = {
    1: Item(id=1, name="Sample", description="A sample item", price=9.99)
}


@app.get("/items", response_model=List[Item])
def list_items():
    return list(_items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    item = _items.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if item.id in _items:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    _items[item.id] = item
    return item


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in _items:
        raise HTTPException(status_code=404, detail="Item not found")
    del _items[item_id]
    return


# Run with: uvicorn starter-code:app --reload
