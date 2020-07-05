'''
SQLAlchemy models
'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Binary

Base = declarative_base()

class Client(Base):
    '''
    Class for clients table ORM in hospital authentication DB
    '''
    __tablename__ = 'clients'

    username = Column(String, primary_key=True)
    hashed_pass = Column(Binary)
