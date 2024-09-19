from .config import settings
from sqlmodel import create_engine

DATABASE_URL = settings.DATABASE_URL
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
