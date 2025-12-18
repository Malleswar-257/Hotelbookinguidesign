from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional, List
from passlib.context import CryptContext
from datetime import datetime
from app import models, schemas, crud, database, security

db = database.get_db()
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/auth/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(db)):    existing_user = crud.get_user_by_email(email=user.email, db=db)    if existing_user:        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")    hashed_password = security.get_password_hash(user.password)    return crud.create_user(user=user, db=db)

@app.post("/auth/login", response_model=schemas.Token)
def login_for_access_token(form_data: schemas.TokenRequestForm, db: Session = Depends(db)):    user = authenticate_user(email=form_data.email, password=form_data.password, db=db)    if not user:        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})    access_token_expires = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE_MINUTES)    access_token = security.create_access_token(data={
    pass  # TODO: Complete implementation
}
)