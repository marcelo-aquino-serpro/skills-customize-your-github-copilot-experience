from typing import Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="FastAPI REST APIs")


class ItemBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    description: Optional[str] = Field(default=None, max_length=300)
    category: str = Field(min_length=1, max_length=50)


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int


items = [
    Item(id=1, name="Intro to APIs", description="Learn how REST APIs work", category="education"),
    Item(id=2, name="FastAPI Starter", description="Build endpoints with FastAPI", category="education"),
]
next_item_id = 3


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items(category: Optional[str] = None):
    """Return all items, optionally filtered by category."""
    # TODO: return the full list or filter by category when provided.
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Return a single item by id."""
    # TODO: find the item and raise a 404 error if it does not exist.
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate):
    """Create a new item."""
    global next_item_id

    # TODO: append the new item to the in-memory collection.
    new_item = Item(id=next_item_id, **payload.model_dump())
    next_item_id += 1
    items.append(new_item)
    return new_item


@app.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemCreate):
    """Update an existing item."""
    # TODO: replace the matching item or raise a 404 error.
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_item = Item(id=item_id, **payload.model_dump())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    """Delete an existing item."""
    # TODO: remove the item and return an empty response body.
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
