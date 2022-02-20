from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE= "postgresql://postgres:password@localhost/kabum_db"
SQLALCHEMY_DATABASE="postgresql+psycopg2://postgres:password@localhost:5432/kabum_db"

engine= create_engine(SQLALCHEMY_DATABASE)
SessionLocal= sessionmaker(bind=engine)
Base= declarative_base()

def get_session_local():

    session= SessionLocal()
       
    return session