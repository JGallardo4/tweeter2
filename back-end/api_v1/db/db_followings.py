from .db_utils import get, put
# from os import path

def get_follows(user_id):
    return get("""
        SELECT
            Id AS userId,
            Email AS email,
            Username AS username,
            Bio AS bio,
            Birthdate AS birthdate
        FROM
            (
                SELECT
                    Followed_Id
                FROM
                    Followings
                WHERE
                    Follower_Id = (?)
            ) AS Followed_Ids
	        JOIN Users ON Followed_Ids.Followed_Id = Users.Id""", [user_id])

def create_follow(user_id, followed_id):
    put("""
        INSERT INTO
            Followings (Follower_Id, Followed_Id)
        VALUES 
            (?, ?)""", [user_id, followed_id])

def delete_follow(user_id, followed_id):
    put("""
        DELETE FROM
            Followings 
        WHERE 
            Follower_Id = (?) 
            AND Followed_Id = (?)""", [user_id, followed_id])