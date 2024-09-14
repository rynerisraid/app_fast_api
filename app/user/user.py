from typing import Optional
from sqlmodel import Field, SQLModel, Session
from app.database import engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    mail: str
    age: Optional[int] = None


SQLModel.metadata.create_all(engine)