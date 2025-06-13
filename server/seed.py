
from server.app import create_app
from server.models import db, Restaurant, Pizza, RestaurantPizza


app = create_app()
with app.app_context():
    db.drop_all()
    db.create_all()
    # create resturants
    r1 = Restaurant(name="Domino's", address="123 Main St")
    r2 = Restaurant(name="Papa John's", address="456 Side St")
    
    #create Pizzas
    p1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    
    # add to sessions
    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()
    
    #resturants_pizza r/ship
    rp = RestaurantPizza(price=15, pizza_id=p1.id, restaurant_id=r1.id)
    db.session.add(rp)
    db.session.commit()
