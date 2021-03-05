from datetime import datetime, timedelta
from flask import make_response, jsonify, request
from flask_bcrypt import check_password_hash, generate_password_hash
from functools import wraps
from ..db import db_users, db_sessions
import jwt

from ...config_secrets import secrets

def generate_token(user_id):
    expiry = datetime.utcnow() + timedelta(minutes=+30)
    token = jwt.encode(
            {
                "exp": expiry,
                "user_id": user_id
            }, secrets["secret_key"], algorithm="HS256")
    return token

def generate_hash(password):
    return generate_password_hash(password)

def check_hash(password_claim, stored_hash):
    return check_password_hash(stored_hash, password_claim)

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):        
        user_id = None
        
        try:            
            data = request.get_json()
            raw_token = data["loginToken"]
            decoded_token = jwt.decode(raw_token, secrets["secret_key"], algorithms=['HS256'])
            user_id = decoded_token["user_id"]
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({"message": "Expired token"}), 401)
            db_users.log_user_out(user_id)
        except Exception as e:
            return make_response(jsonify({"message": "Invalid token"}), 401)
        else:
            if db_sessions.is_logged_in(user_id):
                return f(user_id, *args, **kws)
            else:
                return make_response(jsonify({"message": "Please log in"}), 401)
    return decorated_function

def api_key_required(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        api_key = None
        try:            
            api_key = request.headers['X-Api-Key']
            if api_key == secrets["api-key"]:                
                return f(*args, **kws)
        except Exception as e:
            print(e)
            return make_response(jsonify({"message": "Invalid api key"}), 401)
    return decorated_function
