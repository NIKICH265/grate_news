from src.auth.models import User
from src.auth.schematics import CreateUser
from sqlalchemy.orm import Session
from sqlalchemy import select


def create_user(user: CreateUser, session: Session):
    user_dict = user.model_dump()
    new_user = User(**user_dict)
    session.add(new_user)
    session.commit()
    return new_user


def get_user(username: str, session: Session):
    stmt = select(User).where(User.username == username)
    user = session.scalar(stmt)  # scalars
    return user
