from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/users/{user_id}/items/{item_id}")
async def read_item(user_id: int, item_id: str, q: Union[str, None] = None, short_desc: bool = False):
    item = {"item_id": item_id, "owner": user_id}

    if q:
        item.update({"q": q})
    
    if not short_desc:
        item.update({"description": "This is an amazing item that has a long description"})

    return item

# You can declare multiple path parameters and query parameters at the same time, 
# FastAPI knows which is which.

# And you don't have to declare them in any specific order.