# backend/routes/main_routes.py

from flask import Blueprint, request, render_template
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
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    # Add more configuration or initialization code if needed
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()