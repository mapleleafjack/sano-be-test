from .users import users_api
from .order import order_api


def register_blueprints(app):
    app.register_blueprint(users_api)
    app.register_blueprint(order_api)
