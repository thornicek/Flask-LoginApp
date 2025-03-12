# Flask Login Website

This project is a simple Flask web application that implements user authentication with login and registration functionalities. It uses a SQLite database to store user information.

## Project Structure

```
flask-login-website
├── app
│   ├── __init__.py          # Initializes the Flask application
│   ├── auth.py              # Contains authentication routes and logic
│   ├── db.py                # Handles database interactions
│   ├── main.py              # Main entry point of the application
│   ├── templates            # Contains HTML templates
│   │   ├── base.html        # Base template for other pages
│   │   ├── index.html       # Homepage template
│   │   └── login.html       # Login page template
│   └── static               # Contains static files
│       └── style.css        # CSS styles for the application
├── venv                      # Virtual environment for dependencies
├── .flaskenv                # Environment variables for Flask
├── requirements.txt         # Lists project dependencies
└── README.md                # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd flask-login-website
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   Create a `.flaskenv` file in the root directory with the following content:
   ```
   FLASK_APP=app/main.py
   FLASK_ENV=development
   ```

6. **Run the application:**
   ```
   flask run
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Navigate to the login page to log in or register a new account.
- After logging in, you will be redirected to the homepage.

## TODO:

- Frontend: add bootstrap
- Manager/Admin user which has access to the whole database and can change the data