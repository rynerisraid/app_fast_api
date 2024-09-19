from datetime import datetime, timedelta
from ..config import Settings
import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select
from app.user.user import User
from sqlalchemy import Engine
from fastapi import HTTPException


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

    def __init__(self,engine: Engine) -> None:
        self.engine: Engine = engine
        pass

    def create_user(self, user: User) -> User:
        user_res =  self.get_user(user) 
        if user_res is None:
            with Session(self.engine) as session:
                try:
                    session.add(user)
                except Exception as e:
                    raise HTTPException(status_code=400, detail=e)         
                finally:
                    session.commit()
        else:
            raise HTTPException(status_code=400, detail=user_res)
        return user
    

    def get_user(self, user: User) -> User:
        res = None
        with Session(self.engine) as session:
            
            try:
                statement = select(User).where(User.username == user.username)
                user = session.exec(statement).first()
                if user is not None:
                    res = "用户名已存在"
                statement = select(User).where(User.email == user.email)
                user = session.exec(statement).first()
                if user is not None:
                    res = "邮箱已存在"
                statement = select(User).where(User.phone == user.phone)
                user = session.exec(statement).first()
                if user is not None:
                    res = "手机号已存在"
                
            except Exception as e:
                return e
            finally:
                session.commit()
        return res
                
