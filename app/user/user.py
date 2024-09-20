from typing import Optional
from sqlmodel import Field, SQLModel
from app.database import engine
from datetime import datetime


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, unique=True, nullable=True)
    username: str = Field(index=True, nullable=False, unique=True)
    email: str = Field(index=True, nullable=False, unique=True, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: Optional[str] = Field(index=True, nullable=True, unique=True, regex=r"^[1][3,4,5,7,8][0-9]{9}$")
    password: str = Field(nullable=False)
    status: str = Field(default="active")
    is_super_user: bool = Field(default=False)
    token: Optional[str] = Field(default=None, nullable=True)
    created_time: Optional[datetime] = Field(default=datetime.now(), nullable=True)
    updated_time: Optional[datetime] = Field(default=datetime.now(), nullable=True)
    last_login_time: Optional[datetime] = Field(default=None, nullable=True)


    def __repr__(self) -> str:
        return f"<User username={self.username} email={self.email}>"




