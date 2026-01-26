from flask import session
from database import db
from sqlalchemy import select
from .models import User

def check_if_is_manager():
    user_id = session.get('user_id')
    if user_id is None:
        raise Exception("Didn't login")

    
    user = db.session.execute(select(User).where(User.user_id == user_id)).scalar()
    # print(f"user: {user}")
    if user is not None:
        return user.is_manager
    
    raise Exception("Can't find the user")

def check_if_is_logged_in():
    if session.get('user_id'):
        return True
    
    return False

def check_if_is_banned():
    user_id = session.get('user_id')
    if user_id is None:
        raise Exception("Didn't login")
        # return True
    
    is_banned = db.session.execute(select(User.is_banned).where(User.user_id == user_id)).scalar()
    if is_banned is not None:
        return is_banned
    
    raise Exception("Can't find the user")