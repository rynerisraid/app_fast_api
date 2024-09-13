from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,Session
from .config import settings


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
async_engine = create_async_engine(DATABASE_URL)
DbSession = sessionmaker(bind=async_engine, expire_on_commit=False,class_=AsyncSession)

session = DbSession()
