from fastapi import APIRouter, Path, Query
from typing_extensions import Annotated

router = APIRouter()

# greater than or equal - ge


@router.get("/items_ge/{item_id}")
async def read_items_greater_or_equal(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=10)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# greater than - gt, less than or equal = le


@router.get("/items_gt_le/{item_id}")
async def read_items_greater_than_and_less_or_equal(
    item_id: Annotated[int, Path(title="The ID of item", gt=5, le=10)], q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# Number validations: floats, greater than and less than


@router.get("/items_float_gt_lt/{item_id}")
async def read_items_float_greater_than_and_less_than(
    item_id: Annotated[int, Path(title="The ID of item", gt=5, le=10)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=1.05)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

# With Query, Path (and others you haven't seen yet) you can declare metadata and 
# string validations in the same ways as with Query Parameters and String Validations.

# And you can also declare numeric validations:

# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal