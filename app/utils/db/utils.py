from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def connect_to_db(DB_URL):
    '''
    Returns db session
    '''
    engine = create_engine(
        DB_URL, connect_args={'check_same_thread': False}
    )
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session_local
