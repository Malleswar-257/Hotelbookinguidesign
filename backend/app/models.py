from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()
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
    description = Column(String)
    rating = Column(Integer)
class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"))
    type = Column(String)
    price = Column(String)
    capacity = Column(Integer)
class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    room_id = Column(Integer, ForeignKey("rooms.room_id"))
    check_in_date = Column(String)
    check_out_date = Column(String)
def create_user(email: str, password: str, role: str):
    return User(email=email, password=password, role=role)
def create_hotel(name: str, city: str):
    return Hotel(name=name, city=city)
def create_room(type: str, price: str, capacity: int, hotel_id: int):
    return Room(type=type, price=price, capacity=capacity, hotel_id=hotel_id)
def create_booking(user_id: int, room_id: int, check_in_date: str, check_out_date: str):
    return Booking(user_id=user_id, room_id=room_id, check_in_date=check_in_date, check_out_date=check_out_date)