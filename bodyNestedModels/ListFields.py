from fastapi import APIRouter
from typing import Union, List
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results