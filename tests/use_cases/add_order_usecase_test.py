from unittest import mock
from unittest.mock import MagicMock
from core.models import User
from core.use_cases.add_order_usecase import AddOrderUsecase
from core.use_cases.notify_user_usecase import NotifyUserUsecase
import pytest


@pytest.fixture
def order_gateway_mock():
    return MagicMock()


@pytest.fixture
def user_gateway_mock():
    return MagicMock()


@pytest.fixture
def send_sms_notification_gateway_mock():
    return MagicMock()


@pytest.fixture
def send_email_notification_gateway_mock():
    return MagicMock()


@pytest.fixture
def use_case_under_test(
    order_gateway_mock,
    user_gateway_mock,
    send_sms_notification_gateway_mock,
    send_email_notification_gateway_mock,
):
    return AddOrderUsecase(
        order_gateway_mock,
        user_gateway_mock,
        send_sms_notification_gateway_mock,
        send_email_notification_gateway_mock,
    )


def test_add_order_usecase_returns_error_when_data_not_provided(use_case_under_test):
    response = use_case_under_test(
        user_id=None, sequencing_type=None, shipping_info=None
    )
    assert response == {"errors": ["NOT_PROVIDED"]}


def test_add_order_usecase_returns_error_when_user_not_found(
    user_gateway_mock, use_case_under_test
):
    user_gateway_mock.get_by_id.return_value = None

    response = use_case_under_test(
        user_id="12345",
        sequencing_type="whole-exome-sequencing",
        shipping_info={"shipping": "info"},
    )
    assert response == {"errors": ["USER_NOT_FOUND"]}


def test_add_order_usecase_returns_error_when_gateway_returns_error(
    order_gateway_mock, use_case_under_test
):
    order_gateway_mock.add_order.return_value = {"errors": ["GATEWAY_ERROR"]}

    response = use_case_under_test(
        user_id="12345",
        sequencing_type="whole-exome-sequencing",
        shipping_info={"shipping": "info"},
    )
    assert response == {"errors": ["GATEWAY_ERROR"]}


@mock.patch.object(NotifyUserUsecase, "__call__")
def test_add_order_usecase_returns_new_order_id(
    notify_user_usecase_mock, order_gateway_mock, use_case_under_test
):
    order_gateway_mock.add_order.return_value = {"id": "12345"}
    notify_user_usecase_mock.return_value = {"status": "SMS sent"}

    response = use_case_under_test(
        user_id="12345",
        sequencing_type="whole-exome-sequencing",
        shipping_info={"shipping": "info"},
    )
    assert response == {
        "order_id": "12345",
        "notification_response": {"status": "SMS sent"},
    }


@mock.patch.object(NotifyUserUsecase, "__call__")
def test_add_order_usecase_calls_notify_user_usecase(
    notify_user_usecase_mock, order_gateway_mock, user_gateway_mock, use_case_under_test
):
    user = User(id="12345")

    order_gateway_mock.add_order.return_value = {"id": "432432"}
    user_gateway_mock.get_by_id.return_value = user
    notify_user_usecase_mock.return_value = "NOTIFICATION_RESPONSE"

    response = use_case_under_test(
        user_id="12345",
        sequencing_type="whole-exome-sequencing",
        shipping_info={"shipping": "info"},
    )
    assert response == {
        "order_id": "432432",
        "notification_response": "NOTIFICATION_RESPONSE",
    }
    notify_user_usecase_mock.assert_called_once_with(
        user=user, sequencing_type="whole-exome-sequencing", order_id="432432"
    )
