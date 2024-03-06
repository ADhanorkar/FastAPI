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
async def create_item(item_id, item: Item, q: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    
    if q:
        result.update({"q": q})

    return result


# Request body + path + query parameters
# You can also declare body, path and query parameters, all at the same time.
# FastAPI will recognize each of them and take the data from the correct place.

# The function parameters will be recognized as follows:

# If the parameter is also declared in the path, it will be used as a path parameter.
# If the parameter is of a singular type (like int, float, str, bool, etc) it will be 
# interpreted as a query parameter.
# If the parameter is declared to be of the type of a Pydantic model, it will be 
# interpreted as a request body.