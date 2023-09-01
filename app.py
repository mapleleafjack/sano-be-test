from flask import Flask, render_template

from core.blueprints import register_blueprints
from core.models import create_tables


def create_app():
    app = Flask(__name__, static_url_path="/static", static_folder="static")
    register_blueprints(app)

    @app.route("/")
    def hello_world():
        return render_template("index.html")

    return app


create_tables()
