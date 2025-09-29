from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.database import Base


class User(Base):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[bytes]
    role: Mapped[str] = mapped_column(default="user")
    news: Mapped[list["News"]] = relationship(back_populates="user")
