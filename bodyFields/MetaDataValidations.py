from fastapi import APIRouter, Body
from typing import Union
from typing_extensions import Annotated
from pydantic import BaseModel, Field

router = APIRouter()


class Item(BaseModel):
    name: str
    desc: Union[str, None] = Field(
        default=None, title="Description of the item", max_length=10)
    price: float = Body(
        gt=2, description="The price must be greater than zero")
    tax: Union[float, None] = None


@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
