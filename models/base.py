# Створюємо тут всі основні функції і об'єкти для подальшого управління БД.

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

db = create_engine(os.getenv('DATABASE'))

Session = sessionmaker(db)
session = Session()


Base = declarative_base()

def create_db():
    Base.metadata.create_all(db)

def drop_db():
    Base.metadata_drop_all(db)
