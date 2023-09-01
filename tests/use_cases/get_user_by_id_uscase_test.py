from unittest.mock import MagicMock
from core.models import User
from core.use_cases.get_user_by_id_usecase import GetUserByIdUseCase
import pytest


@pytest.fixture
def add_user_gateway_mock():
    return MagicMock()


@pytest.fixture
def usecase_under_test(add_user_gateway_mock):
    return GetUserByIdUseCase(add_user_gateway_mock)


def test_get_user_by_id_usecase_returns_error_when_no_id_provided(
    usecase_under_test, add_user_gateway_mock
):
    response = usecase_under_test(None)

    assert response == {"errors": ["NOT_PROVIDED"]}


def test_get_user_by_id_usecase_calls_gateway(
    usecase_under_test, add_user_gateway_mock
):
    usecase_under_test("12345")

    add_user_gateway_mock.get_user_by_id.assert_called_once_with("12345")


def test_get_user_by_id_usecase_returns_user(usecase_under_test, add_user_gateway_mock):
    add_user_gateway_mock.get_user_by_id.return_value = User(id="12345")

    response = usecase_under_test("12345")

    assert response.id == "12345"


def test_get_user_by_id_returns_error_when_gateway_returns_error(
    usecase_under_test, add_user_gateway_mock
):
    add_user_gateway_mock.get_user_by_id.return_value = {"errors": ["NOT_FOUND"]}

    response = usecase_under_test("12345")

    assert response == {"errors": ["NOT_FOUND"]}
