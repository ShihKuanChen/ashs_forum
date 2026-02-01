import os
from flask import Flask
from flask_session import Session # type: ignore
from flask_migrate import Migrate
from datetime import timedelta
import redis
from database import db
from blueprints.auth.views import auth_bp
from blueprints.article.views import article_bp
from blueprints.board.views import board_bp
from blueprints.comment.views import comment_bp
from blueprints.manage.views import manage_bp


app = Flask(__name__)

# set sql
if os.getenv('SUPER_MODE') == 'true':
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SUPER_DATABASE_URI')

else:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI') or os.getenv('DATABASE_URI')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# set session
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_USE_SIGNER'] = True # use session id to sign
app.config['SESSION_PERMANENT'] = True # set session will not be removed when close browser
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) # set session life time
app.config['SESSION_REDIS'] = redis.from_url(os.getenv('REDIS_URL')) # type: ignore

Session(app)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(article_bp, url_prefix='/api/article')
app.register_blueprint(board_bp, url_prefix='/api/board')
app.register_blueprint(comment_bp, url_prefix='/api/comment')
app.register_blueprint(manage_bp, url_prefix='/api/manage')
