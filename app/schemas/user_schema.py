from pydantic import BaseModel

class UserRegister(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserResetPassword(BaseModel):
    email: str
    password: str
    new_password: str

class UserOut(BaseModel):
    access_token: str

class UserRegistrationSchema(BaseModel):
    username: str
    email: str
    password: str

class UserRegistrationResponse(BaseModel):
    message: str
    username: str

class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str
