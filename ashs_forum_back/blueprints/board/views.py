from flask import Blueprint
from database import db
from sqlalchemy import select
from flask import request, jsonify
from .models import Board
from blueprints.utils import get_tw_zone
from typing import Any

board_bp = Blueprint('board', __name__)

@board_bp.route("/boards_info", methods=['GET'])
def get_boards():
    boards = db.session.execute(
        select(Board)
        .order_by(Board.board_id.asc())
    ).scalars().all()

    result: list[dict[str, Any]] = []
    for board in boards:
        last_time = None if board.board_last_time is None else board.board_last_time.astimezone(get_tw_zone()).strftime("%Y-%m-%d") # type: ignore
        result.append({
            "board_id": board.board_id,
            "board_eng": board.board_eng,
            "board_zh": board.board_zh,
            "board_n_articles": board.board_n_articles,
            "board_last_time": last_time
        })
    
    return jsonify(result)

@board_bp.route("/board_zh", methods=['GET'])
def get_board_zh():
    board_eng = request.args.get('board')
    board_zh = db.session.execute(
        select(Board.board_zh).where(Board.board_eng == board_eng)
    ).scalar()

    if board_zh is None:
        return jsonify({"error": "Board not found"}), 404

    return jsonify({"board_zh": board_zh})