from .db_utils import get, put

def get_followers(user_id):
    return get("""
        SELECT
            Id,
            Email,
            Username,
            Bio,
            Birthdate
        FROM
            (
                SELECT
                    Follower_Id
                FROM
                    Followings
                WHERE
                    Followed_Id = (?)
            ) AS Follower_Ids
	        JOIN Users ON Follower_Ids.Follower_Id = Users.Id""", [user_id])