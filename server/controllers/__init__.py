from .pizza_controller import pizza_bp
from .restaurant_controller import restaurant_bp
from .restaurant_pizza_controller import restaurant_pizza_bp

def register_controllers(app):
    app.register_blueprint(pizza_bp, url_prefix='/pizzas')
    app.register_blueprint(restaurant_bp, url_prefix='/restaurants')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/restaurant_pizzas')
