from src.auth.crud import get_user
from fastapi import HTTPException, status, Form
import bcrypt


def validate_password(password: str, hash_password: bytes):
    return bcrypt.checkpw(password.encode(), hash_password)


def auth_user(nickname, password):
    user = get_user(nickname)
    invalid = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password"
    )
    if not user:
        raise invalid
    if not validate_password(password, user["password"]):
        raise invalid
    return user


def validate_auth_user(nickname=Form(), password=Form()):
    return auth_user(nickname, password)
