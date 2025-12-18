from pydantic import BaseModel
from typing import Optional, List
from datetime import date
class UserCreate(BaseModel):    name: str    email: str    password: str    role: str = "user"
class Token(BaseModel):    access_token: str    token_type: str = "bearer"
class TokenRequestForm(BaseModel):    email: str    password: str
class Hotel(BaseModel):    hotel_id: int    name: str    city: str    description: float    rating: int
class Room(BaseModel):    room_id: int    hotel_id: int    type: str    price: float    capacity: int    availability_count: int
class Booking(BaseModel):    booking_id: int    user_id: int    room_id: int    check_in: date    check_out: date    price: float    status: str

    pass  # TODO: Complete implementation