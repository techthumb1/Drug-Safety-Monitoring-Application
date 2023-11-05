from flask import Flask, jsonify
from models import DrugUpdate

app = Flask(__name__)

@app.route('/updates', methods=['GET'])
def get_updates():
    try:
        updates = DrugUpdate.query.all()
        return jsonify([update.serialize() for update in updates])
    except:
        return jsonify(error="Failed to fetch updates"), 500
