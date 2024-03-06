from fastapi import APIRouter

router = APIRouter()

# if we change order of below routes only "/users/{user_id}" will execute always

@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@router.get("/users/{user_id}")
async def read_user_me(user_id:str):
    return {"user_id": user_id}