from .db_utils import get, put, put_return_id, put_return_row_count, put_return_row_count

def get_likes_by_comment_id(comment_id):
    comments = get("""
        SELECT
	        commentId,
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
                Comment_Id AS commentId,
                User_Id as userId
            FROM
                Comment_Likes
            WHERE
                Comment_Id = (?)
        ) AS Comment_Likes ON  Comment_Likes.userId = User.Id
        """, [comment_id])
    return comments

def get_all_likes():
    likes = get("""
        SELECT
	        commentId,
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
                Comment_Id AS commentId,
                User_Id as userId
            FROM
                Comment_Likes
        ) AS Comment_Likes ON  Comment_Likes.userId = User.Id
        """)
    return likes

def create_like(comment_id, user_id):
    put("""
    INSERT INTO
        Comment_Likes (Comment_Id, User_Id)
    VALUES (?, ?)""", [comment_id, user_id])

def like_exists(user_id, comment_id):
    like = get("""
        SELECT
            *
        FROM
            Comment_Likes
        WHERE
            User_Id = (?)
            AND Comment_Id = (?)""", [user_id, comment_id])
    
    if like:
        return True
    else:
        return False

def delete_like(user_id, comment_id):
    deleted = put_return_row_count("""
        DELETE FROM
            Comment_Likes
        WHERE
            User_Id = (?)
            AND Comment_Id = (?)""", [user_id, comment_id])

    if deleted == 1:
        return True
    else:
        return False