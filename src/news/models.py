from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from src.settings import settings
from sqlalchemy import ForeignKey


class News(Base):
    __tablename__ = "news"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    status: Mapped[str] = mapped_column(default=settings.NEWS_STATUS["pending"])
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    user: Mapped["User"] = relationship(back_populates="news")
