import re

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.jwt_help import is_admin
from src.database import db_helper
from src.news.enums import NewsStatus
from src.news.security.crud import get_all_news, news_verify

router = APIRouter(tags=["security"], dependencies=[Depends(is_admin)])


@router.get("/all_pending_news")
def pending_news(session: Session = Depends(db_helper.session_depends)):
    news = get_all_news(session)
    return news


@router.patch("/confirm_news/{idx}")
def confirm_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    news = news_verify(idx, session, NewsStatus.confirm)
    if news:
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.patch("/reject_news/{idx}")
def reject_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    news = news_verify(idx, session, NewsStatus.reject)
    if news:
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
