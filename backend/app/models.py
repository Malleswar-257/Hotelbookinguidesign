from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User model
class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

# Hotel model
class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String, index=True)
    description = Column(String, index=True)
    rating = Column(Integer, index=True)

# Room model
class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key=True, index=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), index=True)
    type = Column(String, index=True)
    price = Column(Float, index=True)
    capacity = Column(Integer, index=True)
    availability_count = Column(Integer, index=True)

# Booking model
class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), index=True)
    check_in = Column(DateTime, index=True)
    check_out = Column(DateTime, index=True)
    price = Column(Float, index=True)
    status = Column(String, index=True)

Base.metadata.create_all(bind=engine)