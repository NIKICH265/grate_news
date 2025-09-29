from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.auth.view import router as auth_router
from src.likes.view import router as like_router
from src.news.view import router as news_router
from src.database import db_helper, Base
from src.security.view import router as security_router
from fastapi.middleware.cors import CORSMiddleware


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     Base.metadata.create_all(db_helper.engine)
#     yield


app = FastAPI(
    # lifespan=lifespan
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(news_router, prefix="/news")
app.include_router(security_router, prefix="/security")
app.include_router(like_router, prefix="/likes")
