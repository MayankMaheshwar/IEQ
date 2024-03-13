from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
product_bp = Blueprint('product', __name__)
customer_bp = Blueprint('customer', __name__)

from . import auth_routes, product_routes, customer_routes
