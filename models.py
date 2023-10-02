# Imports
from sqlalchemy import Column, String, Integer

from db import *

# Tables

# Users
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50))
    password = Column(String(100))