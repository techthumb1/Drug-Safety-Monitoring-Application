# backend/services/review_service.py

# import tensorflow as tf  # Uncomment when TensorFlow issue is resolved

from ml_models.review_processor import preprocess_review  # Import our preprocessing function
from flask import Blueprint, request, render_template, current_app

from backend.services import review_service

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        review_text = request.form.get('review_text')
        # Logic to save review and maybe predict side effects
        prediction = review_service.predict_severe_side_effects(review_text)
        return render_template('index.html', prediction=prediction)
    return render_template('index.html')

# Additional configuration or initialization code

def create_app():
    app = current_app._get_current_object()
    app.register_blueprint(main_routes)
    # Add more configuration or initialization code if needed
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()
