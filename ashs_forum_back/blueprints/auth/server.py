from database import db
from sqlalchemy import update
from .models import User

def ban_user(user_id: str, commit: bool=False):
    result = db.session.execute(
        update(User)
        .where(User.user_id == user_id)
        .values(is_banned=True)
    )

    if result.rowcount == 0: # type: ignore
        raise Exception("Can't find the user")

    if not commit: return

    try:
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        raise e

def unban_user(user_id: str, commit: bool=False):
    result = db.session.execute(
        update(User)
        .where(User.user_id == user_id)
        .values(is_banned=False)
    )

    if result.rowcount == 0: # type: ignore
        raise Exception("Can't find the user")

    if not commit: return

    try:
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        raise e
    