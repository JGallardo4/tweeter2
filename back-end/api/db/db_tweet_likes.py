from .db_utils import get, put, put_return_id, put_return_row_count, put_return_row_count

def get_likes_by_tweet_id(tweet_id):
    likes = get("""
        SELECT
	        tweetId,
            userId,            
            username
        FROM
        (
            SELECT
                Id,
                Username as username
            FROM
                Users
        ) AS User
        JOIN (
            SELECT
                Tweet_Id AS tweetId,
                User_Id as userId
            FROM
                Tweet_Likes
            WHERE
                Tweet_Id = (?)
        ) AS Tweet_Likes ON  Tweet_Likes.userId = User.Id
        """, [tweet_id])
    return likes

def get_all_likes():
    likes = get("""
        SELECT
	        tweetId,
            userId,            
            username
        FROM
        (
            SELECT
                Id,
                Username as username
            FROM
                Users
        ) AS User
        JOIN (
            SELECT
                Tweet_Id AS tweetId,
                User_Id as userId
            FROM
                Tweet_Likes
        ) AS Tweet_Likes ON  Tweet_Likes.userId = User.Id
        """)
    return likes

def create_like(tweet_id, user_id):
    put("""
    INSERT INTO
        Tweet_Likes (Tweet_Id, User_Id)
    VALUES (?, ?)""", [tweet_id, user_id])

def like_exists(user_id, tweet_id):
    like = get("""
        SELECT
            *
        FROM
            Tweet_Likes
        WHERE
            User_Id = (?)
            AND Tweet_Id = (?)""", [user_id, tweet_id])
    
    if like:
        return True
    else:
        return False

def delete_like(user_id, tweet_id):
    deleted = put_return_row_count("""
        DELETE FROM
            Tweet_Likes
        WHERE
            User_Id = (?)
            AND Tweet_Id = (?)
    """, [user_id, tweet_id])

    if deleted == 1:
        return True
    else:
        return False