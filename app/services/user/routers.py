from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from app.services.user import UserService
from app.models.user import User
from app.schemas.message import Message


router = APIRouter()


@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")


# 用户注册
@router.post("/register", response_model=Message)
def register(user: User):
    db_user =  UserService().create_user(user)
    if db_user:
        return Message(message="注册成功")
    else:
        raise HTTPException(status_code=400, detail="注册失败")


# 重置密码


# 用户登录

# 用户退出