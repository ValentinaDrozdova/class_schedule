from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from settings.settings import settings
from .models import BaseModel


engine = create_async_engine(f"postgresql+asyncpg://"
                             f"{settings.DB_USER}:{settings.DB_PASSWORD}@"
                             f"{settings.DB_HOST}/{settings.DB_NAME}",
                             echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False, class_=AsyncSession)


async def init_db():
    async with engine.begin() as conn:
        # await conn.run_sync(BaseModel.metadata.drop_all)
        await conn.run_sync(BaseModel.metadata.create_all)
