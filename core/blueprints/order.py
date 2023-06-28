from flask import Blueprint, jsonify
from core.models import User
from core.schemas import UserSchema

order_api = Blueprint("order_api", __name__)


@order_api.route("/order", methods=["POST"])
def create_order():
    return "Order sent successfully"