from fastapi import APIRouter, Depends
from src.auth.jwt_help import get_current_token_pyload
from src.news import schemas

router = APIRouter(tags=["news"])


@router.get("/")
def news():
    print("")


@router.post("/")
def create_news(news: schemas.CreateNews, user=Depends(get_current_token_pyload)):
    new_news = {
        "title": news.title,
        "content": news.content,
        "author": user["id"],
        "status": False,
    }
    return create_news
