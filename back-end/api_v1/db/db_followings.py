from .db_utils import get, put
from os import path

def get_follows(user_id):
    absolute_directory = path.dirname(__file__)
    path_to_file = path.join(absolute_directory, 'get_follows.sql')
    sqlFile = open(path_to_file, 'r')
    sqlCommand = sqlFile.read()
    sqlFile.close()

    return get(sqlCommand)

def create_follow(user_id, followed_id):
    put("INSERT INTO Followings (Follower_Id, Followed_Id) VALUES (?, ?)", [user_id, followed_id])

def delete_follow(user_id, followed_id):
    put("DELETE FROM Followings WHERE Follower_Id = (?) AND Followed_Id = (?)", [user_id, followed_id])