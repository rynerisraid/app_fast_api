from typing import Optional
from sqlmodel import Field, SQLModel, Session
from app.database import engine


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


def create_user(user: User, session: Session) -> User:
    with Session(engine) as session:
        session.add(user)
