from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)

class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rating = Column(Integer, nullable=False)
    status = Column(String, nullable=False)

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    availability_count = Column(Integer, default=0)

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), nullable=False)
    check_in = Column(Date, nullable=False)
    check_out = Column(Date, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    status = Column(String, nullable=False)