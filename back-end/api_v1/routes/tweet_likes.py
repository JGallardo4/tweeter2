from flask import Blueprint, jsonify, make_response, request
from flask_api import status
from ..security.sec_utils import token_required, api_key_required
from ..db import db_tweet_likes

tweet_likes = Blueprint('/api/tweet-likes', __name__)

@tweet_likes.route("/api/tweet-likes", methods=["GET"])
@api_key_required
def get_tweet_likes():
    try:
        tweet_id = request.args["tweetId"]
        print(tweet_id)

        # Get Tweet Likes by Tweet Id
        if tweet_id:
            tweet_likes = db_tweet_likes.get_likes_by_tweet_id(tweet_id)
            print(tweet_likes)

            if tweet_likes:
                return make_response(jsonify(tweet_likes), status.HTTP_200_OK)
            else:
                return make_response(jsonify({"message": "Likes not found"}), status.HTTP_404_NOT_FOUND)
                
        # Get all Tweet Likes
        else:
            all_likes = db_tweet_likes.get_all_likes()
            print(all_likes)
            if not all_likes:
                return make_response(jsonify({"message": "No results found"}), status.HTTP_404_NOT_FOUND)
            else:
                return make_response(jsonify(all_likes), status.HTTP_200_OK)
    except Exception as e:
        print(e)
            
@tweet_likes.route("/api/tweet-likes", methods=["POST"])
@api_key_required
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

@tweet_likes.route("/api/tweet-likes", methods=["DELETE"])
@api_key_required
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