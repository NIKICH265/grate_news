import bcrypt
from fastapi import Response
from src.auth.jwt_help import create_jwt
from src.auth.schematics import ReadUser


def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    password_bytes = password.encode()
    return bcrypt.hashpw(password_bytes, salt)


def sign_in(response: Response, user: ReadUser):
    access_token = create_jwt(user)
    response.set_cookie(
        key="access_token",
        value=access_token,
        secure=False,
        httponly=True,
        max_age=3600,
    )
    response.status_code = 200
    return response
