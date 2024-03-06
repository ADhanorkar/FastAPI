from fastapi import APIRouter, Path, Body
from typing import Union
from typing_extensions import Annotated
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

# Path Param, Query Param, Payload Body - together


@router.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title='Item ID', gt=5, le=10)],
    q: Union[str, None] = None,
    item: Union[Item, None] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

# Multiple body parameters


class User(BaseModel):
    userName: str
    full_name: Union[str, None] = None


@router.post("/item_multi_body/{item_id}")
async def update_item_multi_body(
    item_id: int, item: Item, user: User, importance: Annotated[bool, Body()]
):
    return {"item_id": item_id, "item": item, "user": user, "importance": importance}

# Embed Item in request payload body


@router.put("/item_embed/{item_id}")
async def item_embed(
    item_id: int, item: Annotated[Item, Body(embed=True)]
):
    return {"item_id": item_id, "item": item}
