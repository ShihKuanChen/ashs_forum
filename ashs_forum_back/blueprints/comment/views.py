from database import db
from datetime import datetime
from flask import request, jsonify, session, Blueprint
from sqlalchemy import select
from .models import Comment

comment_bp = Blueprint('comment', __name__)


@comment_bp.route("/write", methods=['POST'])
def create_comment():
    if not session.get('logged_in'):
        return jsonify({"error": "Unauthorized"}), 401
    
    current_time = datetime.now()
    
    request_data: dict[str, str] = request.get_json()

    article_id = int(request_data['article_id'])
    comment_content = request_data['comment_content']
    writer_id = session['user_id']

    if comment_content.strip() == "":
        return jsonify({"error": "Content cannot be empty"}), 400

    new_comment = Comment(
        article_id=article_id,
        comment_content=comment_content,
        writer_id=writer_id,
        comment_upload_time=current_time.strftime("%Y-%m-%d %H:%M")
    )

    db.session.add(new_comment)

    try:
        db.session.commit()

        return jsonify({"message": "Comment created successfully"}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@comment_bp.route("/comments/<int:article_id>", methods=['GET'])
def get_comments(article_id: int):
    comments = (
        db.session
        .execute(
            select(Comment)
            .where(Comment.article_id == article_id)
            .order_by(Comment.comment_id.asc())
        )
        .scalars()
        .all()
    )
    result: list[dict[str, str | int]] = []

    for comment in comments:
        result.append({
            "comment_id": comment.comment_id,
            "comment_content": comment.comment_content,
            "comment_upload_time": comment.comment_upload_time,
        })

    return jsonify(result)