from fastapi import APIRouter
from typing import Union

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short_desc: bool = False):
    item = {"item_id": item_id}

    if q:
        item.update({"q":q})

    if not short_desc:
        item.update( {"description": "This is an amazing item that has a long description"})

    return item

# we can also declare bool types, and they will be converted
# test below results
# http://localhost:8000/items/foo?short=1
# or
# http://127.0.0.1:8000/items/foo?short=True
# or 
# http://127.0.0.1:8000/items/foo?short=true
# or
# http://127.0.0.1:8000/items/foo?short=on
# or
# http://127.0.0.1:8000/items/foo?short=yes