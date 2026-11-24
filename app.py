
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to my website!"


@app.route("/login")
def login():
    return "This is the login page."


@app.route("/register")
def register():
    return "This is the registration page."

@app.route("/about")
def about():
    return "This is my first Flask project. I am learning Python backend development."


if __name__ == "__main__":
    app.run(debug=True)


