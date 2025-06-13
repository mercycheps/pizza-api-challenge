from flask import Blueprint, jsonify

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants')
def get_restaurants():
    return jsonify({"message": "List of restaurants"})
