from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime, timedelta
from . import jwt as jwt_module
from . import password as pwd
from ...schemas.message import Message

router = APIRouter()


@router.get("/ping", response_model=Message)
async def ping():
    return Message(message="pong!")
