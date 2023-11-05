# backend/app/app.py

###from flask import Flask
###from flask_sqlalchemy import SQLAlchemy
###from flask_migrate import Migrate
###
#### Initialize the Flask application
###app = Flask(__name__)
###
#### Load configurations from environment or config file
#### app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
#### app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
###
###app = Flask(__name__)
###app.config.from_object(DevelopmentConfig)
###
#### Initialize SQLAlchemy and Flask-Migrate
###db = SQLAlchemy(app)
###migrate = Migrate(app, db)
###
#### Importing routes
###from .routes import main_routes
###
#### Registering routes with the app
###app.register_blueprint(main_routes)
###
#### Models and services can be imported below or in their respective files
###
###if __name__ == "__main__":
###    app.run(debug=True)
###

from flask import Flask
from extensions import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    # Initialize extensions
    db.init_app(app)

    # Register blueprints here
    from routes.main_routes import main
    app.register_blueprint(main)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
