from fastapi.security import HTTPBearer
import jwt
from fastapi import HTTPException, status, Depends
from src.auth.schematics import ReadUser
from src.settings import settings

http_bearer = HTTPBearer()


def create_jwt(user: ReadUser):
    jwt_py_load = {"id": user.id, "username": user.username, "role": user.role}
    return encode_jwt(jwt_py_load)


def encode_jwt(pyload: dict):
    encoded = jwt.encode(pyload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded


def decode_jwt(token: str | bytes):
    try:
        decode = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return decode
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token1"
        )


def get_current_token_pyload(token: HTTPBearer = Depends(http_bearer)):
    try:
        pyload = decode_jwt(token=token.credentials)
        return pyload
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token2"
        )
