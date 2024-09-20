from fastapi import APIRouter, HTTPException, status, Cache
from datetime import datetime, timedelta

from .services import UserService
from .user import User
from app.schemas.message import Message
from app.schemas.form import *
from app.database import engine
from app.schemas.info import ResponseInfo
from fastapi_cache import cached, CacheKey, CacheType

router = APIRouter()

@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")

# 用户注册
@router.post("/register", response_model=ResponseInfo)
def register(user: User):
    db_user = UserService(engine).create_user(user)
    if db_user:
        return ResponseInfo(status_code=status.HTTP_200_OK,message="注册成功",data={user})
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="注册失败")

# 用户登录
@router.post("/login",response_model=ResponseInfo)
def login(login_form: LoginForm):
    user = User(username= login_form.username, password= login_form.password)
    db_user = UserService(engine).login(user)
    if db_user:
        return ResponseInfo(status_code=status.HTTP_200_OK,message="登录成功",data={'token':user.token})
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="登录失败")

# 重置密码
@router.post("/gen_code", response_model=ResponseInfo)
def gen_code(gen_code_form: GenRestCodeForm):
    pass


@router.post("/rest_password", response_model=ResponseInfo)  
def rest_password(user: User):
    pass



# 用户退出
@router.post("/logout",response_model=Message)
def logout():
    pass
