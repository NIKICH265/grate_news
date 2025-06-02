from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.auth.jwt_help import is_admin
from src.database import db_helper
from src.news.enums import NewsStatus
from src.security import crud

router = APIRouter(tags=["security"], dependencies=[Depends(is_admin)])


@router.get("/all_pending_news")
def pending_news(session: Session = Depends(db_helper.session_depends)):
    news = crud.get_all_news(session)
    return news


@router.patch("/confirm_news/{idx}")
def confirm_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    news = crud.news_verify(idx, session, NewsStatus.confirm)
    if news:
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.patch("/reject_news/{idx}")
def reject_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    if news := crud.news_verify(idx, session, NewsStatus.reject):
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/delete_news/{idx}")
def delete_news(idx: int, session: Session = Depends(db_helper.session_depends)):
    if news := crud.delete_news(idx, session):
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/delete_user/{idx}")
def delete_user(idx: int, session: Session = Depends(db_helper.session_depends)):
    if news := crud.delete_user(idx, session):
        return news
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
