from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

router = APIRouter()

@router.post("/items/{item_id}")
async def create_item(item_id: str, item: Item):
    return {"item_id": item_id, **item.dict()}

# Request body + path parameters¶
# You can declare path parameters and request body at the same time.

# FastAPI will recognize that the function parameters that match path 
# parameters should be taken from the path, and that function parameters 
# that are declared to be Pydantic models should be taken from the request body.