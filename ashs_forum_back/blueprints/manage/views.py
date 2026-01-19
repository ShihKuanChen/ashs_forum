from flask import Blueprint
from blueprints.auth.utils import check_if_is_manager
from blueprints.board.server import create_board, remove_board
from flask import jsonify, request



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
        create_board(board_eng, board_zh)
        return jsonify({"message": "Board created successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@manage_bp.route("/remove_board", methods=['POST'])
def remove_boardd_route():
    if not check_if_is_manager():
        return jsonify({"error": "Unauthorized"}), 401
    
    board_data = request.get_json()
    board_eng = board_data.get('board_eng')

    if board_eng is None:
        return jsonify({"error": "Invalid board data"}), 400
    

    if board_eng.strip() == "":
        return jsonify({"error": "Board name cannot be empty"}), 400
    
    try:
        remove_board(board_eng)
        return jsonify({"message": "Board removed successfully"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

