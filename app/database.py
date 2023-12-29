from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import find_dotenv, load_dotenv
import os
load_dotenv(find_dotenv())

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
tablename = os.getenv("TABLE_NAME")
host = os.getenv("HOST")

SQLALCHEMY_DATABASE_URL = '{database}://{username}:{password}@{host}/{tablename}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base() 


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()