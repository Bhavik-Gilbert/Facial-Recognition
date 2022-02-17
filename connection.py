import mysql.connector
from mysql.connector import Error

def create_connection(host_name="localhost", user_name="root", user_password="", db_name="facial_recogntion"):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query, record=""):
    cursor = connection.cursor(buffered=True)
    try:
        if(record == ""):
            cursor.execute(query)
        else:
            cursor.execute(query, record)
        connection.commit()
        print("Query executed successfully")
        return cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")

def query(query: str, record=True):
    return execute_query(create_connection(), query, record)