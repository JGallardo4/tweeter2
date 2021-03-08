from .db_utils import get, put

def log_user_in(user_id):
    put("""
        REPLACE INTO 
            User_Sessions (User_Id) 
        VALUES 
            (?)""", [user_id])

def log_user_out(user_id):
    put("""
        DELETE FROM 
            User_Sessions 
        WHERE 
            User_Id = (?)""", [user_id])
    
def is_logged_in(user_id):
    if get("""
        SELECT 
            * 
        FROM 
            User_Sessions 
        WHERE 
            User_Id = (?)""", [user_id]):
        return True
    else:
        return False