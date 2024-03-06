from fastapi import APIRouter
from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

router = APIRouter()

@router.post('/items/')
async def create_item(item: Item):
    return item

# When you need to send data from a client (let's say, a browser) 
# to your API, you send it as a request body.

# A request body is data sent by the client to your API. A response 
# body is the data your API sends to the client.

# Your API almost always has to send a response body. But clients 
# don't necessarily need to send request bodies all the time.