from fastapi import APIRouter

from app.model.model import get_inference
from app.utils.user import User
from app.utils.data import Data

router = APIRouter()
NET_ID = 'localhost:8000'

@router.post('/login')
async def login(user: User):
    pass

@router.post('/signup')
async def signup(user: User):
    pass

@router.post('/predict')
async def infer(data: Data):
    get_inference(data.dict(), NET_ID)
