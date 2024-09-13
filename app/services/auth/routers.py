from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from ...schemas.message import Message


router = APIRouter()


@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")


# 用户注册



# 用户信息

# 重置密码


# 用户登录

# 用户退出