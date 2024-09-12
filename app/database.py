from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker
from .config import settings


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
async_engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(
    async_engine, expire_on_commit=False, class_=AsyncSession
)