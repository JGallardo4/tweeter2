from .db_utils import get, put, put_return_id, put_return_row_count
from datetime import datetime

def get_comments_by_tweet_id(tweet_id):
    comments = get("""
        SELECT
            TweetComments.Id AS commentId,
	        Tweet_Id AS tweetId,
            User_Id AS userId,
            Username AS username,            
            Content AS content,
            Created_At AS createdAt            
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
                Comments
            WHERE
                Tweet_Id = (?)
        ) AS TweetComments ON TweetComments.User_Id = Users.Id
        """, [tweet_id])
    return tweets

def get_comment_by_id(comment_id) :
    comment = get("""
        SELECT
	        Comment.Id AS commentId,
            Tweet_Id AS tweetId,
            User_Id AS userId,
            Username AS username,
            Content AS content,
            Created_At AS createdAt            
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
                Comments
            WHERE
                Id = (?)
        ) AS Comment ON Comment.User_Id = User.Id
        """, [comment_id])
    return comment

def create_comment(user_id, tweet_id, content):
    created_at = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    comment_id = put_return_id("""
        INSERT INTO
	        Comments (User_Id, Tweet_Id, Content, Created_At)
        VALUES
	        (?, ?, ?, ?)""", [user_id, tweet_id, content, created_at])

    return comment_id


def delete_comment(user_id, comment_id):
    deleted = put_return_row_count("""
        DELETE FROM
	        Comments
        WHERE
            User_Id = (?)
            AND Id = (?)""", [user_id, comment_id])

    return deleted

def update_comment(content, user_id, comment_id):
    updated = put_return_row_count("""
        UPDATE 
            Comments
        SET
            Content = (?)
        WHERE 
            User_Id = (?) AND Id = (?)""", [content, user_id, comment_id])
    
    return updated
