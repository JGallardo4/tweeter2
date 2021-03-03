from .db_utils import get, put, put_return_id, put_return_row_count
from datetime import datetime

def get_tweets_by_user_id(user_id):
    tweets = get("""
        SELECT
	        UserTweets.Id AS tweetId,
            User.Id AS userId,
            Content AS content,
            Created_At AS createdAt,
            Username AS username
        FROM
        (
            SELECT
                Id,
                Username
            FROM
                Users
        ) AS User
        JOIN (
            SELECT
                *
            FROM
                Tweets
            WHERE
                User_Id = (?)
        ) AS UserTweets ON UserTweets.User_Id = User.Id
        """, [user_id])
    return tweets

def get_tweet_by_id(tweet_id):
    tweet = get("""
        SELECT
	        UserTweets.Id AS tweetId,
            User.Id AS userId,
            Content AS content,
            Created_At AS createdAt,
            Username AS username
        FROM
        (
            SELECT
                Id,
                Username
            FROM
                Users
        ) AS User
        JOIN (
            SELECT
                *
            FROM
                Tweets
            WHERE
                Id = (?)
        ) AS UserTweets ON UserTweets.User_Id = User.Id
        """, [tweet_id])
    return tweet

def get_all_tweets():
    tweets = get("""
        SELECT
	        UserTweets.Id AS tweetId,
            User.Id AS userId,
            Content AS content,
            Created_At AS createdAt,
            Username AS username
        FROM
        (
            SELECT
                Id,
                Username
            FROM
                Users
        ) AS User
        JOIN (
            SELECT
                *
            FROM
                Tweets
        ) AS UserTweets ON UserTweets.User_Id = User.Id
        """)
    return tweets

def create_tweet(user_id, content):
    created_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    tweet_id = put_return_id("""
        INSERT INTO
	        Tweets (User_Id, Content, Created_At)
        VALUES
	        (?, ?, ?)""", [user_id, content, created_at])

    return tweet_id

def delete_tweet(user_id, tweet_id):
    deleted = put_return_row_count("""
        DELETE FROM
	        Tweets
        WHERE
            Id = (?)
            AND User_Id = (?)""", [tweet_id, user_id])

    return deleted
