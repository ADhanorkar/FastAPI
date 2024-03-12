from fastapi import APIRouter
from typing import Union, Set
from pydantic import BaseModel

router = APIRouter()


class Image(BaseModel):
    name: str
    url: str


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
