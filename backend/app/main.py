from fastapi import FastAPI, HTTPException, Depends, Request
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from pydantic_settings import BaseSettings
from app.models import User
from app.auth import authenticate_user, get_current_active_user

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/db"
engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "dev-secret-key-change-in-production"

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app = FastAPI()

@app.post("/auth/register")
async def register_user(request: Request, name: str, email: str, password: str):
# Implement registration logic here
    pass

@app.post("/auth/login")
async def login_user(request: Request, email: str, password: str):
# Implement login logic here
    pass

@app.get("/hotels")
async def get_hotels(current_user: User = Depends(get_current_active_user)):
# Implement hotels retrieval logic here
    pass

@app.get("/bookings")
async def get_bookings(current_user: User = Depends(get_current_active_user)):
# Implement bookings retrieval logic here
    pass
