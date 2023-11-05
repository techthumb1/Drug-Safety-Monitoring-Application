# backend/models/drug_review.py

#from app import db
from extensions import db

class DrugReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drug_name = db.Column(db.String(128), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    adverse_event = db.Column(db.String(256))
    reported_at = db.Column(db.DateTime, default=db.func.current_timestamp())
