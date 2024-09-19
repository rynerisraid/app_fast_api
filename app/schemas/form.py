from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class RegisterForm(BaseModel):
    username: str
    password: str
    email: str
    phone: str
    address: str
    first_name: str
    last_name: str