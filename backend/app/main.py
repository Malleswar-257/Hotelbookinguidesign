from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
from typing import List, Optional
from app.schemas import User, UserInDB, Hotel, Room, Booking
from app.database import SessionLocal, engine, get_db, Base
from app.models import User as UserModel, Hotel as HotelModel, Room as RoomModel, Booking as BookingModel

DATABASE_URL = "sqlite:///./app.db"
SECRET_KEY = "dev-secret-key-change-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_router = APIRouter(prefix="/api", tags=["users"])

# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

# Pydantic models / schemas
class UserBase(BaseModel):
    name: str = Field(..., min_length = 1)
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    user_id: int

class HotelBase(BaseModel):
    hotel_id: int
    name: str
    city: str
    description: str
    rating: int

class RoomBase(BaseModel):
    room_id: int
    hotel_id: int
    type: str
    price: float
    capacity: int
    availability_count: int

class BookingBase(BaseModel):
    booking_id: int
    user_id: int
    room_id: int
    check_in: datetime
    check_out: datetime
    price: float
    status: str

# CRUD operations
def get_user(email: str, db: Session = Depends(get_db)):
    return db.query(UserModel).filter(UserModel.email == email).first()

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    user_model = UserModel(**user.dict(), hashed_password = hashed_password)
    db.add(user_model)
    db.commit()
    db.refresh(user_model)
    return user_model

def get_hotel(hotel_id: int, db: Session = Depends(get_db)):
    return db.query(HotelModel).filter(HotelModel.hotel_id == hotel_id).first()

def create_booking(booking: BookingBase, db: Session = Depends(get_db)):
    booking_model = BookingModel(**booking.dict())
    db.add(booking_model)
    db.commit()
    db.refresh(booking_model)
    return booking_model

# Authentication
async def authenticate_user(email: str, password: str):
    user = await get_user(email)
    if not user or not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
else:
    expire = datetime.utcnow() + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
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
    except JWTError:
        raise credentials_exception
    user = await get_user(email = email)
    if user is None:
        raise credentials_exception
    return user

# API endpoints
@api_router.post("/token", response_model=UserInDB)
def login_for_access_token(form_data: UserCreate, db: Session = Depends(get_db)):
    user = await authenticate_user(form_data.email, form_data.password)
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