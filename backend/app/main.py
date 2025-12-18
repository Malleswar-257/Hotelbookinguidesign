from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from typing import List, Optional
from databases import Database
from .config import Settings, get_settings, database
from .schemas import UserCreate, User, Hotel, Room, Booking, HotelCreate, RoomCreate, BookingCreate, TokenData
from .models import users_table, hotels_table, rooms_table, bookings_table
db = Database(database)
security = CryptContext(schemes=["bcrypt"], deprecated="auto")
JWT_SECRET_KEY = Settings().SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def verify_password(plain_password, hashed_password):
    return security.verify(plain_password, hashed_password)
def get_user(db: Session, email: str):
    query = users_table.select().where(users_table.c.email == email)
    result = await db.fetch_one(query = query)
    if result:
        return User(**result)
def authenticate_user(email: str, password: str):
    user = get_user(db = db, email = email)
    if not user or not verify_password(password, user.password):
        return False
    return user
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email = email)
    except JWTError:
        raise credentials_exception
    user = get_user(db = db, email = token_data.email)
    if user is None:
        raise credentials_exception
    return user
def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions")
    return current_user@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(user.password)
    new_user = {"name": user.name, "email": user.email, "password": hashed_password, "role": "user"}
    query = users_table.insert().values(new_user)
    await db.execute(query)
    return User(email = user.email)
@app.post("/hotels", status_code=status.HTTP_201_CREATED)
def create_hotel(hotel: HotelCreate, db: Session = Depends(get_db)):
    new_hotel = {"name": hotel.name, "city": hotel.city, "description": hotel.description, "rating": hotel.rating}
    query = hotels_table.insert().values(new_hotel)
    await db.execute(query)
    return Hotel(name = hotel.name, city = hotel.city)
@app.post("/rooms", status_code=status.HTTP_201_CREATED)
def create_room(room: RoomCreate, db: Session = Depends(get_db)):
    new_room = {"hotel_id": room.hotel_id, "type": room.type, "price": room.price, "capacity": room.capacity, "availability_count": room.availability_count}
    query = rooms_table.insert().values(new_room)
    await db.execute(query)
    return Room(hotel_id = room.hotel_id, type = room.type)
@app.post("/bookings", status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    new_booking = {"user_id": booking.user_id, "room_id": booking.room_id, "check_in": booking.check_in, "check_out": booking.check_out, "price": booking.price, "status": booking.status}
    query = bookings_table.insert().values(new_booking)
    await db.execute(query)
    return Booking(user_id = booking.user_id, room_id = booking.room_id)
@app.get("/users", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = users_table.select().offset(skip).limit(limit)
    results = await db.fetch_all(query = query)
    return [User(**result) for result in results]
@app.get("/hotels", response_model=List[Hotel])
def read_hotels(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = hotels_table.select().offset(skip).limit(limit)
    results = await db.fetch_all(query = query)
    return [Hotel(**result) for result in results]
@app.get("/rooms", response_model=List[Room])
def read_rooms(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = rooms_table.select().offset(skip).limit(limit)
    results = await db.fetch_all(query = query)
    return [Room(**result) for result in results]
@app.get("/bookings", response_model=List[Booking])
def read_bookings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = bookings_table.select().offset(skip).limit(limit)
    results = await db.fetch_all(query = query)
    return [Booking(**result) for result in results]