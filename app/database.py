from sqlmodel import create_engine
from .config import settings


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

