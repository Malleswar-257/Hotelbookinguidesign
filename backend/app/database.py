from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
database_url = "postgresql+asyncpg://user:password@localhost/db"
engine = create_async_engine(database_url)
session_local = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)