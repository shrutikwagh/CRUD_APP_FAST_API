from sqlalchemy import create_engine    # create engine
from sqlalchemy.orm import sessionmaker # sessionmaker
from sqlalchemy.ext.declarative import declarative_base # declarative_base


DB_URL='mysql://username:psw@localhost:3306/db_name'
engine = create_engine(DB_URL)
# Creating a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Defining a Base
Base = declarative_base()