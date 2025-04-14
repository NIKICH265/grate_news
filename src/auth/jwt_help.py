from fastapi.security import HTTPBearer
import jwt
from fastapi import HTTPException, status, Depends
from src.auth.schematics import CreateUser
from src.settings import settings

http_bearer = HTTPBearer()


def create_jwt(user):
    jwt_py_load = {
        "id": user["id"],
        "nickname": user["nickname"],
        "status": user["status"],
    }
    return encode_jwt(jwt_py_load)


def encode_jwt(pyload: dict):
    encoded = jwt.encode(pyload, settings.SECRET_KEY, algorithm=settings.algoritm)
    return encoded


def decode_jwt(token: str | bytes):
    try:
        decode = jwt.decode(token, settings.SECRET_KEY, algorithm=[settings.algoritm])
        return decode
    except jwt.exceptions.InvalidSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token1"
        )


def get_current_token_pyload(token: HTTPBearer = Depends(http_bearer)):
    try:
        pyload = decode_jwt(token=token)
        return pyload
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token2"
        )
