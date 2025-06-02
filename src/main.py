from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.auth.view import router as auth_router
from src.news.view import router as news_router
from src.database import db_helper, Base
from src.security.view import router as security_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(db_helper.engine)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(auth_router)
app.include_router(news_router, prefix="/news")
app.include_router(security_router, prefix="/security")
