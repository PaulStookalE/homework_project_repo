# Створюємо таблицю User.

from .base import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'user_data'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    password = Column(String, nullable=False)
    age = Column(Integer, nullable=False)