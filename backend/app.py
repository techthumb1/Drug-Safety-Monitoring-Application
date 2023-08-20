# drug_safety_drug_safety_monitoring_application/app.py
from flask import Flask, render_template, request, jsonify
from services.review_service import process_review  # Import our service layer function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        review = request.form.get('review')
        prediction = process_review(review)  # Use the service layer function
        return jsonify(prediction=prediction)
    return render_template('index.html')
# backend/app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')  # Assuming 'config.py' contains Flask & DB configurations

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register routes here
# from backend.routes import main_routes
# app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)
