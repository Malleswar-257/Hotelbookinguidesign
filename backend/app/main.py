from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List, Optional
from db.session import get_db
from schemas import UserCreate, UserResponse, HotelSearchQuery, HotelResponse
from crud import user_crud, hotel_crud
from auth import authenticate_user, create_access_token
from models import User, Hotel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/register", response_model=UserResponse)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    if user_crud.get_user_by_email(db, email=user_data.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = user_crud.create_user(db=db, user_data=user_data)
    return UserResponse.from_orm(user)

@app.post("/login", response_model=UserResponse)
def login_for_access_token(form_data: dict, db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.get('email'), form_data.get('password'))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={
}
)