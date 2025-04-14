from fastapi import APIRouter, Depends
from src.auth.schematics import User, ReadUser
from src.auth.validate import validate_auth_user
from src.auth.crud import create_new_user
from src.auth.jwt_help import create_jwt, get_current_token_pyload

router = APIRouter(tags=["login"])


@router.post("/sign_up")
def register(user=Depends(create_new_user)):
    return ReadUser(**user)


@router.post("/sign_in")
def auth_user(user: User = Depends(validate_auth_user)):
    access_token = create_jwt(user)
    return access_token


@router.get("/about_me")
def about_me(credentionals=Depends(get_current_token_pyload)):
    if not credentionals:
        return "Error"
    return credentionals
