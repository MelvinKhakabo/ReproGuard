from flask import jsonify, request
from backend.app import app

@app.route('/api/resources', methods=['GET'])
def get_resources():
    return jsonify({"message": "List of resources"})