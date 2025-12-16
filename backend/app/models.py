from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.sql.expression import text
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)

class Hotel(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    location = Column(String)

class RoomType(enum.Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    type = Column(String)
    price = Column(Float)
    hotel = relationship("Hotel", back_populates="rooms")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))
    room_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    user = relationship("User", back_populates="bookings")
    hotel = relationship("Hotel", back_populates="bookings")

Hotel.rooms = relationship("Room", back_populates="hotel")
User.bookings = relationship("Booking", back_populates="user")