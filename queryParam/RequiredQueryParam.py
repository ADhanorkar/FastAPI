from fastapi import APIRouter

router = APIRouter()

@router.get("/items/{item_id}")
async def read_user_item(item_id: str, needy: str):
    return {"item_id": item_id, "needy": needy}

# When you declare a default value for non-path parameters (for now, 
# we have only seen query parameters), then it is not required.

# If you don't want to add a specific value but just make it optional, 
# set the default as None.

# But when you want to make a query parameter required, 
# you can just not declare any default value.