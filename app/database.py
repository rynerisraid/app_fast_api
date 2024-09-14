from sqlmodel import create_engine
from .config import settings
from sqlalchemy.orm import Session


DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)

