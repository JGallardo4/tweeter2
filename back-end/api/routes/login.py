import jwt
from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ...config_secrets import secrets
from ..db import db_sessions, db_users
from ..security.sec_utils import check_hash, generate_token, api_key_required

login = Blueprint('/api/login', __name__)

@login.route("/api/login", methods=["POST"])
@api_key_required
def login_user():
    try:
        data = request.get_json()
        email = data["email"]
        password_claim = data["password"].encode('utf8')       

        user = db_users.get_user_by_email(email)
        stored_password = db_users.get_user_password(user[0]["userId"])

        if check_hash(password_claim, stored_password):
            db_sessions.log_user_in(user[0]["userId"])
            token = generate_token(user[0]["userId"])
            user[0].update({"loginToken": token})
            return make_response(jsonify(user), 201)
        else:
            return make_response(jsonify({"message": "Incorrect username or password"}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({"message": "Incorrect data"}), 400)

@login.route("/api/login", methods=["DELETE"])
@api_key_required
def logout_user():
    user_id = None
    
    try:            
        data = request.get_json()
        raw_token = data["loginToken"]
        decoded_token = jwt.decode(raw_token, secrets["secret_key"], algorithms=['HS256'])
        user_id = decoded_token["user_id"]
    except jwt.ExpiredSignatureError:
        pass                 
    except Exception as e:
        return make_response(jsonify({"message": "Invalid token"}), 401)
        
    db_sessions.log_user_out(user_id)
    return "", status.HTTP_204_NO_CONTENT    
