from flask import request, jsonify, Blueprint
from werkzeug.security import check_password_hash
from bson import ObjectId
import json
from flask import Blueprint
from app import mongo



customer_bp = Blueprint('customer', __name__)


@customer_bp.route('/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        mongo.customers.insert_one(data)
        return jsonify({'message': 'Customer created'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<id>', methods=['GET'])
def get_customer(id):
    try:
        customer = mongo.customers.find_one({'_id': ObjectId(id)})
        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        return json.loads(json.dumps(customer, default=str)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    try:
        data = request.json
        result = mongo.customers.update_one({'_id': ObjectId(id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({'error': 'Customer not found'}), 404
        return jsonify({'message': 'Customer updated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@customer_bp.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    try:
        result = mongo.customers.delete_one({'_id': ObjectId(id)})
        if result.deleted_count == 0:
            return jsonify({'error': 'Customer not found'}), 404
        return jsonify({'message': 'Customer deleted'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
