from flask import Flask

from core.blueprints import register_blueprints
from core.models import create_tables


def create_app():
    app = Flask(__name__)
    register_blueprints(app)

    @app.route("/")
    def hello_world():
        return "Hello, World!"

    return app


create_tables()
