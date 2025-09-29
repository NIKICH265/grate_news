from fastapi import APIRouter, Depends
from src.auth.jwt_help import is_admin

router = APIRouter(tags=["security_plus"], dependencies=[Depends(is_admin)])
