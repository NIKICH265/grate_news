from sqlalchemy.orm import Session

from src.auth.models import User
from src.news.crud import get_news
from src.news.models import News
from sqlalchemy import select, desc
from src.news.enums import NewsStatus


def get_user_by_id(id: int, session: Session):
    stmt = select(User).where(User.id == id)
    user = session.scalar(stmt)
    return user


def get_all_news(session: Session):
    stmt = select(News).where(News.status == NewsStatus.pending).order_by(desc(News.id))
    news = session.scalars(stmt).all()
    return news


def news_verify(id: int, session: Session, status: NewsStatus):
    stmt = get_news(id, session)
    if stmt:
        stmt.status = status
        session.commit()
        return stmt


def delete_news(id: int, session: Session):
    stmt = get_news(id, session)
    if stmt:
        session.delete(stmt)
        session.commit()
        return f"news {stmt.title} was deleted"


def delete_user(id: int, session: Session):
    stmt = get_user_by_id(id, session)
    if stmt:
        session.delete(stmt)
        session.commit()
        return f"user {stmt.username} was deleted"
