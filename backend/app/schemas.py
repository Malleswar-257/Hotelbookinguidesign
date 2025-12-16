from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    name: str = Field(..., max_length=255)
    email: str = Field(..., max_length=255)
    password: str = Field(..., min_length=8)


class User(BaseModel):
    user_id: int
    name: str
    email: str
    role: str


class Hotel(BaseModel):
    hotel_id: int
    name: str
    city: str
    description: str = None
    rating: int = None


class Room(BaseModel):
    room_id: int
    hotel_id: int
    type: str
    price: float
    capacity: int
    availability_count: int


class Booking(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    check_in: str
    check_out: str
    price: float
    status: str
