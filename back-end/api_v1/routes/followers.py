from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..db import db_followers, db_users

followers = Blueprint('/api/followers', __name__)

@followers.route("/api/followers", methods=["GET"])
def get_followers():
    try:
        data = request.get_json()
        user_id = data["userId"]

        if db_users.get_user_by_id(user_id):
            return make_response(jsonify(db_followers.get_followers(user_id)), status.HTTP_200_OK)
        else:
            return make_response(jsonify({"message": "User not found"}), status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return "", status.HTTP_400_BAD_REQUEST  
