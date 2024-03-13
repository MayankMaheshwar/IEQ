from flask import jsonify, request
from functools import wraps

def role_required(required_types):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # In a real scenario, extract the user's type from a secure source like JWT token after authentication
            user_type = request.headers.get('Type')

            if user_type not in required_types:
                return jsonify({'message': 'You do not have permission to access this resource'}), 403
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator