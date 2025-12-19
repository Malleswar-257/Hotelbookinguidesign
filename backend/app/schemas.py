from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailStr
    password: str
    role: str = "user"

class UserInDB(User):
    user_id: int

class Hotel(BaseModel):
    hotel_id: int
    name: str
    city: str
    description: str
    rating: int

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
    check_in: datetime
    check_out: datetime
    price: float
    status: str
