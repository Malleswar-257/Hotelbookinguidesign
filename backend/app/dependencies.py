from sqlalchemy.ext.asyncio import AsyncSession
from app.database import engine
async def get_db() -> AsyncSession:
    async with engine.begin() as conn:
        yield conn