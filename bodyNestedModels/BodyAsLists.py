from fastapi import APIRouter
from typing import List, Dict
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    name: str
    url: HttpUrl

router = APIRouter()

# Body as Lists
@router.post("/images/multiple")
async def create_multiple_images(images: List[Image]):
    return images

# Body as Dicts
@router.post("/index-weight/")
async def create_index_weight(index_weight: Dict[int, float]):
    return index_weight