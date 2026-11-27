import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        database="login_system"
    )

    return connection