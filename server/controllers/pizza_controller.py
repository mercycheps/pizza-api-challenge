from flask import Blueprint, jsonify
from server.models import Pizza

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'ingredients': p.ingredients
        } for p in pizzas
    ])
