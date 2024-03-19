from werkzeug.security import check_password_hash
from app import mongo


def create_user(username, email, password, user_type):
    try:
        user_collection = mongo.db.users
        if user_collection.find_one({'username': username}):
            return {'status': False, 'message': 'Username already exists'}

        user_collection.insert_one({
            'username': username,
            'email': email,
            'password': password,
            'type': user_type
        })

        return {'status': True, 'message': 'User created successfully'}
    except Exception as e:
        return {'status': False, 'message': f'Error creating user: {str(e)}'}

def validate_user(username, password):
    try:
        user_collection = mongo.db.users
        user = user_collection.find_one({'username': username})
        
        if user and check_password_hash(user['password'], password):
            return {
                'username': user['username'],
                'email': user['email'],
                'type': user['type']
            }

        return None
    except Exception as e:
        return {'status': False, 'message': f'Error validating user: {str(e)}'}
