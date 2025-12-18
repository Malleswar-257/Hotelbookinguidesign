from sqlalchemy.orm import Session
from app import models
def get_user_by_email(email: str, db: Session):    return db.query(models.User).filter(models.User.email == email).first()
def create_user(user: models.UserCreate, db: Session):    hashed_password = pwd_context.hash(user.password)    db_user = models.User(name = user.name, email = user.email, password = hashed_password, role = user.role)    db.add(db_user)    db.commit()    db.refresh(db_user)    return db_user
def authenticate_user(email: str, password: str, db: Session):    user = get_user_by_email(email = email, db = db)    if not user or not pwd_context.verify(password, user.password):        return None    return user
def get_hotels(db: Session):    return db.query(models.Hotel).all()
def get_bookings_by_user_id(user_id: int, db: Session):    return db.query(models.Booking).filter(models.Booking.user_id == user_id).all()
def get_all_bookings(db: Session):    return db.query(models.Booking).all()
