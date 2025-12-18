from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()
class Item(BaseModel):
    name: str
def read_items(query: Union[None, str] = Query(default = None), skip: int = 0, limit: int = 10):
    items = []
    if query:
        for item in fake_items_db:
            if query.lower() in item.name.lower():
                items.append(item)
    return items
router = APIRouter()
@router.get("/items")
def read_items(query: Union[None, str] = Query(default = None), skip: int = 0, limit: int = 10):
    return read_items(query = query, skip = skip, limit = limit)
