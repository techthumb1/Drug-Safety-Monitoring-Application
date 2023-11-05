# backend/routes/main_routes.py

from backend.models import drug_review
from flask import Blueprint, request, render_template
from backend.services import review_service

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        drug_name = request.form.get('drug_name')
        review_text = request.form.get('review_text')
        
        new_review = drug_review(drug_name=drug_name, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
        
        prediction = review_service.predict_severe_side_effects(review_text)
        return render_template('index.html', prediction=prediction)
    
    return render_template('index.html')


@main_routes.route('/all_reviews', methods=['GET'])
def all_reviews():
    reviews = DrugReview.query.all()
    return render_template('all_reviews.html', reviews=reviews)


# Additional configuration or initialization code

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    # Add more configuration or initialization code if needed
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()