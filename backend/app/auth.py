from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic_settings import BaseSettings
from app.models import User
from app.security import verify_password, get_user_by_email
from app.dependencies import get_db

class Settings(BaseSettings):
    SECRET_KEY: str = "dev-secret-key-change-in-production"

async def authenticate_user(email: str, password: str, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_email(email, db)
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_current_active_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token_data = jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])
    email: str = token_data.get("sub")
    if email is None:
        raise credentials_exception
    user = await get_user_by_email(email, db)
    if user is None:
        raise credentials_exception
    return user
