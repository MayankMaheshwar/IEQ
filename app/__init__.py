from flask import Flask
from flask_pymongo import PyMongo
from flask_caching import Cache
from flask_jwt_extended import JWTManager



mongo = PyMongo()
cache = Cache()


def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    app.config['JWT_SECRET_KEY'] = 'your_secret_key_here'  # Change this!

    jwt = JWTManager(app)

    app.config['CACHE_TYPE'] = 'simple'
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300


    mongo.init_app(app)
    cache.init_app(app)


    from app.routes.auth_routes import auth_bp
    from app.routes.product_routes import product_bp
    from app.routes.customer_routes import customer_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(customer_bp)


    return app
