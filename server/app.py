from flask import Flask
from flask_migrate import Migrate
from server.models import db
from server.config import Config
from server.controllers import register_controllers

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    register_controllers(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)