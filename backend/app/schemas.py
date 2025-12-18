from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from sqlalchemy.orm import Session
from app.database import Base

class UserBase(BaseModel):
    name: str
    email: str
    password: str
class UserCreate(UserBase):
    pass
class User(UserBase):
    user_id: int
    role: str

    class Config:
        orm_mode = True
class HotelBase(BaseModel):
    name: str
    city: str
dclass HotelCreate(HotelBase):
    description: Optional[str]
    rating: Optional[int]
class Hotel(HotelBase):
    hotel_id: int
    description: Optional[str] = None
    rating: Optional[int] = None
    rooms: list["Room"] = []

    class Config:
        orm_mode = True
class RoomBase(BaseModel):
    type: str
    price: float
    capacity: int
    availability_count: int
class RoomCreate(RoomBase):
    hotel_id: int
class Room(RoomBase):
    room_id: int
    hotel_id: int
    hotel: "Hotel"
    bookings: list["Booking"] = []

    class Config:
        orm_mode = True
class BookingBase(BaseModel):
    check_in: date
    check_out: date
class BookingCreate(BookingBase):
    user_id: int
    room_id: int
class Booking(BookingBase):
    booking_id: int
    user_id: int
    room_id: int
    price: float
    status: str
    user: "User"
    room: "Room"

    class Config:
        orm_mode = True