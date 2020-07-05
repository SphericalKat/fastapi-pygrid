from sqlalchemy.orm import Session
import bcrypt

from app.utils.db import schemas as db_schemas
from app.utils.pydantic_models import schemas as py_schemas

def get_client(db: Session, username: str):
    '''
    Retrieve client from database
    '''
    return db.query(db_schemas.Client).filter(
        db_schemas.Client.username == username
        ).first()

def create_client(db: Session, client: py_schemas.ClientBase):
    '''
    Register client onto database
    '''
    hashed_pw = bcrypt.hashpw(client.password, salt=bcrypt.gensalt())
    db_client = db_schemas.Client(user=client.username, hashed_pass=hashed_pw)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def authenticate_client(db: Session, client: py_schemas.ClientBase):
    '''
    Authenticate client creds with stored DB creds.
    Returns True if creds match, False otherwise.
    '''
    stored_hash = get_client(db, client.username).hashed_pass
    return bcrypt.checkpw(client.password, stored_hash)
