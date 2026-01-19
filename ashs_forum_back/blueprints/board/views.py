from flask import Blueprint
from database import db
from sqlalchemy import select
from flask import request, jsonify
from .models import Board

board_bp = Blueprint('board', __name__)

@board_bp.route("/boards_info", methods=['GET'])
def get_boards():
    boards = db.session.execute(select(Board)).scalars().all()

    result: list[dict[str, str | int]] = []
    for board in boards:
        result.append({
            "board_id": board.board_id,
            "board_eng": board.board_eng,
            "board_zh": board.board_zh,
            "board_n_articles": board.board_n_articles,
            "board_last_time": board.board_last_time
        })
    
    return jsonify(result)

@board_bp.route("/board_zh", methods=['GET'])
def get_board_zh():
    board_eng = request.args.get('board')
    board_zh = db.session.execute(
        select(Board.board_zh).where(Board.board_eng == board_eng)
    ).scalar()

    return jsonify({"board_zh": board_zh})