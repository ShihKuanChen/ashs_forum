from flask import Blueprint, request, jsonify, session
from sqlalchemy import select
from database import db
from .models import Article
from datetime import datetime, timezone
from blueprints.auth.utils import check_if_is_manager, check_if_is_logged_in
from blueprints.board.server import update_board
from blueprints.utils import get_tw_zone

article_bp = Blueprint('article', __name__)

@article_bp.route("/articles_info", methods=['GET'])
def get_articles_info():
    limit = request.args.get('limit', default=30, type=int)
    last_id = request.args.get('last_id', default=-1, type=int)
    board = request.args.get('board')

    result: list[dict[str, str | int]] = []

    if last_id == -1:
        pinned_stmt = (
            select(Article)
            .where(Article.pinned == True)
            .where(Article.article_board == board)
            .order_by(Article.article_id.desc())
        )

        pinned_articles = db.session.execute(pinned_stmt).scalars().all()

        for article in pinned_articles:
            upload_time = article.article_upload_time.astimezone(get_tw_zone()).strftime("%Y-%m-%d %H:%M")
            result.append({
                "article_title": article.article_title,
                "article_upload_time": upload_time,
                "article_id": article.article_id,
                "writer_id": article.writer_id
            })

    stmt = select(Article)

    if last_id != -1:
        stmt = stmt.where(Article.article_id < last_id)

    stmt = (
        stmt
        .where(Article.article_board == board)
        .where(Article.pinned == False)
        .order_by(Article.article_id.desc())
        .limit(limit)
    )

    articles = db.session.execute(stmt).scalars().all()
    
    for article in articles:
        upload_time = article.article_upload_time.astimezone(get_tw_zone()).strftime("%Y-%m-%d %H:%M")
        result.append({
            "article_title": article.article_title,
            "article_upload_time": upload_time,
            "article_id": article.article_id,
            "writer_id": article.writer_id
        })
    
    return jsonify(result)

@article_bp.route("/<int:article_id>", methods=['GET'])
def get_article(article_id: int):
    article = db.session.get(Article, article_id)
    
    if article is None:
        return jsonify({"error": "Can't find the article."}), 404
    
    upload_time = article.article_upload_time.astimezone(get_tw_zone()).strftime("%Y-%m-%d %H:%M")
    
    return jsonify({
        "article_id": article.article_id,
        "article_title": article.article_title,
        "article_content": article.article_content,
        "article_upload_time": upload_time
    })

@article_bp.route("/write", methods=['POST'])
def create_article():
    if not check_if_is_logged_in():
        return jsonify({"error": "Unauthorized"}), 401
    
    current_time = datetime.now(timezone.utc)
    
    request_data = request.get_json()

    article_board = request_data['article_board']
    article_content = request_data['article_content']
    article_title = request_data['article_title']
    writer_id = session['user_id']
    pinned = request_data['pinned'] and check_if_is_manager()

    print(f"is_pinned: {pinned} is_manager: {check_if_is_manager()}")

    if article_title.strip() == "" or article_content.strip() == "":
        return jsonify({"error": "Title and content cannot be empty"}), 400

    new_article = Article(
        article_board=article_board,
        article_content=article_content,
        article_title=article_title,
        article_upload_time=current_time,
        writer_id=writer_id,
        pinned=pinned
    )

    db.session.add(new_article)
    update_board(article_board, commit=True)
    print("update board")

    return jsonify({"message": "Article created successfully"}), 201

    # board_data = db.session.execute(
    #     select(Board).where(Board.board_eng == article_board)
    # ).scalar_one()

    # board_data.board_n_articles += 1
    # board_data.board_last_time = current_time.strftime("%Y-%m-%d")
    