from pydantic import BaseModel




class RegisterInfo(BaseModel):
    status_code: int
    message: str
    data: dict

class LoginInfo(BaseModel):
    status_code: int
    message: str
    data: dict

class ResponseInfo(BaseModel):
    status_code: int
    message: str
    data: dict

