from typing import Optional, List
from sqlalchemy.orm import Session
from datetime import date
from app.models import User, Hotel, Room, Booking, RoomType
from app.schemas import BookRoom

DATABASE_URL = "sqlite:///./app.db"

fake_db = {
    "users": [
        {"id": 1, "username": "user1", "password_hash": "$2b$12$.pZiJhHdR9qLm7UvXwvFuefzV8yVxYs4jBzK.5bQnN3DcG5Zm5J6", "email": "user1@example.com", "is_active": True}
    ],
    "hotels": [
        {"id": 1, "name": "Hotel A", "location": "New York"},
        {"id": 2, "name": "Hotel B", "location": "Los Angeles"}
    ],
    "rooms": [
        {"id": 1, "hotel_id": 1, "type": RoomType.SINGLE.value, "price": 100.0, },
        {"id": 2, "hotel_id": 1, "type": RoomType.DOUBLE.value, "price": 150.0, }
    ],
    "bookings": [
        {"id": 1, "user_id": 1, "hotel_id": 1, "room_type": RoomType.SINGLE.value, "start_date": date(2023, 10, 1), "end_date": date(2023, 10, 5)}
    ]
}

def get_user_by_username(db: Session, username: str):
    return next((user for user in fake_db["users"] if user["username"] == username), None)

def create_user(db: Session, user: UserCreate, password_hash: str):
    new_user = {"id": len(fake_db["users"]) + 1, "username": user.username, "password_hash": password_hash, "email": user.email, "is_active": user.is_active}
    fake_db["users"].append(new_user)
    return new_user

def get_hotels(db: Session, location: Optional[str] = None, start_date: Optional[date] = None, end_date: Optional[date] = None) -> List[dict]:
    hotels = []
    for hotel in fake_db["hotels"]:
        if location and hotel["location"] != location:
            continue
        rooms_booked = [booking for booking in fake_db["bookings"] if booking["hotel_id"] == hotel["id"]]
        if start_date and end_date:
            booked_dates = {date.fromisoformat(booking["start_date"]), date.fromisoformat(booking["end_date"])}
            available_dates = set(range(start_date, end_date + 1)) - booked_dates
            if not available_dates:
                continue
        hotels.append(hotel)
    return hotels

def get_rooms(db: Session, hotel_id: int) -> List[dict]:
    rooms = [room for room in fake_db["rooms"] if room["hotel_id"] == hotel_id]
    return rooms

def create_booking(db: Session, user: User, book: BookRoom) -> dict:
    new_booking = {"id": len(fake_db["bookings"]) + 1, "user_id": user.id, "hotel_id": book.hotel_id, "room_type": book.room_type.value, "start_date": str(book.start_date), "end_date": str(book.end_date)}
    fake_db["bookings"].append(new_booking)
    return new_booking

def cancel_booking(db: Session, user: User, booking_id: int):
    for i, booking in enumerate(fake_db["bookings"]):
        if booking["id"] == booking_id and booking["user_id"] == user.id:
            del fake_db["bookings"][i]
            break