from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from app.services.auth.routers import router as auth_router


# 加载 .env 文件
load_dotenv()


app = FastAPI()
app.include_router(auth_router, prefix="/api/v1/auth",tags=["auth"])


@app.get('/')
async def read_root():
    return  {"message": "Hello World"}