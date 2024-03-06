from fastapi import APIRouter, Path, Query
from typing import Union
from typing_extensions import Annotated

router = APIRouter()

# Using Path from fastapi
@router.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="Path Parameter", description= "The ID of the item to get")],
    q: Annotated[Union[str, None], Query(alias="item-query")] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
