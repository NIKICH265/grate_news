from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.auth.jwt_help import get_current_token_pyload
from src.database import db_helper
from src.likes import crud
from src.likes.utils import user_reaction

router = APIRouter(tags=["likes"])


@router.post("/{news_id}/like")
def set_like(
    news_id: int,
    user: dict = Depends(get_current_token_pyload),
    session: Session = Depends(db_helper.session_depends),
):
    return user_reaction(news_id, user, session, True)


@router.delete("/{news_id}")
def delete_reaction(
    news_id: int,
    user: dict = Depends(get_current_token_pyload),
    session: Session = Depends(db_helper.session_depends),
):
    reaction = crud.get_like(news_id, user["id"], session)
    crud.reaction_delete(reaction, session)


@router.get("/{news_id}")
def get_reactions(
    news_id,
    session: Session = Depends(db_helper.session_depends),
):
    return crud.get_reaction(news_id, session)


@router.post("/{news_id}/dislike")
def set_dislike(
    news_id: int,
    user: dict = Depends(get_current_token_pyload),
    session: Session = Depends(db_helper.session_depends),
):
    return user_reaction(news_id, user, session, False)
