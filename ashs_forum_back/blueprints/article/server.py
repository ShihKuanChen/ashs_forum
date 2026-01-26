from database import db
from sqlalchemy import select, delete
from .models import Article

def remove_article_by_id(article_id: int, commit: bool=False):
    db.session.execute(
        delete(Article)
        .where(Article.article_id == article_id)
    )

    if not commit: return
    
    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e

def remove_article_by_board(board_eng: str, commit: bool=False):
    db.session.execute(
        delete(Article)
        .where(Article.article_board == board_eng)
    )
    
    if not commit: return
    
    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e


def get_article_board_eng_by_id(article_id: int):
    article = db.session.execute(
        select(Article)
        .where(Article.article_id == article_id)
    ).scalar()

    if article is None:
        raise Exception("Article not found")
    
    return article.article_board
