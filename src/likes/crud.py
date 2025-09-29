from sqlalchemy import select, func
from sqlalchemy.orm import Session
from src.likes.models import Reaction


def get_like(news_id, user_id, session: Session):
    reactions = (
        select(Reaction)
        .where(Reaction.news_id == news_id)
        .where(Reaction.user_id == user_id)
    )
    return session.scalar(reactions)


def update_reaction(user_reaction: Reaction, like: bool, session: Session):
    user_reaction.reaction = like
    session.commit()


def set_reaction(news_id, user_id, reaction: bool, session: Session):
    stmt = Reaction(news_id=news_id, user_id=user_id, reaction=reaction)
    session.add(stmt)
    session.commit()
    return stmt


def reaction_delete(user_reaction: Reaction, session: Session):
    if user_reaction:
        session.delete(user_reaction)
        session.commit()


def get_reaction(news_id, session: Session):
    stmt = (
        select(
            Reaction.reaction,
            func.count().label("count"),
        )
        .where(Reaction.news_id == news_id)
        .group_by(Reaction.reaction)
    )
    result = session.execute(stmt).all()
    counts = {like: count for like, count in result}
    return {"likes": counts.get(True, 0), "dislike": counts.get(False, 0)}
