from pydantic import BaseModel
from datetime import date
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
class UserResponse(BaseModel):
    user_id: int
    name: str
    email: str
class HotelSearchQuery(BaseModel):
    city: Optional[str] = None
class HotelResponse(BaseModel):
    hotel_id: int
    name: str
    city: str
description: str
rating: int