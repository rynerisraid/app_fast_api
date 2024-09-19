from typing import Optional
from sqlmodel import Field, SQLModel, Session
from app.database import engine
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True, nullable=False)
    email: str = Field(index=True, nullable=False)
    password: str = Field(nullable=False)
    created_time: Optional[datetime] = Field(default=None, nullable=False)
    updated_time: Optional[datetime] = Field(default=None, nullable=False)

    def __repr__(self) -> str:
        return f"<User username={self.username} email={self.email}>"


SQLModel.metadata.create_all(engine)