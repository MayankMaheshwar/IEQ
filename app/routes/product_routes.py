from flask import Blueprint, request, jsonify, Flask
from bson import ObjectId
from flask import Blueprint
from app import mongo, cache

product_bp = Blueprint('product', __name__)




product_bp = Blueprint('product', __name__)

@product_bp.route('/', methods=['GET'])
def index():
    return jsonify({"Mayank":"IEQ assignment"}), 200


@product_bp.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        mongo.products.insert_one(data)
        return jsonify({'message': 'Product created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products', methods=['GET'])
@cache.cached(timeout=50, query_string=True)
def get_products():
    try:
        query_params = request.args
        search_term = query_params.get('search', '')
        sort_by = query_params.get('sort', 'name')
        order = DESCENDING if query_params.get('order', 'desc') == 'desc' else ASCENDING
        
        filter_field = query_params.get('filter_field', '')
        filter_value = query_params.get('filter_value', '')

        query = {"$text": {"$search": search_term}} if search_term else {}
        if filter_field and filter_value:
            query[filter_field] = filter_value
        
        products = mongo.products.find(query).sort(sort_by, order)
        return jsonify([product for product in products]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<id>', methods=['PUT'])
def update_product(id):
    try:
        data = request.json
        result = mongo.products.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'message': 'Product updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@product_bp.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        result = mongo.products.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify({'message': 'Product deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
