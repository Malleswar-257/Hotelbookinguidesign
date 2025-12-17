from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)

    bookings = relationship("Booking", back_populates="user")

class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(Text, index=True)
    rating = Column(Integer, index=True)

    rooms = relationship("Room", back_populates="hotel")

class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), index=True)
    type = Column(String, index=True)
    price = Column(Integer, index=True)
    capacity = Column(Integer, index=True)
    availability_count = Column(Integer, index=True)

    bookings = relationship("Booking", back_populates="room")

class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), index=True)
    check_in = Column(Date, index=True)
    check_out = Column(Date, index=True)
    price = Column(Integer, index=True)
    status = Column(String, index=True)

    user = relationship("User", back_populates="bookings")
    room = relationship("Room", back_populates="bookings")
