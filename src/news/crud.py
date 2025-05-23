from sqlalchemy.orm import Session

from src.news import schemas
from src.news.models import News
from src.news.schemas import CreateNews
from src.auth.crud import get_user
from sqlalchemy import select, desc
from src.settings import settings


def create_news(data: CreateNews, user: dict, session: Session):
    user = get_user(user["username"], session)
    new_news = News(
        title=data.title,
        content=data.content,
        user=user,
        user_id=user.id,
    )
    session.add(new_news)
    session.commit()
    return new_news


def get_news(id: int, session: Session) -> News:
    stmt = select(News).where(News.id == id)
    news = session.scalar(stmt)
    return news


def get_all_news(session: Session):
    stmt = (
        select(News)
        .where(News.status == settings.NEWS_STATUS["confirm"])
        .order_by(desc(News.id))
    )
    news = session.scalars(stmt).all()
    return news


def updating_news(news: News, news_data: schemas.UpdateNewsSchemas, session: Session):
    if news_data.title is not None:
        news.title = news_data.title
    if news_data.content is not None:
        news.content = news_data.content
    session.commit()
    return news


def deleting_news(news: News, session: Session):
    session.delete(news)
    session.commit()
    return "news was deleted"
