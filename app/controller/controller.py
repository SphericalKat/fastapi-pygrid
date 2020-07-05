from fastapi import APIRouter

from app.model import models
from app.utils.pydantic_models.user import User
from app.utils.pydantic_models.data import Data

router = APIRouter()
NET_ID = 'localhost:8000'

@router.post('/login')
async def login(user: User):
    body = user.dict()
    response = models.login(body['username'], body['password'])
    if response['msg'] == 'Success':
        # Add JWT Authentication
        pass

@router.post('/signup')
async def signup(user: User):
    pass

@router.post('/predict')
async def infer(data: Data):
    models.get_inference(data.dict(), NET_ID)
