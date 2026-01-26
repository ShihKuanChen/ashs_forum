from flask import Blueprint
from blueprints.auth.utils import check_if_is_manager
from blueprints.board.server import create_board, remove_board, update_board
from blueprints.article.server import remove_article_by_id, get_article_board_eng_by_id, remove_article_by_board
from blueprints.comment.server import remove_comments_by_article_id, remove_comments_by_board
from flask import jsonify, request
from database import db


manage_bp = Blueprint('manage', __name__)

@manage_bp.route("/create_board", methods=['POST'])
def create_board_route():
    if not check_if_is_manager():
        return jsonify({"error": "Unauthorized"}), 401
    
    board_data = request.get_json()
    board_eng = board_data.get('board_eng')
    board_zh = board_data.get('board_zh')

    if board_eng is None or board_zh is None:
        return jsonify({"error": "Invalid board data"}), 400
    

    if board_eng.strip() == "" or board_zh.strip() == "":
        return jsonify({"error": "Board name cannot be empty"}), 400

    try:
        create_board(board_eng, board_zh, commit=True)
        return jsonify({"message": "Board created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@manage_bp.route("/remove_board", methods=['POST'])
def remove_board_route():
    if not check_if_is_manager():
        return jsonify({"error": "Unauthorized"}), 401
    
    board_data = request.get_json()
    board_eng = board_data.get('board_eng')

    if board_eng is None:
        return jsonify({"error": "Invalid board data"}), 400
    

    if board_eng.strip() == "":
        return jsonify({"error": "Board name cannot be empty"}), 400
    
    try:
        remove_comments_by_board(board_eng, commit=False)
        remove_article_by_board(board_eng, commit=False)
        remove_board(board_eng, commit=False)
        db.session.commit()
        return jsonify({"message": "Board removed successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@manage_bp.route("/remove_article_and_comments", methods=['POST'])
def remove_article_and_comments():
    if not check_if_is_manager():
        return jsonify({"error": "Unauthorized"}), 401
    
    article_id = request.get_json().get('article_id')
    board_eng = get_article_board_eng_by_id(article_id)

    if article_id is None:
        return jsonify({"error": "Invalid article id"}), 400
    
    try:
        remove_article_by_id(int(article_id))
        remove_comments_by_article_id(int(article_id))
        update_board(board_eng)
        db.session.commit()
        return jsonify({"message": "Article and comments removed successfully"}), 200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500