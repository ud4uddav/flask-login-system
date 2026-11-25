
from flask import Flask, render_template
from database import get_db_connection
import mysql.connector

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/test-db")
def test_db():

    connection = None
    cursor = None

    try:
        # Connect to MySQL
        connection = get_db_connection()

        # Create a cursor
        cursor = connection.cursor()

        # Execute SQL query
        cursor.execute("SELECT DATABASE()")

        # Get the result
        database_name = cursor.fetchone()

        return f"Successfully connected to: {database_name[0]}"

    except mysql.connector.Error as error:
        return f"Database connection failed: {error}", 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(debug=True)
