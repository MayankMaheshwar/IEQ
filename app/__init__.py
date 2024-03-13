from flask import Flask
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    app.secret_key = 'your_secret'

    from app.routes import auth_routes, product_routes, customer_routes

    app.register_blueprint(auth_routes.auth_bp)
    app.register_blueprint(product_routes.product_bp)
    app.register_blueprint(customer_routes.customer_bp)

    return app
