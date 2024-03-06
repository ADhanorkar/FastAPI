from fastapi import APIRouter, Query
from typing import Union
from typing_extensions import Annotated

router = APIRouter()

# Query title and description


@router.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(
        title="Query String",
        description="Query string for the items to search in the database that have a good match",
        min_length=3)] = None):
    results = {"items": [{"item_id": "SB0011"}, {"item_id": "SB0012"}]}
    if q:
        results.update({"q": q})
    return results

# Query Alice param and deprecating param


@router.get("/items_alice/")
async def read_items_alice_param_deprecated(q: Annotated[str, Query(alias="item-query", deprecated=True)] = None):
    results = {"items": [{"item_id": "SB0011"}, {"item_id": "SB0012"}]}
    if q:
        results.update({"q": q})
    return results

# exclude from schema - hidden


@router.get("/items_hidden/")
async def read_items_hidden_query(hidden_query: Annotated[str, Query(include_in_schema=False)] = None):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found / provided"}
