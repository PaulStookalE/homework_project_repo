# Створюємо таблицю School.

from .base import Base
from sqlalchemy import Column, Integer, String, Float

class School(Base):
    __tablename__ = 'school_data'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Float, nullable=False)
    location = Column(String, nullable=False)
    time_to_come = Column(String, nullable=False)