from database import db, Base
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column


class Article(db.Model, Base):
    __tablename__ = 'articles'
    article_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    article_board: Mapped[str] = mapped_column(String(50), nullable=False)
    article_title: Mapped[str] = mapped_column(String(50), nullable=False)
    article_content: Mapped[str] = mapped_column(Text, nullable=False)
    article_upload_time: Mapped[str] = mapped_column(String(50), nullable=False)
    writer_id: Mapped[str] = mapped_column(String(80), nullable=False)
    pinned: Mapped[bool] = mapped_column(nullable=False, default=False)