# drug_safety_app/services/review_service.py
import tensorflow as tf
from ml_models.review_processor import preprocess_review  # Import our preprocessing function

model = tf.keras.models.load_model('ml_models/drug_safety_model.h5')  # Location of your saved model

def process_review(review):
    """Service function to process a raw review and get a prediction.
    
    Args:
    - review (str): Raw review text.
    
    Returns:
    - str: The prediction (safe/unsafe) for the provided review.
    """
    processed_review = preprocess_review(review)
    prediction = model.predict(processed_review)
    # Convert prediction to a human-readable result
    # Example:
    return "Safe" if prediction[0] > 0.5 else "Unsafe"
