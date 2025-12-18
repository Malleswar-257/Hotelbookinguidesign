from sqlalchemy.orm import Session
from app import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Users(name=user.name, email=user.email, password=models.get_password_hash(user.password), role='user')
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()

def verify_password(plain_password, hashed_password):
    return models.verify_password(plain_password, hashed_password)