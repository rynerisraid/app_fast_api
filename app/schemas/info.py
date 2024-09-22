from fastapi.responses import JSONResponse


class ResponseInfo(JSONResponse):
    status_code: int
    msg: str
    data: dict

