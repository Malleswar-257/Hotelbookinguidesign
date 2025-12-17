from sqlalchemy.orm import Session
from models import User, Hotel
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
def create_user(db: Session, user_data: UserCreate):
    hashed_password = user_data.password  # In a real app, hash the password
    user = User(name=user_data.name, email=user_data.email, password=hashed_password, role='user')
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def search_hotels(db: Session, query: HotelSearchQuery):
    hotels = db.query(Hotel).filter(Hotel.city == query.city).all() if query.city else db.query(Hotel).all()
    return hotels