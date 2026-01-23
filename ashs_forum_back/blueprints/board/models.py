from database import db, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class Board(db.Model, Base):
    __tablename__ = 'boards'
    board_id: Mapped[int] = mapped_column(unique=True, primary_key=True, autoincrement=True, init=False)
    board_eng: Mapped[str] = mapped_column(String(50), unique=True, primary_key=True, nullable=False)
    board_zh: Mapped[str] = mapped_column(String(50), nullable=False)
    board_n_articles: Mapped[int] = mapped_column(nullable=False, default=0)
    board_last_time: Mapped[datetime] = mapped_column(nullable=True, default=None)