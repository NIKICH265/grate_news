from src.auth.crud import get_user
from fastapi import HTTPException, status, Form, Depends
import bcrypt
from src.auth.schematics import CreateUser
from src.auth.utils import hash_password
from sqlalchemy.orm import Session

from src.database import db_helper


def validate_password(password: str, hash_password: bytes):
    return bcrypt.checkpw(password.encode(), hash_password)


def auth_user(username: str, password, session: Session):
    user = get_user(username, session=session)
    invalid = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password"
    )
    if not user:
        raise invalid
    if not validate_password(password, user.password):
        raise invalid
    return user


def validate_auth_user(
    username=Form(),
    password=Form(),
    session: Session = Depends(db_helper.session_depends),
):
    return auth_user(username, password, session)


def create_new_user(username: str = Form(), password: str = Form()):
    hash_pass = hash_password(password)
    user = CreateUser(username=username, password=hash_pass)
    return user
