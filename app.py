
from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash, os
from mysql.connector import IntegrityError, Error
from database import get_db_connection

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email or not password:
            return "Email and password are required."

        connection = None
        cursor = None

        try:
            connection = get_db_connection()
            cursor = connection.cursor(dictionary=True)

            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))

            user = cursor.fetchone()

            if user and check_password_hash(user["password"], password):

                session["user_id"] = user["id"]
                session["user_name"] = user["name"]

                return redirect(url_for("dashboard"))

            return "Invalid email or password."

        except Error as error:
            print("Database error:", error)
            return "Something went wrong."

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        # Get data from the registration form
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        # Basic validation
        if not name or not email or not password:
            return "All fields are required."

        # Hash the password
        hashed_password = generate_password_hash(password)

        connection = None
        cursor = None

        try:
            # Connect to MySQL
            connection = get_db_connection()
            cursor = connection.cursor()

            # Insert user into database
            sql = """
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """

            values = (name, email, hashed_password)

            cursor.execute(sql, values)

            # Save changes
            connection.commit()

            return "Registration successful! Your account has been created."

        except IntegrityError:
            return "This email is already registered."

        except Error as error:
            print("Database error:", error)
            return "Something went wrong while saving your account."

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()

    return render_template("register.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html")


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))




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

    except Error as error:
        return f"Database connection failed: {error}", 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()                                  



if __name__ == "__main__":
    app.run(debug=True)



