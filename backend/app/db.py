from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.dialects.postgresql import DECIMAL
Base = declarative_base()
engine = create_engine("postgresql://postgres:password@localhost/db")
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
def get_db():    db = SessionLocal()    try:        yield db    finally:        db.close()
class User(Base):    __tablename__ = "users"    user_id = Column(Integer, primary_key=True, index=True)    name = Column(String, required=True)    email = Column(String, unique=True, required=True)    password = Column(String, required=True)    role = Column(String, required=True)
class Hotel(Base):    __tablename__ = "hotels"    hotel_id = Column(Integer, primary_key=True, index=True)    name = Column(String, required=True)    city = Column(String, required=True)    description = Column(DECIMAL, required=True)    rating = Column(Integer, required=True)
class Room(Base):    __tablename__ = "rooms"    room_id = Column(Integer, primary_key=True, index=True)    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), required=True)    type = Column(String, required=True)    price = Column(DECIMAL, required=True)    capacity = Column(Integer, required=True)    availability_count = Column(Integer, required=True)
class Booking(Base):    __tablename__ = "bookings"    booking_id = Column(Integer, primary_key=True, index=True)    user_id = Column(Integer, ForeignKey("users.user_id"), required=True)    room_id = Column(Integer, ForeignKey("rooms.room_id"), required=True)    check_in = Column(DECIMAL, required=True)    check_out = Column(DECIMAL, required=True)    price = Column(DECIMAL, required=True)    status = Column(String, required=True)
