from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import UserCreate, User, Hotel, Room, Booking
from app.database import get_db, create_user, authenticate_user, create_hotel, create_room, get_bookings_by_status_and_rating
from app.auth import get_current_active_user, get_admin_role

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.post("/auth/register", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.post("/bookings", response_model=Booking)
def create_booking(user_id: int, room_id: int, check_in: str, check_out: str, price: float, status: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return create_room(db=db, user_id=user_id, room_id=room_id, check_in=check_in, check_out=check_out, price=price, status=status)

@app.get("/bookings", response_model=list[Booking])
def get_bookings(status: str = None, rating: int = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return get_bookings_by_status_and_rating(db=db, status=status, rating=rating)

@app.get("/hotels", response_model=list[Hotel])
def get_hotels(rating: int = None, status: str = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_active_user)):
    return create_room(db=db, user_id=user_id, room_id=room_id, check_in=check_in, check_out=check_out, price=price, status=status)
