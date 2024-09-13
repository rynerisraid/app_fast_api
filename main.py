from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from app.services.auth.routers import router as auth_router
from sqlmodel import SQLModel
from app.database import engine
from contextlib import asynccontextmanager
# 加载 .env 文件
load_dotenv()


app = FastAPI()
app.include_router(auth_router, prefix="/api/v1/auth",tags=["auth"])



@asynccontextmanager
def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    

@app.get('/')
async def read_root():
    return  {"message": "Hello World"}

