from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE="postgresql+psycopg2://postgres:password@localhost:5432/kabum_db"

engine= create_engine(SQLALCHEMY_DATABASE)
SessionLocal= sessionmaker(bind=engine)

def get_session_local():

    session= SessionLocal()
       
    return session
