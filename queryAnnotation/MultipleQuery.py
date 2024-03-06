from fastapi import APIRouter, Query
from typing import Union, List
from typing_extensions import Annotated

router = APIRouter()

# Optional query list
@router.get("/items_optional/")
async def read_items_optional(q: Annotated[Union[List[str], None], Query()] = None):
    query_items = {"q": q}
    return query_items

# list with pre-defined values
@router.get("/items_query_default_values/")
async def read_items_query_default_values(q: Annotated[List[str], Query()] = ["Hello", "World"]):
    query_items = {"q": q}
    return query_items

# list with blank list
@router.get("/items_query_blank_list/")
async def read_items_query_blank_list(q: Annotated[List[str], Query()] = []):
    query_items = {"q": q}
    return query_items

# list checks the type
@router.get("/items_type_check")
async def read_item_type_check(q: Annotated[List[int], Query()] = []):
    query_items = {"q": q}
    return query_items