from flask import jsonify
from mariadb import connect

from ...config_secrets import secrets

connection = None
cursor = None

def db_connect():
    return connect(
        user = secrets["user"],
        password = secrets["password"],
        host = secrets["host"],
        port = secrets["port"],
        database = secrets["database"]
    )

def get(command, arguments=[]):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)

        row_headers=[x[0] for x in cursor.description]

        row_values = cursor.fetchall()

        json_data=[]
        for result in row_values:
            json_data.append(dict(zip(row_headers,result)))
            
        result = json_data
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()
        return result

def put(command, arguments=[]):
    try:
        connection = db_connect()
        cursor = connection.cursor()
        cursor.execute(command, arguments)
        connection.commit()
    except Exception as err:
        print(err)
        quit()    
    else:        
        if (cursor != None):
            cursor.close()
        if (connection != None):        
            connection.close()