from unittest import mock
from core.gateways.user_gateway import UserGateway
from core.models import User
import pytest


@pytest.fixture
def gateway_under_test():
    return UserGateway()


def test_user_gateway_returns_error_when_data_not_provided(gateway_under_test):
    response = gateway_under_test.add_user(
        name=None, phone_number=None, email=None, address=None
    )
    assert response == {"errors": ["NOT_PROVIDED"]}


@mock.patch.object(User, "create")
def test_user_gateway_adds_user_to_database(create_mock, gateway_under_test):
    create_mock.return_value = User(id="12345")

    response = gateway_under_test.add_user(
        name="John Doe",
        phone_number="123456789",
        email="john.doe@test.it",
        address={
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
        },
    )

    assert response.id == "12345"


@mock.patch.object(User, "select")
def test_user_gateway_gets_all_users_from_database(select_mock, gateway_under_test):
    select_mock.return_value = [
        User(
            id="12345",
            name="John Doe",
            phone_number="123456789",
            email="john.doe@gmail.com",
            address={"some": "address"},
        ),
        User(
            id="123213123",
            name="Jovanni Doe",
            phone_number="1321321321",
            email="john.doe1@gmail.com",
            address={"some": "address"},
        ),
    ]

    response = gateway_under_test.get_all_users()

    assert len(response) == 2


def test_user_gateway_get_by_id_returns_error_when_id_not_provided(gateway_under_test):
    response = gateway_under_test.get_by_id(id=None)
    assert response == {"errors": ["NOT_PROVIDED"]}


@mock.patch.object(User, "get_or_none")
def test_user_gateway_gets_user_by_id_from_database(
    get_or_none_mock, gateway_under_test
):
    get_or_none_mock.return_value = User(
        id="12345",
        name="John Doe",
        phone_number="123456789",
        email="john.doe@gmail.com",
        address={"some": "address"},
    )

    response = gateway_under_test.get_by_id("12345")

    assert response.id == "12345"
    assert response.name == "John Doe"
    assert response.phone_number == "123456789"
    assert response.email == "john.doe@gmail.com"
    assert response.address == {"some": "address"}
