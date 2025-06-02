from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.jwt_help import get_current_token_pyload
from src.database import db_helper
from src.news import schemas
from src.news.crud import (
    create_news,
    get_all_news,
    get_news,
    updating_news,
    deleting_news,
)
from src.news.enums import NewsStatus

router = APIRouter(tags=["news"])


@router.get("/")
def get_newses(session: Session = Depends(db_helper.session_depends)):
    all_news = get_all_news(session)
    return all_news


@router.post("/")
def create_new_news(
    news: schemas.CreateNews,
    user=Depends(get_current_token_pyload),
    session: Session = Depends(db_helper.session_depends),
):
    new_news = create_news(news, user, session)
    return schemas.ReadNewsSchemas(
        title=new_news.title,
        id=new_news.id,
        status=new_news.status,
        content=new_news.content,
        user=user,
    )


@router.get("/{idx}")
def get_one_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    news = get_news(idx, session)
    if news.status == NewsStatus.confirm:
        return news
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="news is not found"
    )


@router.patch("/{idx}")
def update_news(
    idx: int,
    news_data: schemas.UpdateNewsSchemas,
    session: Session = Depends(db_helper.session_depends),
    user=Depends(get_current_token_pyload),
):
    print(news_data)
    news = get_news(idx, session)
    if news is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="news is not found"
        )
    if news.status == NewsStatus.confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="confirmed news is not updatable",
        )
    if news.user_id != user["id"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you can only change your own news",
        )
    new_news = updating_news(news, news_data, session)
    return new_news


@router.delete("/{idx}")
def delete_news(
    idx: int,
    session: Session = Depends(db_helper.session_depends),
    user=Depends(get_current_token_pyload),
):
    news = get_news(idx, session)
    if news is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="news is not found"
        )
    if user["id"] != news.user_id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="you can delete only your own news",
        )
    if news.status == NewsStatus.confirm:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    deleting_news(news, session)
    return "deleted"
