from fastapi import FastAPI
from src.auth.view import router as auth_router
from src.news.view import router as news_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(news_router, prefix="/news")
