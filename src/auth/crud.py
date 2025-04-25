from fastapi import Form
from src.auth.utils import hash_password
from src import database
from src.database import read_user
from src.database import create_data


def create_new_user(nickname: str = Form(), password: str = Form()):
    hash_pass = hash_password(password)
    user = {"nickname": nickname, "password": hash_pass, "status": "user"}
    return create_data(user)


def get_user(nickname: str):
    db = read_user()
    for user in db:
        if nickname == user["nickname"]:
            user["password"] = user["password"].encode()
            return user
