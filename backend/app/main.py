from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime
import os
from dotenv import load_dotenv
from app.database import SessionLocal, engine, Base
from app.models import User, Hotel, Room, Booking
from app.schemas import UserCreate, UserLogin, HotelResponse, RoomResponse, BookingRequest, BookingResponse
from sqlalchemy.exc import SQLAlchemyError

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./app.db')
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
token_url = "token"

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email = email)
    except JWTError:
        raise credentials_exception
    user = get_user(db, email = token_data.email)
    if user is None:
        raise credentials_exception
    return user

def create_user(db: Session, user: UserCreate):
    fake_hashed_password = pwd_context.hash(user.password)
    db_user = User(email=user.email, hashed_password=fake_hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_hotels(db: Session, rating: str = None, status: str = None):
    query = db.query(Hotel)
    if rating:
        query = query.filter(Hotel.rating == int(rating))
    if status:
        query = query.filter(Hotel.status == status)
    return query.all()

def get_bookings(db: Session, user_id: int = None, room_id: int = None):
    query = db.query(Booking)
    if user_id:
        query = query.filter(Booking.user_id == user_id)
    if room_id:
        query = query.filter(Booking.room_id == room_id)
    return query.all()

@app.post("/auth/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, email = user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db = db, user = user)

@app.post("/auth/login", response_model=UserResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, email = user.email, password = user.password)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
}
)