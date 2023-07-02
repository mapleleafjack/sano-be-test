from unittest.mock import MagicMock
from core.use_cases.get_all_users_usecase import GetAllUsersUsecase
import pytest


@pytest.fixture
def add_user_gateway_mock():
    return MagicMock()


@pytest.fixture
def order_gateway_mock():
    return MagicMock()


@pytest.fixture
def usecase_under_test(add_user_gateway_mock, order_gateway_mock):
    return GetAllUsersUsecase(add_user_gateway_mock, order_gateway_mock)


def test_get_all_users_usecase_calls_gateway(usecase_under_test, add_user_gateway_mock):
    usecase_under_test()

    add_user_gateway_mock.get_all_users.assert_called_once()
