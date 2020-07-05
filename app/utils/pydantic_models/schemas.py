'''
Pydantic DB models
'''

from typing import List, Optional

from pydantic import BaseModel

class ClientBase(BaseModel):
    '''
    Pydantic model for DB client
    '''
    username: str
    password: bytes
