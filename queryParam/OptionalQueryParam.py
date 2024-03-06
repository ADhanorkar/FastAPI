from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None]=None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}