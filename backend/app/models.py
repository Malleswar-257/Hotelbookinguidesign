from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL
from sqlalchemy.orm import relationship
class User(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
class Hotel(Base):
    __tablename__ = "Hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(Text)
    rating = Column(Integer)