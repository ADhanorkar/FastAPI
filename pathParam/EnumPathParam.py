from fastapi import APIRouter
from enum import Enum

class AIModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

router = APIRouter()

@router.get("/models/{model_name}")
async def get_model(model_name: AIModelName):
    if model_name is AIModelName.alexnet:
        return {"model_name": model_name, "message": "deep learning FTW!"}
    
    if model_name.value is 'lenet':
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}