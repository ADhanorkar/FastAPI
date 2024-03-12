from fastapi import APIRouter
from typing import Union, List
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class Image(BaseModel):
    name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    image: Union[Image, None] = None

# Special types and validation


@router.put("/items_special/{item_id}")
async def update_item_sp_types(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# List of SubModels (nested classes)


class Item2(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    images: Union[List[Image], None] = None


@router.put("/items_sub_model_list/{item_id}")
async def update_item_sub_model_list(item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results
