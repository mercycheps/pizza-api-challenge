from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models so they're registered with SQLAlchemy
from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza