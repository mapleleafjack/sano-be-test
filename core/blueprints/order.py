from core.gateways.email_notification_service_gateway import (
    EmailNotificationServiceGateway,
)
from core.gateways.order_gateway import OrderGateway
from core.gateways.sms_notification_service_gateway import SMSNotificationServiceGateway
from core.gateways.user_gateway import UserGateway
from core.use_cases.add_order_usecase import AddOrderUsecase
from flask import Blueprint, jsonify, request
from core.models import User
from core.schemas import UserSchema

order_api = Blueprint("order_api", __name__)


@order_api.route("/order", methods=["POST"])
def create_order():
    user_id = request.json.get("user_id", None)
    sequencing_type = request.json.get("sequencing_type", None)
    shipping_info = request.json.get("shipping_info", None)

    add_order_usecase = AddOrderUsecase(
        order_gateway=OrderGateway(),
        user_gateway=UserGateway(),
        sms_notification_service_gateway=SMSNotificationServiceGateway(),
        email_notification_service_gateway=EmailNotificationServiceGateway(),
    )

    response = add_order_usecase(
        user_id=user_id, sequencing_type=sequencing_type, shipping_info=shipping_info
    )

    return response
