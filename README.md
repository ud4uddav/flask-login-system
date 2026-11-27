# Flask Login System

A beginner-friendly user authentication application built with **Python, Flask and MySQL**. This project demonstrates how a backend application handles user registration, password hashing, login authentication and session management.

## Features

- User registration with name, email and password.
- Password hashing using Werkzeug.
- Store user information in a MySQL database.
- Prevent duplicate email registrations.
- User login with email and password verification.
- Session-based authentication.
- Protected dashboard accessible only to logged-in users.
- Logout functionality that clears the user session.
- Environment variables for database credentials and Flask secret key.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Relational database |
| mysql-connector-python | Python–MySQL connection |
| Werkzeug | Password hashing and verification |
| HTML | Web page structure |
| CSS | Basic styling |
| python-dotenv | Environment variable management |
| Git & GitHub | Version control |

## How It Works

1. **Registration:** A user submits their name, email and password through a registration form.
2. **Password hashing:** Werkzeug generates a password hash instead of storing the original password.
3. **Database storage:** Flask connects to MySQL and saves the user's details in the `users` table.
4. **Login:** The application retrieves the user by email and verifies the submitted password against the stored hash.
5. **Session management:** After successful authentication, Flask stores the user's ID and name in a session.
6. **Dashboard:** Only authenticated users can access the dashboard.
7. **Logout:** The session is cleared when the user logs out.

## Project Structure

```text
flask-login-system/
│
├── app.py
├── database.py
├── requirements.txt
├── .env                  # Local environment variables (not committed)
├── .gitignore
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
└── static/
    └── style.css
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ud4uddav/flask-login-system.git
cd flask-login-system
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Create a database and users table:

```sql
CREATE DATABASE login_system;

USE login_system;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);
```

### 5. Configure environment variables

Create a local `.env` file in the project root:

```env
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
FLASK_SECRET_KEY=your_random_secret_key
```

Never commit your `.env` file or expose your credentials.

### 6. Start the application

```bash
python app.py
```

Open the application at:

http://127.0.0.1:5000/


## Project Scope

This is a learning project developed to strengthen my understanding of backend development and authentication fundamentals. It is not intended for production use. Additional security measures and production deployment are future improvements.
