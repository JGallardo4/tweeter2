from flask import Blueprint, jsonify, make_response, request
from flask_api import status
from ..security.sec_utils import token_required
from ..db import db_tweet_likes

tweet_likes = Blueprint('/api/tweet-likes', __name__)

@tweet_likes.route("/api/tweet-likes", methods=["GET"])
def get_tweets():
    data = request.get_json()    

    # Get Tweet Likes by Tweet Id
    if data:
        try:
            tweet_id = data["tweetId"]
        except:
            return make_response(None, status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            tweet_likes = db_tweet_likes.get_likes_by_tweet_id(tweet_id)             
            if tweet_likes:
                return make_response(jsonify(tweet_likes), status.HTTP_200_OK)
            else:
                return make_response(jsonify({"message": "Like not found"}), status.HTTP_404_NOT_FOUND)
    # Get all Tweet Likes
    else:
        result = db_tweet_likes.get_all_likes()
        if not result:
            return make_response(jsonify({"message": "No results found"}), status.HTTP_404_NOT_FOUND)
        else:
            return make_response(jsonify(result), status.HTTP_200_OK)
            
@tweet_likes.route("/api/tweet-likes", methods=["POST"])
@token_required
def create_tweet_like(user_id):   
    try:
        data = request.get_json()   
        tweet_id = data["tweetId"]
        like_exists = db_tweet_likes.like_exists(user_id, tweet_id)

        if like_exists:
            return "", status.HTTP_400_BAD_REQUEST
        else:
            db_tweet_likes.create_like(tweet_id, user_id)
            return "", status.HTTP_201_CREATED
    except Exception as e:
        return "", status.HTTP_400_BAD_REQUEST

#204
@tweet_likes.route("/api/tweet-likes", methods=["DELETE"])
@token_required
def delete_tweet_like(user_id):   
    try:
        data = request.get_json()   
        tweet_id = data["tweetId"]
        deleted = db_tweet_likes.delete_like(user_id, tweet_id)
        print(deleted)

        if deleted:
            return "", status.HTTP_204_NO_CONTENT
        else:
            return "", status.HTTP_400_BAD_REQUEST
    except Exception as e:
        return "", status.HTTP_400_BAD_REQUEST