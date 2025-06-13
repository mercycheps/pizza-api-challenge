from flask import Blueprint, request, jsonify

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)


@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    return jsonify({"message": "List of restaurant_pizzas"})
