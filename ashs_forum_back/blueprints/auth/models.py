from database import db, Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model, Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(String(256), primary_key=True)
    user_name: Mapped[str] = mapped_column(nullable=False)
    user_email: Mapped[str] = mapped_column(nullable=False)
    is_manager: Mapped[bool] = mapped_column(nullable=False, default=False)
    is_banned: Mapped[bool] = mapped_column(nullable=False, default=False)
