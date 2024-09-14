from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from app.user.routers import router as user_router
from sqlmodel import SQLModel
from app.database import engine
from contextlib import asynccontextmanager

import sys
sys.path.append('.')

# 加载 .env 文件
load_dotenv()


app = FastAPI()
app.include_router(user_router, prefix="/api/v1/user",tags=["user"])



@asynccontextmanager
def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    

@app.get('/')
async def read_root():
    return  {"message": "Hello World"}

