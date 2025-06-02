from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base
from src.news.enums import NewsStatus
from sqlalchemy import ForeignKey, Enum


class News(Base):
    __tablename__ = "news"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    status: Mapped[NewsStatus] = mapped_column(
        Enum(NewsStatus), default=NewsStatus.pending
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SET NULL"))
    user: Mapped["User"] = relationship(back_populates="news")
