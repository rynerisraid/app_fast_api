from datetime import datetime, timedelta
from ..config import Settings
import jwt
from passlib.context import CryptContext
from sqlmodel import Session
from app.user.user import User


SECRET_KEY = Settings().SECRET_KEY
ALGORITHM = Settings().JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = Settings().JWT_ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)




class UserService:

    def __init__(self,engine) -> None:
        self.engine = engine
        pass

    def create_user(self, user: User) -> User:
        with Session(self.engine) as session:
            session.add(user)
            session.commit()
        return user
    
    def update_user(self, user: User) -> User:
        with Session(self.engine ) as session:
            pass

        