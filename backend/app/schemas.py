from pydantic import BaseModel, Field, EmailStr, validator
from datetime import date
from app.models import RoomType

class UserCreate(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: EmailStr = Field(...)
    is_active: bool = True

class User(UserCreate):
    id: int
    hashed_password: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Hotel(BaseModel):
    id: int
    name: str
    location: str

class HotelList(BaseModel):
    hotels: list[Hotel]

class RoomType(enum.Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"

class RoomRoomType(str, enum.Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    TRIPLE = "Triple"

class Room(BaseModel):
    id: int
    hotel_id: int
    type: RoomRoomType
    price: float

class RoomList(BaseModel):
    room_types: list[Room]

class BookRoom(BaseModel):
    hotel_id: int
    start_date: date
    end_date: date
    room_type: RoomRoomType

class Booking(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_type: RoomRoomType
    start_date: date
    end_date: date

class DeleteBooking(BaseModel):
    message: str