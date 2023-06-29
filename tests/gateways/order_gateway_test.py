from core.gateways.order_gateway import OrderGateway
import pytest

@pytest.fixture
def gateway_under_test():
    return OrderGateway()

def test_order_gateway_returns_error_when_user_id_not_provided(gateway_under_test):
    response = gateway_under_test.add_order(user_id=None, sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "errors": ["NOT_PROVIDED"]
    }
    