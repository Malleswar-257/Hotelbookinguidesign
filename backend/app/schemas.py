from typing import Optional, List
from pydantic import BaseModel, validator
from datetime import date
from decimal import Decimal

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None

class UserCreate(UserBase):
    password: str

    @validator("password")
    def password_must_be_set(cls, v):
        if not v:
            raise ValueError("Password must be set")
        return v

class User(UserBase):
    user_id: int
    hashed_password: str
    role: Optional[str] = None

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    expires_at: Optional[date] = None

class LoginForm(BaseModel):
    username: str
    password: str

class BookingBase(BaseModel):
    check_in: date
    check_out: date
    price: Decimal

class Booking(BookingBase):
    booking_id: int
    user_id: int
    room_id: int
    status: Optional[str] = None

    class Config:
        orm_mode = True

class RoomBase(BaseModel):
    hotel_id: int
    type: str
    price: Decimal
    capacity: int

class Room(RoomBase):
    room_id: int
    availability_count: int

    class Config:
        orm_mode = True
