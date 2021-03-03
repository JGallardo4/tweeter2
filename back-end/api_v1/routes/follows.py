from flask import Blueprint, jsonify, make_response, request
from flask_api import status

from ..db import db_followings, db_users
from ..security.sec_utils import token_required, api_key_required

follows = Blueprint('/api/follows', __name__)

@follows.route("/api/follows", methods=["GET"])
@api_key_required
def get_follows():
    try:
        user_id = request.args["userId"]
        follows = db_followings.get_follows(user_id)

        if follows:
            return make_response(jsonify(follows), status.HTTP_200_OK)
        else:
            return make_response(jsonify({"message": "User not found"}), status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return "", status.HTTP_400_BAD_REQUEST        

@follows.route("/api/follows", methods=["POST"])
@api_key_required
@token_required
def create_follows(user_id):
    try:
        data = request.get_json()
        followed_id = data["followId"]
    except:
        return make_response(jsonify({"message": "Invalid data"}), status.HTTP_400_BAD_REQUEST)
    else:
        db_followings.create_follow(user_id, followed_id)
        return "", status.HTTP_204_NO_CONTENT 

@follows.route("/api/follows", methods=["DELETE"])
@api_key_required
@token_required
def delete_follows(user_id):
    try:
        data = request.get_json()
        followed_id = data["followId"]
    except:
        return make_response(jsonify({"message": "Invalid data"}), status.HTTP_400_BAD_REQUEST)
    else:
        db_followings.delete_follow(user_id, followed_id)
        return "", status.HTTP_204_NO_CONTENT 
