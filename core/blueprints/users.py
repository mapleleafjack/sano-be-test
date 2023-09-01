from core.gateways.order_gateway import OrderGateway
from core.gateways.user_gateway import UserGateway
from core.use_cases.add_user_usecase import AddUserUsecase
from core.use_cases.get_all_users_usecase import GetAllUsersUsecase
from flask import Blueprint, jsonify, request

users_api = Blueprint("users_api", __name__)


@users_api.route("/users", methods=["GET"])
def get_all_users():
    get_all_users_usecase = GetAllUsersUsecase(
        user_gateway=UserGateway(), order_gateway=OrderGateway()
    )
    data = get_all_users_usecase()

    return jsonify({"data": data, "count": len(data)})


@users_api.route("/users", methods=["POST"])
def add_user():
    name = request.json.get("name", None)
    phone_number = request.json.get("phone_number", None)
    email = request.json.get("email", None)
    address = request.json.get("address", None)

    response = AddUserUsecase(add_user_gateway=UserGateway()).add_user(
        name=name, phone_number=phone_number, email=email, address=address
    )

    if isinstance(response, dict) and "errors" in response:
        return jsonify(response)

    return jsonify(response.id)
