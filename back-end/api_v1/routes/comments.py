from flask import Blueprint, jsonify, make_response, request
from flask_api import status
from ..security.sec_utils import token_required, api_key_required
from ..db import db_comments

comments = Blueprint('/api/comments', __name__)

@comments.route("/api/comments", methods=["GET"])
@api_key_required
def get_comments_by_tweet_id():
    try:
        tweet_id = request.args["tweetId"]
        tweets_comments = db_comments.get_comments_by_tweet_id(tweet_id)
        return make_response(jsonify(user_tweets), status.HTTP_200_OK)
    except:
        return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@comments.route("/api/comments", methods=["POST"])
@api_key_required
@token_required
def create_comment(user_id):   
    try:
        data = request.get_json()
        tweet_id = data["tweetId"]
        content = data["content"]

        new_comment_id = db_comments.create_comment(user_id, tweet_id, content)

        new_comment = db_comments.get_comment_by_id(new_comment_id)        

        return make_response(jsonify(new_comment), status.HTTP_201_CREATED)
    except Exception as e:
        print(e)
        return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)

@comments.route("/api/comments", methods=["DELETE"])
@api_key_required
@token_required
def delete_comment(user_id):   
    try:
        data = request.get_json()
        comment_id = data["commentId"]
        deleted = db_comments.delete_comment(user_id, comment_id)

        if deleted != 1:
            return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return "", status.HTTP_204_NO_CONTENT
    except Exception as e:
        print(e)
        return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)

@comments.route("/api/comments", methods=["PATCH"])
@api_key_required
@token_required
def update_comment(user_id):
    try:
        data = request.get_json()
        comment_id = data["commentId"]
        content = data["content"]

        updated = db_comments.update_comment(content, user_id, comment_id)
        
        if updated != 1:
            return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            comment = db_comments.get_comment_by_id(comment_id)
            return make_response(jsonify(comment), status.HTTP_200_OK)        
    except Exception as e:
        print(e)
        return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)
        