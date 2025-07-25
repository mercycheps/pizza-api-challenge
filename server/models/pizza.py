from server.models import db
from sqlalchemy.orm import relationship

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)
    
    restaurant_pizzas = relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Pizza {self.name}>"
