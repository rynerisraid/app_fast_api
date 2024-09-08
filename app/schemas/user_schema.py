from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    password:str
    email:str
    full_name:str
    is_superuser:bool = False
    disabled:bool = False

class UserLogin(BaseModel):
    username:str
    password:str

class UserOut(BaseModel):
    username:str
    email:str
    full_name:str
    is_superuser:bool
    disabled:bool

class UserUpdate(BaseModel):
    username:str
    email:str
    full_name:str
    is_superuser:bool
    disabled:bool