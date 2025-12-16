from sqlalchemy import Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, required=True)
    email = Column(String, unique=True, required=True)
    password = Column(String, required=True)
    role = Column(String, required=True)

class Hotel(Base):
    __tablename__ = "Hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, required=True)
    city = Column(String, required=True)
    description = Column(String, required=True)
    rating = Column(Integer, required=True)

class Room(Base):
    __tablename__ = "Rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("Hotels.hotel_id"), required=True)
    type = Column(String, required=True)
    price = Column(DECIMAL(10,2), required=True)
    capacity = Column(Integer, required=True)
    availability_count = Column(Integer, required=True)

class Booking(Base):
    __tablename__ = "Bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("Users.user_id"), required=True)
    room_id = Column(Integer, ForeignKey("Rooms.room_id"), required=True)
    check_in = Column(Date, required=True)
    check_out = Column(Date, required=True)
    price = Column(DECIMAL(10,2), required=True)
    status = Column(String, required=True)