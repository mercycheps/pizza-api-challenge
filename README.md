#  Pizza API Challenge

A simple Flask API for managing Restaurants, Pizzas, and their associations using SQLAlchemy and Flask-Migrate.

## Features

- List all restaurants
- Get a specific restaurant with its pizzas
- Delete a restaurant (and its related data)
- List all pizzas
- Create a new restaurant-pizza association with price validation

---

##  Technologies Used

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Migrate
- SQLite (default, easy to swap for PostgreSQL)
- RESTful API structure

---

##  Project Structure

pizza-api-challenge/
├── challenge-1-pizzas.postman_collection.json
├── instance/
│ └── app.db
├── LICENSE
├── README.md
├── server/
│ ├── app.py
│ ├── config.py
│ ├── controllers/
│ │ ├── init.py
│ │ ├── pizza_controller.py
│ │ ├── restaurant_controller.py
│ │ └── restaurant_pizza_controller.py
│ ├── models/
│ │ ├── init.py
│ │ ├── pizza.py
│ │ ├── restaurant.py
│ │ └── restaurant_pizza.py
│ └── seed.py




>  `__pycache__/` and `migrations/` directories are excluded from this structure and are  listed in `.gitignore`.



## 📦 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/mercycheps/pizza-api-challenge.git
cd pizza-api-challenge
```


Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```
Set Environment Variables

```bash
export FLASK_APP=server.app:create_app
export FLASK_ENV=development
```

Initialize the Database
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
Seed the Database (Optional)

```bash
python server/seed.py
```

Run the Server

```bash
flask run
```

API Endpoints
Restaurants
GET /restaurants
Returns a list of all restaurants

GET /restaurants/<int:id>
Returns a restaurant with its pizzas
If not found → {"error": "Restaurant not found"} (404)

DELETE /restaurants/<int:id>
Deletes a restaurant
If successful → 204 No Content
If not found → {"error": "Restaurant not found"} (404)

Pizzas
GET /pizzas
Returns a list of all pizzas

Restaurant Pizzas
POST /restaurant_pizzas
Creates a new restaurant-pizza record
Request:
```
{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}
```
Success Response:
```
{
  "id": 4,
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3,
  "pizza": {
    "id": 1,
    "name": "Emma",
    "ingredients": "Dough, Tomato Sauce, Cheese"
  },
  "restaurant": {
    "id": 3,
    "name": "Kiki's Pizza",
    "address": "address3"
  }
}
```
Error Response:
```
{
  "errors": ["Price must be between 1 and 30"]
}
```

Testing with Postman
-Open Postman

-Click Import

-Upload challenge-1-pizzas.postman_collection.json

-Use the collection to test endpoints




