import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_USER = os.getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "password")
POSTGRES_DB = os.getenv("POSTGRES_DB", "kabum_db")
POSTGRES_DB_HOST = os.getenv("POSTGRES_DB_HOST", "localhost")

SQLALCHEMY_DATABASE = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DB_HOST}:5432/{POSTGRES_DB}"

engine = create_engine(SQLALCHEMY_DATABASE)
SessionLocal = sessionmaker(bind=engine)

def get_session_local():

    session = SessionLocal()
       
    return session
