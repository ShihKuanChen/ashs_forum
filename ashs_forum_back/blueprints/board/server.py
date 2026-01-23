from sqlalchemy import select, delete, func
from .models import Board
from blueprints.article.models import Article
from database import db
# from datetime import datetime

def update_board(board_eng: str, commit: bool=False):
    board_data = db.session.execute(
        select(Board).where(Board.board_eng == board_eng)
    ).scalar_one()

    count_stmt = select(func.count()).select_from(Article).where(Article.article_board == board_eng)
    count = db.session.execute(count_stmt).scalar()

    lastest_article = db.session.execute(
        select(Article)
        .where(Article.article_board == board_eng)
        .order_by(Article.article_id.desc())
        .limit(1)
    ).scalar()

    # print(f"{board_eng} count: {count}")
    # print(f"{board_eng} lastest: {lastest_article.article_upload_time}") # type: ignore


    if count is None:
        raise Exception("Board not found")

    board_data.board_n_articles = count
    board_data.board_last_time = None if lastest_article is None else lastest_article.article_upload_time # type: ignore
    
    # get lastest article timestamp
    # board_data.board_last_time = datetime.fromtimestamp(update_time).strftime("%Y-%m-%d") 

    if not commit: return

    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e

def create_board(board_eng: str, board_zh: str, commit: bool=False):
    new_board = Board(
        board_eng=board_eng,
        board_zh=board_zh
    )
    db.session.add(new_board)

    if not commit: return

    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e


def remove_board(board_eng: str, commit: bool=False):
    db.session.execute(
        delete(Board)
        .where(Board.board_eng == board_eng)
    )

    if not commit: return

    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e