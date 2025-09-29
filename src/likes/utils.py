from sqlalchemy.orm import Session

from src.likes import crud


def user_reaction(news_id, user, session: Session, reaction: bool):
    reactions = crud.get_like(news_id, user["id"], session)
    if not reactions:
        crud.set_reaction(news_id, user["id"], reaction, session)
    elif reaction and not reactions.reaction:
        crud.update_reaction(reactions, reaction, session)
    elif not reaction and reactions.reaction:
        crud.update_reaction(reactions, reaction, session)
    return crud.get_reaction(news_id, session)
