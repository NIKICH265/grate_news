from pydantic import BaseModel
from src.auth.schematics import User


class NewsSchemas(BaseModel):
    title: str
    content: str


class CreateNews(NewsSchemas):
    pass


class ReadNewsSchemas(NewsSchemas):
    id: int
    status: str
    user: User


class UpdateNewsSchemas(NewsSchemas):
    title: str | None = None
    content: str | None = None
