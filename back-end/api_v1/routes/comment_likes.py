from flask import Blueprint, jsonify, make_response, request
from flask_api import status
from ..security.sec_utils import token_required
from ..db import db_comment_likes

comment_likes = Blueprint('/api/comment-likes', __name__)

@comment_likes.route("/api/comment-likes", methods=["GET"])
def get_comment_likes():
    data = request.get_json()    

    # Get Comment Likes by Tweet Id
    if data:
        comment_id = data["commentId"]

        if not comment_id:
            return make_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR)            
        else:
            comment_likes = db_comment_likes.get_likes_by_comment_id(comment_id)             
            if comment_likes:
                return make_response(jsonify(comment_likes), status.HTTP_200_OK)
            else:
                return make_response(jsonify({"message": "Like not found"}), status.HTTP_404_NOT_FOUND)
    # Get all Comment Likes
    else:
        likes = db_comment_likes.get_all_likes()
        if not likes:
            return make_response(jsonify({"message": "No results found"}), status.HTTP_404_NOT_FOUND)
        else:
            return make_response(jsonify(likes), status.HTTP_200_OK)
            
@comment_likes.route("/api/comment-likes", methods=["POST"])
@token_required
def create_comment_like(user_id):   
    try:
        data = request.get_json()   
        comment_id = data["commentId"]
        like_exists = db_comment_likes.like_exists(user_id, comment_id)

        if like_exists:
            return "", status.HTTP_400_BAD_REQUEST
        else:
            db_comment_likes.create_like(comment_id, user_id)
            return "", status.HTTP_201_CREATED
    except Exception as e:
        return "", status.HTTP_400_BAD_REQUEST

@comment_likes.route("/api/comment-likes", methods=["DELETE"])
@token_required
def delete_comment_like(user_id):   
    try:
        data = request.get_json()   
        comment_id = data["commentId"]
        deleted = db_comment_likes.delete_like(user_id, comment_id)

        if deleted:
            return "", status.HTTP_204_NO_CONTENT
        else:
            return "", status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return "", status.HTTP_400_BAD_REQUEST