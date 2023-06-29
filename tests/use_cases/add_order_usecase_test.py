from unittest.mock import MagicMock
from core.use_cases.add_order_usecase import AddOrderUsecase
import pytest

@pytest.fixture
def order_gateway_mock():
    return MagicMock()

@pytest.fixture
def user_gateway_mock():
    return MagicMock()

@pytest.fixture
def use_case_under_test(order_gateway_mock, user_gateway_mock):
    return AddOrderUsecase(order_gateway_mock, user_gateway_mock)

def test_add_order_usecase_returns_error_when_data_not_provided(use_case_under_test):
    response = use_case_under_test(user_id=None, sequencing_type=None, shipping_info=None)
    assert response == {
        "errors": ["NOT_PROVIDED"]
    }

def test_add_order_usecase_returns_error_when_user_not_found(user_gateway_mock, use_case_under_test):
    user_gateway_mock.get_by_id.return_value = None

    response = use_case_under_test(user_id="12345", sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "errors": ["USER_NOT_FOUND"]
    }

def test_add_order_usecase_returns_error_when_gateway_returns_error(order_gateway_mock, use_case_under_test):
    order_gateway_mock.add_order.return_value = {"errors": ["GATEWAY_ERROR"]}

    response = use_case_under_test(user_id="12345", sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "errors": ["GATEWAY_ERROR"]
    }

def test_add_order_usecase_returns_new_order_id(order_gateway_mock, use_case_under_test):
    order_gateway_mock.add_order.return_value = {"id": "12345"}

    response = use_case_under_test(user_id="12345", sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})
    assert response == {
        "id": "12345"
    }