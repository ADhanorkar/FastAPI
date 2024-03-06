from fastapi import APIRouter

router = APIRouter()

# The first one will always be used since the path matches first.

@router.get("/users")
async def read_users():
    return ['User 1', 'User 2']

@router.get("/users")
async def read_users2():
    return ['User 3', 'User 4']

