from database import db
from sqlalchemy import delete, select
from .models import Comment
from blueprints.article.models import Article

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
    subquery = select(Article.article_id).where(Article.article_board == board_eng)
    stmt = delete(Comment).where(Comment.article_id.in_(subquery))
    db.session.execute(stmt)

    if not commit: return
    
    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e