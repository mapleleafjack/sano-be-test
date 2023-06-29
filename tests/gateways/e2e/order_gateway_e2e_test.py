from core.gateways.order_gateway import OrderGateway
from core.gateways.user_gateway import UserGateway
from core.models import User
import pytest


def add_order_to_db(gateway_under_test, user_id):
    user = User(id=user_id)
    sequencing_type = "whole-exome-sequencing"
    shipping_info = {"shipping": "info"}

    gateway_under_test.add_order(user=user, sequencing_type=sequencing_type, shipping_info=shipping_info)

@pytest.fixture
def gateway_under_test():
    order_gateway = OrderGateway()

    user = UserGateway().add_user(name="test", phone_number="1234567890", email="jack.musajo@gmail.com", address={"line1": "1234 Main St"})
    order = add_order_to_db(order_gateway, user.id)

    yield order_gateway, user, order

    print("Teardown fixture after each test")


def xtest_order_gateway_returns_error_when_user_id_not_provided(gateway_under_test):
    order_gateway, user, order_id = gateway_under_test

    response = order_gateway.add_order(user=None, sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "errors": ["NOT_PROVIDED"]
    }

def xtest_order_gateway_returns_order_data(gateway_under_test):
    order_gateway, user_id, order_id = gateway_under_test

    response = order_gateway.get_order_by_user_id(user_id)

    assert response[0]["user"]["id"] == str(user_id)