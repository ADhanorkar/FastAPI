from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

router = APIRouter()

@router.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": "{:.2f}".format(price_with_tax) })
    return item_dict

# Inside of the function, you can access all the attributes of 
# the model object directly and perform the computation