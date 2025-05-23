from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.auth import crud
from src.auth.schematics import ReadUser
from src.auth.validate import validate_auth_user, create_new_user
from src.auth.jwt_help import create_jwt, get_current_token_pyload
from src.database import db_helper
from fastapi import HTTPException, status

router = APIRouter(tags=["login"])


@router.post("/sign_up")
def register(
    data=Depends(create_new_user),
    session: Session = Depends(db_helper.session_depends),
):
    user = crud.get_user(data.username, session)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="user already exist"
        )
    new_user = crud.create_user(data, session)

    return ReadUser.model_validate(new_user)


@router.post("/sign_in")
def auth_user(user: ReadUser = Depends(validate_auth_user)):
    access_token = create_jwt(user)
    return access_token


@router.get("/about_me")
def about_me(credentionals=Depends(get_current_token_pyload)):
    if not credentionals:
        return "Error"
    return credentionals
