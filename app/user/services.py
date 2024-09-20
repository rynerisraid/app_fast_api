from datetime import datetime, timedelta
from ..config import Settings
import jwt
from passlib.context import CryptContext
from sqlmodel import Session, select
from app.user.user import User
from sqlalchemy import Engine
from fastapi import HTTPException,status


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
        user.password = get_password_hash(user.password)
        if user_res is None:
            with Session(self.engine) as session:
                try:
                    session.add(user)
                except Exception as e:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)         
                finally:
                    session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=user_res)
        user.password = None
        return user
    

    def login(self, user: User) -> User:
        user_res =  self.get_user(user)
        if user_res is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户名或密码错误")
        else:
            if verify_password(user.password, user_res.password):
                token = create_access_token(data=user.username, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
                user_res.token = token
                user_res.last_login_time = datetime.now()
                with Session(self.engine) as session:
                    try:
                        session.add(user_res)
                        session.commit()
                        session.refresh(user_res)    
                    except Exception as e:
                        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
                    finally:
                        user_res.password = None
        return user_res



    def get_user(self, user: User) -> User:
        res = None
        with Session(self.engine) as session:
            
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                    if user_query_res.username == user.username:
                        res = "用户名已存在"
                    elif user_query_res.email == user.email:
                        res = "邮箱已存在"
                    elif user_query_res.phone ==user.phone:
                        res = "手机号已被注册"
                
            except Exception as e:
                return e
            finally:
                session.commit()
        return res
    
    def is_super_user(self, user:User) -> bool:
        res = False
        with Session(self.engine) as session:
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                    if user_query_res.is_super_user == True:
                        res = True
                session.add(user_query_res)
                session.commit()
                session.refresh(user_query_res)
            except Exception as e:
                return e

               
        return res
    
    def get_user_state(self, user:User) -> User:
        res = False
        with Session(self.engine) as session:
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                        res = user_query_res.status
            except Exception as e:
                return e
            finally:
                session.commit()
        return res

    
    def set_user_inactive(self, user:User) -> User:
        with Session(self.engine) as session:
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                    user_query_res.is_active = False
                user_query_res.status = 'inactive'
                session.add(user_query_res)
                session.commit()
                session.refresh(user_query_res)  
            except Exception as e:
                return e
        return True
    
    def set_user_active(self, user:User) -> User:
        with Session(self.engine) as session:
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                    user_query_res.is_active = False
            except Exception as e:
                return e
            finally:
                user_query_res.status = 'active'
                session.add(user_query_res)
                session.commit()
                session.refresh(user_query_res)        
        return True


    def verify_password(self, user: User) -> bool:
        with Session(self.engine) as session:
            try:
                statement = select(User).where(User.username == user.username or User.email == user.email or User.phone == user.phone)
                user_query_res = session.exec(statement).first()
                if user_query_res is not None:
                    if verify_password(user.password, user_query_res.password):
                        return True
            except Exception as e:
                return e
            finally:
                session.commit()
        return False