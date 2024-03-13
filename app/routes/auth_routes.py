from flask import request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from . import auth_bp
from app.services.auth_service import create_user, validate_user

@auth_bp.route('/signup', methods=['POST'])
def signup():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        user_type = data.get('user_type')

        if not username or not email or not password or not user_type:
            return jsonify({'message': 'Missing data'}), 400

        password_hash = generate_password_hash(password)
        result = create_user(username, email, password_hash, user_type)

        if not result['status']:
            return jsonify({'message': result['message']}), 400

        return jsonify({'message': 'User created successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Missing username or password'}), 400

        user = validate_user(username, password)

        if not user:
            return jsonify({'message': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=user['username'])
        return jsonify({'message': 'Logged in successfully', 'access_token': access_token}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
