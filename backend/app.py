from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Import the 'db' object from a module called 'extensions'
# It's assumed that 'extensions.py' exists and it contains an initialized 'SQLAlchemy' instance
from extensions import db

# This import statement assumes you have a DevelopmentConfig class defined in a config.py file
from config import DevelopmentConfig

# Function to create the Flask application
def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    
    # Load configurations from the provided class
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    Migrate(app, db)
    
    # Register blueprints
    from .routes.main_routes import main_routes
    app.register_blueprint(main_routes)

    # Import models here if needed, after initializing the app context
    # from .models import YourModel

    # Define any routes here or in their respective blueprint modules
    @app.route('/process-data', methods=['POST'])
    def process_data():
        try:
            # Assuming process_openfda_data() is a function defined in the services module
            from .services.review_service import process_openfda_data
            process_openfda_data()
            return jsonify({"status": "success", "message": "Data processing initiated."}), 200
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
    
    return app

# Check if the run.py file is executing the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
