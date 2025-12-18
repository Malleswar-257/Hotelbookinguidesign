from sqlalchemy.orm import Session from app import models, schemas
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()
def create_hotel(hotel: schemas.HotelCreate, db: Session = Depends(crud.get_db)):
    fake_hashed_password = get_password_hash(hotel.city)
    db_user = models.Hotel(name = hotel.name, city = hotel.city)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_room(room: schemas.RoomCreate, hotel_id: int, db: Session = Depends(crud.get_db)):
    fake_hashed_password = get_password_hash(str(room.price))
    db_user = models.Room(type = room.type, price = room.price, capacity = room.capacity, hotel_id = hotel_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user