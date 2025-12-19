from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from sqlalchemy.orm import Session
from passlib.context import CryptContext
dotenv_path = ".env"
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path)
from app.database import Base, get_db, engine, User, Hotel, Room, Booking, create_tables
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = Settings(DATABASE_URL=os.getenv("DATABASE_URL", "sqlite:///./test.db"))
Base.metadata.create_all(bind=engine)
def authenticate_user(email: str, password: str):
    user = get_user_by_email(db, email=email)
    if not user or not crypt_context.verify(password, user.password):
        return False
    return user
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user
def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
class Token(BaseModel):
    access_token: str
    token_type: str
class TokenData(BaseModel):
    email: Optional[str] = None
class UserCreate(BaseModel):
    name: str = Field(...)
    email: str = Field(...)
    password: str = Field(...)
class HotelCreate(BaseModel):
    name: str = Field(...)
    city: str = Field(...)
    description: Optional[str] = None
    rating: Optional[int] = None
class RoomCreate(BaseModel):
    hotel_id: int = Field(...)
    type: str = Field(...)
    price: float = Field(...)
    capacity: int = Field(...)
    availability_count: Optional[int] = None
class BookingCreate(BaseModel):
    user_id: int = Field(...)
    room_id: int = Field(...)
    check_in: str = Field(...)
    check_out: str = Field(...)
    status: str = Field(...)
class UserOut(BaseModel):
    user_id: int
    name: str
    email: str
class HotelOut(BaseModel):
    hotel_id: int
    name: str
    city: str
db = Depends(get_db)
@app.post("/users", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = crypt_context.hash(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
@app.get("/users", response_model=List[UserOut], status_code=status.HTTP_200_OK)
def read_users(email: Optional[str] = None, rating: Optional[int] = None, status: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(User)
    if email is not None:
        query = query.filter(User.email == email)
    if rating is not None:
        query = query.filter(User.rating == rating)
    if status is not None:
        query = query.filter(User.status == status)
    return query.all()
@app.post("/hotels", response_model=HotelOut, status_code=status.HTTP_201_CREATED)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    db_hotel = Hotel(name=hotel.name, city=hotel.city, description=hotel.description, rating=hotel.rating)
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel
@app.get("/hotels", response_model=List[HotelOut], status_code=status.HTTP_200_OK)
def read_hotels(name: Optional[str] = None, city: Optional[str] = None, rating: Optional[int] = None, db: Session = Depends(get_db)):
    query = db.query(Hotel)
    if name is not None:
        query = query.filter(Hotel.name == name)
    if city is not None:
        query = query.filter(Hotel.city == city)
    if rating is not None:
        query = query.filter(Hotel.rating == rating)
    return query.all()
@app.post("/rooms", response_model=RoomOut, status_code=status.HTTP_201_CREATED)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    db_room = Room(hotel_id=room.hotel_id, type=room.type, price=room.price, capacity=room.capacity, availability_count=room.availability_count)
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room
@app.post("/bookings", response_model=BookingOut, status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    db_booking = Booking(user_id=booking.user_id, room_id=booking.room_id, check_in=booking.check_in, check_out=booking.check_out, price=booking.price, status=booking.status)
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking
@app.get("/bookings", response_model=List[BookingOut], status_code=status.HTTP_200_OK)
def read_bookings(user_id: Optional[int] = None, room_id: Optional[int] = None, check_in: Optional[str] = None, check_out: Optional[str] = None, status: Optional[str] = None, db: Session = Depends(get_db)):
    query = db.query(Booking)
    if user_id is not None:
        query = query.filter(Booking.user_id == user_id)
    if room_id is not None:
        query = query.filter(Booking.room_id == room_id)
    if check_in is not None:
        query = query.filter(Booking.check_in == check_in)
    if check_out is not None:
        query = query.filter(Booking.check_out == check_out)
    if status is not None:
        query = query.filter(Booking.status == status)
    return query.all()
@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
}
)