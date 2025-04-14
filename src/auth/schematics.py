from pydantic import BaseModel


class User(BaseModel):
    nick_name: str


class CreateUser(User):
    password: str


class ReadUser(User):
    id: int
    status: str
