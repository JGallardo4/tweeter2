from flask import Blueprint, jsonify, make_response, request
from flask_api import status
from ..security.sec_utils import token_required
from ..db import db_comments

comments = Blueprint('/api/comments', __name__)

@comments.route("/api/comments", methods=["GET"])
def get_comments_by_tweet_id():
    data = request.get_json()

    # Get Comments by Tweet Id
    if data:
        try:
            tweet_id = data["tweetId"]
        except:
            return "", status.HTTP_500_INTERNAL_SERVER_ERROR
        else:
            tweets_comments = db_comments.get_comments_by_tweet_id(tweet_id)             
            if tweets_comments:
                return make_response(jsonify(user_tweets), status.HTTP_200_OK)
            else:
                return make_response(jsonify({"message": "User not found"}), status.HTTP_404_NOT_FOUND)    
    else:
        return "", status.HTTP_500_INTERNAL_SERVER_ERROR

@comments.route("/api/comments", methods=["POST"])
@token_required
def create_comment(user_id):   
    try:
        data = request.get_json()
        tweet_id = data["tweetId"]
        content = data["content"]

        new_comment_id = db_comments.create_comment(user_id, tweet_id, content)

        new_comment = db_comments.get_comment_by_id(new_comment_id)        

        return make_response(jsonify(new_comment), status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)

# @tweets.route("/api/tweets", methods=["DELETE"])
# @token_required
# def delete_tweet(user_id):   
#     try:
#         data = request.get_json()
#         tweet_id = data["tweetId"]
#         deleted = db_tweets.delete_tweet(user_id, tweet_id)

#         print(deleted)

#         if deleted != 1:
#             return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return "", status.HTTP_204_NO_CONTENT
#     except Exception as e:
#         print(e)
#         return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)

# @tweets.route("/api/tweets", methods=["PATCH"])
# @token_required
# def update_tweet(user_id):
#     try:
#         data = request.get_json()
#         tweet_id = data["tweetId"]
#         content = data["content"]

#         db_tweets.update_tweet(user_id, tweet_id, content)
#     except Exception as e:
#         print(e)
#         return make_response("", status.HTTP_500_INTERNAL_SERVER_ERROR)
#     else:
#         tweet = db_tweets.get_brief_tweet_by_id(tweet_id)
#         return make_response(jsonify(tweet), status.HTTP_200_OK)