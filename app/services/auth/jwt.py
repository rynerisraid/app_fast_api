from datetime import datetime, timedelta
from ...config import Settings
from . import password
import jwt


SECRET_KEY = Settings().SECRET_KEY
ALGORITHM = Settings().JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = Settings().JWT_ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
