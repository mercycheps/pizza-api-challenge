from flask import Blueprint

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas')
def get_pizzas():
    return "List of pizzas"
