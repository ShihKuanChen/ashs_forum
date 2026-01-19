from sqlalchemy import select
from .models import Board
from database import db

def update_board(board_eng: str, update_time: str):
    '''
    This function will NOT commit the changes.
    '''
    board_data = db.session.execute(
        select(Board).where(Board.board_eng == board_eng)
    ).scalar_one()

    board_data.board_n_articles += 1
    board_data.board_last_time = update_time

def create_board(board_eng: str, board_zh: str):
    new_board = Board(
        board_eng=board_eng,
        board_zh=board_zh
    )
    db.session.add(new_board)

    try:
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        raise e


def remove_board(board_eng: str):
    board_data = db.session.execute(select(Board).where(Board.board_eng == board_eng)).scalar_one()
    db.session.delete(board_data)

    try:
        db.session.commit()
    
    except Exception as e:
        db.session.rollback()
        raise e

