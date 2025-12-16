from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy_utils import database_exists, create_database
db_url = "postgresql://user:password@localhost/dbname"
echo = False
engine = create_engine(db_url, echo = echo)
SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

if not database_exists(engine.url):
    create_database(engine.url)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255), nullable = False)
    email = Column(String(255), unique = True, index = True, nullable = False)
    password = Column(String(255), nullable = False)
    role = Column(String(50), nullable = False)


class Hotel(Base):
    __tablename__ = "hotels"
    hotel_id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255), nullable = False)
    city = Column(String(255), nullable = False)
    description = Column(String(1000))
    rating = Column(Integer)


class Room(Base):
    __tablename__ = "rooms"
    room_id = Column(Integer, primary_key = True, index = True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), nullable=False)
    type = Column(String(255), nullable = False)
    price = Column(DECIMAL(10, 2), nullable = False)
    capacity = Column(Integer, nullable = False)
    availability_count = Column(Integer, nullable = False)


class Booking(Base):
    __tablename__ = "bookings"
    booking_id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    room_id = Column(Integer, ForeignKey("rooms.room_id"), nullable=False)
    check_in = Column(Date, nullable = False)
    check_out = Column(Date, nullable = False)
    price = Column(DECIMAL(10, 2), nullable = False)
    status = Column(String(50), nullable = False)

Base.metadata.create_all(bind = engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
finally:
    db.close()

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password, role="user")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from sqlalchemy.orm import joinedload
from datetime import date
import json
def create_room(db: Session, user_id: int, room_id: int, check_in: str, check_out: str, price: float, status: str):
    start_date = date.fromisoformat(check_in)
    end_date = date.fromisoformat(check_out)
    booking_days = (end_date - start_date).days + 1
    room = db.query(Room).filter_by(room_id = room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Room not found")
    if room.availability_count < booking_days:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Not enough availability")
    booking = Booking(user_id = user_id, room_id = room_id, check_in = start_date, check_out = end_date, price = price * booking_days, status = status)
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking

def get_bookings_by_status_and_rating(db: Session, status: str = None, rating: int = None):
    query = db.query(Booking).options(joinedload(Booking.user), joinedload(Booking.room)).filter(Bookings.status == status)
    if rating is not None:
        query = query.filter(Hotel.rating >= rating)
    return query.all()
