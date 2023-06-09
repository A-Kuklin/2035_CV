from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from core.settings import settings


engine = create_async_engine(settings.db_url, future=True, echo=True)
AsyncSessionFactory = sessionmaker(engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator:
    async with AsyncSessionFactory() as session:
        yield session
