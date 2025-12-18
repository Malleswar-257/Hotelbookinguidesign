from sqlalchemy import Column, Integer, String
from database import Base
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)
class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(String, index=True)
    rating = Column(Integer, index=True)
class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, foreign_key="hotels.hotel_id")
    type = Column(String, index=True)
    price = Column(String, index=True)
    capacity = Column(Integer, index=True)
    availability_count = Column(Integer, index=True)
class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, foreign_key="users.user_id")
    room_id = Column(Integer, foreign_key="rooms.room_id")
    check_in = Column(String, index=True)
    check_out = Column(String, index=True)
    price = Column(String, index=True)
    status = Column(String, index=True)