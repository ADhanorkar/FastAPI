from fastapi import APIRouter, Query
from typing_extensions import Annotated
from typing import Union

router = APIRouter()

# Multiple metadata/validations


@router.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(min_length=3, max_length=50)] = None):
    result = {"items": [{"item_id": "SB001"}, {"item_id": "SB002"}]}

    if q:
        result.update({"q": q})

    return result

# Regular Expression Validation


@router.get("/items_regex/")
async def read_items(
    q: Annotated[Union[str, None], Query(
        min_length=3, max_length=50, pattern="^fixedquery$")] = None
):
    result = {"items": [{"item_id": "SB001"}, {"item_id": "SB002"}]}

    if q:
        result.update({"q": q})

    return result

# Optional query param (use of default value None)


@router.get("/items_optional/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = None):
    result = {"items": [{"item_id": "SB001"}, {"item_id": "SB002"}]}

    if q:
        result.update({"q": q})

    return result

# Required query param (use of default value ...)


@router.get("/items_required/")
async def read_items(q: Annotated[str, Query(max_length=50)] = ...):
    result = {"items": [{"item_id": "SB001"}, {"item_id": "SB002"}]}

    if q:
        result.update({"q": q})

    return result


# FastAPI allows you to declare additional information and validation for your parameters.
# Additional validation
# We are going to enforce that even though q is optional, whenever it is provided, its
# length doesn't exceed 50 characters.

# But now, having Query(max_length=50) inside of Annotated, we are telling FastAPI that
# we want it to extract this value from the query parameters (this would have been the
# default anyway 🤷) and that we want to have additional validation for this value (that's
# why we do this, to get the additional validation). 😎

# FastAPI will now:

# Validate the data making sure that the max length is 50 characters
# Show a clear error for the client when the data is not valid
# Document the parameter in the OpenAPI schema path operation (so it will show up in the
# automatic docs UI)


# Add more validations

# You can also add a parameter min_length

# You can define a regular expression pattern that the parameter should match

# /^fixedquery$/ This specific regular expression pattern checks that the received
# parameter value:

# ^: starts with the following characters, doesn't have characters before.
# fixedquery: has the exact value fixedquery.
# $: ends there, doesn't have any more characters after fixedquery.
