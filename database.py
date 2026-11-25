
import os
import mysql.connector


def get_db_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("hello789"),
        database="login_system"
    )

    return connection


