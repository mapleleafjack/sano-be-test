from unittest import mock
import uuid
from core.gateways.order_gateway import OrderGateway
from core.models import DNAKitOrder, User
import pytest


@pytest.fixture
def gateway_under_test():
    return OrderGateway()


def test_order_gateway_returns_error_when_user_id_not_provided(gateway_under_test):
    response = gateway_under_test.add_order(
        user=None,
        sequencing_type="whole-exome-sequencing",
        shipping_info={"shipping": "info"},
    )
    assert response == {"errors": ["NOT_PROVIDED"]}


@mock.patch.object(DNAKitOrder, "create")
def test_order_gateway_calls_create_on_dna_kit_order(mock_create, gateway_under_test):
    user = User()
    sequencing_type = "whole-exome-sequencing"
    shipping_info = {"shipping": "info"}

    gateway_under_test.add_order(
        user=user, sequencing_type=sequencing_type, shipping_info=shipping_info
    )
    mock_create.assert_called_once_with(
        user=user, sequencing_type=sequencing_type, shipping_info=shipping_info
    )


def test_order_gateway_get_order_by_user_id_returns_null_when_order_not_found(
    gateway_under_test,
):
    user_id = uuid.uuid4()

    response = gateway_under_test.get_order_by_user_id(user_id)

    assert response == []


@mock.patch.object(OrderGateway, "_get_data_form_db")
def test_order_gateway_returns_order_data(_get_data_form_db, gateway_under_test):
    order = DNAKitOrder(id=uuid.uuid4(), user=User(id=uuid.uuid4()))
    _get_data_form_db.return_value = [order]
    user_id = uuid.uuid4()

    response = gateway_under_test.get_order_by_user_id(user_id)

    assert response[0]["id"] == str(order.id)
