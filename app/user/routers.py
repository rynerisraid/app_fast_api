from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta

from .services import UserService
from .user import User
from app.schemas.message import Message
from app.database import engine

router = APIRouter()


@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")


# 用户注册
@router.post("/register", response_model=Message)
def register(user: User):
    db_user = UserService(engine).create_user(user)
    if db_user:
        return Message(message="注册成功")
    else:
        raise HTTPException(status_code=400, detail="注册失败")


# 重置密码
@router.post("/rest_password", response_model=Message)  
def rest_password():
    pass

# 用户登录
@router.post("/login",response_model=Message)
def login():
    pass

# 用户退出
@router.post("/logout",response_model=Message)
def logout():
    pass
