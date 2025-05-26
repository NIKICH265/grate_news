from sqlalchemy.orm import Session
from src.news.crud import get_news
from src.news.models import News
from sqlalchemy import select, desc
from src.news.enums import NewsStatus


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
