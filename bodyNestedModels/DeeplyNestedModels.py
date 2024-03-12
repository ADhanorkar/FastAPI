from fastapi import APIRouter
from typing import Union, List
from pydantic import BaseModel, HttpUrl


class Image(BaseModel):
    name: str
    url: HttpUrl


class Item(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    image: Union[Image, None] = None


class Offer(BaseModel):
    name: str
    desc: Union[str, None] = None
    price: float
    items: List[Item]


router = APIRouter()


@router.post("/offers/")
async def create_offer(offer: Offer):
    return offer
