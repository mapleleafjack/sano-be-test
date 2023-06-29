from unittest import mock
import uuid
from core.gateways.order_gateway import OrderGateway
from core.models import DNAKitOrder, User
import pytest

@pytest.fixture
def gateway_under_test():
    return OrderGateway()

def test_order_gateway_returns_error_when_user_id_not_provided(gateway_under_test):
    response = gateway_under_test.add_order(user=None, sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "errors": ["NOT_PROVIDED"]
    }

@mock.patch.object(DNAKitOrder, "create")
def test_order_gateway_adds_order_to_database(create_mock, gateway_under_test):
    order_id = uuid.uuid4()
    create_mock.return_value = DNAKitOrder(id=order_id)

    response = gateway_under_test.add_order(user=User(), sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    
    assert response == {"id": order_id}