from pydantic import BaseModel


class LoginForm(BaseModel):
    username: str
    password: str


class RegisterForm(BaseModel):
    username: str
    password: str
    email: str
    phone: str

class ResetPasswordForm(BaseModel):
    password: str
    confirm_password: str

class ChangePasswordForm(BaseModel):
    old_password: str
    new_password: str
    confirm_password: str