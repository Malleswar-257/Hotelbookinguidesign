from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from app.database import Base
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
    disabled = Column(Boolean, default=False)
class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(String)
    rating = Column(Integer)
class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"))
    type = Column(String)
    price = Column(Float)
    capacity = Column(Integer)
    availability_count = Column(Integer)
class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    price = Column(Float)
    status = Column(String)