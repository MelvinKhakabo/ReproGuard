from flask import Blueprint, jsonify, request
from models import db, User, Resource

api = Blueprint('api', __name__)

@api.route('/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{"id": r.id, "title": r.title, "content": r.content} for r in resources])

@api.route('/register', methods=['POST'])
def register_user():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully."}), 201

@api.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid credentials."}), 401