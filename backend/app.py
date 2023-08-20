# backend/app/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize the Flask application
app = Flask(__name__)

# Load configurations from environment or config file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importing routes
from .routes import main_routes

# Registering routes with the app
app.register_blueprint(main_routes)

# Models and services can be imported below or in their respective files

if __name__ == "__main__":
    app.run(debug=True)
