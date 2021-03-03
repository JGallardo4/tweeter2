from .db_utils import get, put

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
