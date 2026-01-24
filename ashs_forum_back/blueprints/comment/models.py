from database import db, Base
from sqlalchemy import Text, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Comment(db.Model, Base):
    __tablename__ = 'comments'
    comment_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, init=False)
    article_id: Mapped[int] = mapped_column(nullable=False)
    comment_content: Mapped[str] = mapped_column(Text, nullable=False)
    comment_upload_time: Mapped[datetime] = mapped_column(nullable=False)
    writer_id: Mapped[str] = mapped_column(String(80), nullable=False)
