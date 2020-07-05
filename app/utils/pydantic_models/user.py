from pydantic import BaseModel

class User(BaseModel):
    '''
    Class to handle user logins.
    Used by FastAPI to JSONify request
    '''
    username: str
    password: str
