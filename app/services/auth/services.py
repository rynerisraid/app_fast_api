from sqlalchemy.ext.asyncio import AsyncSession
from app.models import user
from app.schemas.user_schema import UserRegister



def get_user_by_name(db: AsyncSession, username: str):
    return db.query(user.User).filter(user.User.username == username).first()

def get_user_by_email(db: AsyncSession, email: str):
    return db.query(user.User).filter(user.User.email == email).first()
