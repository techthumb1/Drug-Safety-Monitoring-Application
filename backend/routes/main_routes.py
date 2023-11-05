from flask import Blueprint, render_template
from models.drug_review import DrugReview

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    reviews = DrugReview.query.all()
    return render_template('index.html', reviews=reviews)
