from sqlmodel import create_engine
from .config import settings
from sqlmodel import Field, Session, SQLModel, create_engine


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)


