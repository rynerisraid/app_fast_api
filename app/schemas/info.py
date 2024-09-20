from pydantic import BaseModel


class ResponseInfo(BaseModel):
    status_code: int
    message: str
    data: dict

