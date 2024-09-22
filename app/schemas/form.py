from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class RegisterForm(BaseModel):
    username: str
    password: str
    email: str
    phone: str

class GenCodeForm(BaseModel):
    username: str
    email: str
    phone: str


class ResetPasswordForm(BaseModel):
    username: str
    password: str

