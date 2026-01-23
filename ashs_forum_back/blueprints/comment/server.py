from database import db
from sqlalchemy import delete
from .models import Comment

def remove_comments_by_article_id(article_id: int, commit: bool=False):
    db.session.execute(
        delete(Comment)
        .where(Comment.article_id == article_id)
    )

    if not commit: return
    
    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e

def remove_comments_by_board(board_eng: str, commit: bool=False):
    ...