import os
from flask import request, jsonify, session
# from sqlalchemy import select
from google.oauth2 import id_token
from google.auth.transport import requests
from typing import Mapping, Any
from database import db
from flask import Blueprint
from .models import User
from .utils import check_if_is_manager, check_if_is_logged_in

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=['POST'])
def login():
    request_data: dict[str, str] = request.get_json()
    token = request_data.get('token')

    try:
        # get id info
        id_info: Mapping[str, Any] = id_token.verify_oauth2_token( # type: ignore
            token,
            requests.Request(),
            os.getenv('CLIENT_ID')
        )

        # check if the host domain is correct
        if (id_info.get('hd') != os.getenv('HD')):
            print(id_info.get('hd'))
            print(os.getenv('HD'))
            return jsonify({"error": "Invalid domain"}), 401
        
        new_user = User(
            user_id=id_info['sub'],
            user_name=id_info['name'],
            user_email=id_info['email'],
            is_manager=id_info['sub'] in os.getenv('SUPER_MANAGERS').split(',') # type: ignore
        )

        # try to add a new user
        try:
            db.session.add(new_user)
            db.session.commit()
        
        except:
            print("add user failed")
            db.session.rollback()
        
        session['user_id'] = id_info['sub']
    
        return jsonify({"message": "Login successful"}), 200
        
    except ValueError:
        return jsonify({"error": "Invalid token"}), 401

@auth_bp.route("/is_logged_in", methods=['GET'])
def is_logged_in():
    if check_if_is_logged_in():
        return jsonify({'is_logged_in': True}), 200
    
    return jsonify({'is_logged_in': False}), 200
    
@auth_bp.route("/logout", methods=['POST'])
def logout():
    session.clear()
    return jsonify({"message": "Logout successful"}), 200

@auth_bp.route("/is_manager", methods=['GET'])
def is_manager():
    # print(f"is_manager: {_is_manager()}")
    return jsonify({"is_manager": check_if_is_manager()}), 200

