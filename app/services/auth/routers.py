from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from . import jwt as jwt_module
from . import password as pwd
from ...schemas.message import Message
from ...schemas.user_schema import UserRegistrationResponse,UserRegistrationSchema
from .services import get_user_by_name,get_user_by_email,create_user
from ...database import session

router = APIRouter()


@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")


# 用户注册
@router.post('/register',response_model=UserRegistrationResponse)
async def register(user: UserRegistrationSchema):

    user_db = await get_user_by_email(session,user.email)
    if user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="邮箱已存在")
    # user_db = await get_user_by_name(session,user.username)
    # if user_db:
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户名已存在")
    
    # hashed_password = pwd.hash_password(user.password)
    # new_user = await create_user(session,user=user,hashed_password=hashed_password)
    
    return UserRegistrationResponse(message="ok",username=user.username)
# 重置密码


# 用户登录

# 用户退出