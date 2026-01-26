from flask import session
from database import db
from sqlalchemy import select
from .models import User

def check_if_is_manager():
    user_id = session.get('user_id')
    if user_id is None:
        return False

    
    user = db.session.execute(select(User).where(User.user_id == user_id)).scalar()
    print(f"user: {user}")
    if user is not None:
        return user.is_manager
    
    return False

def check_if_is_logged_in():
    if session.get('user_id'):
        return True
    
    return False

def check_if_is_banned():
    # TODO: done this funcion
    ...