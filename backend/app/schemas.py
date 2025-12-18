from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class HotelResponse(BaseModel):
    hotel_id: int
    name: str
    rating: int
    status: str

class RoomResponse(BaseModel):
    room_id: int
    hotel_id: int
    price: float
    availability_count: int

class BookingRequest(BaseModel):
    room_id: int
    check_in: date
    check_out: date

class BookingResponse(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    check_in: date
    check_out: date
    price: float
    status: str