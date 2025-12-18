from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)

class Hotels(Base):
    __tablename__ = "hotels"

    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(Text)
    rating = Column(Integer)

class Rooms(Base):
    __tablename__ = "rooms"

    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"))
    type = Column(String, index=True)
    price = Column(DECIMAL(10, 2), index=True)
    capacity = Column(Integer, index=True)
    availability_count = Column(Integer, index=True)

    hotel = relationship("Hotels", back_populates="rooms")
class Bookings(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    check_in = Column(Date, index=True)
    check_out = Column(Date, index=True)
    price = Column(DECIMAL(10, 2), index=True)
    status = Column(String, index=True)

    user = relationship("Users", back_populates="bookings")
    room = relationship("Rooms", back_populates="bookings")