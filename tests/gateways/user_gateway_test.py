from unittest import mock
from core.gateways.user_gateway import UserGateway
from core.models import User
import pytest

@pytest.fixture
def gateway_under_test():
    return UserGateway()


@mock.patch.object(User, "create")
def test_user_gateway_adds_user_to_database(create_mock, gateway_under_test):
    create_mock.return_value = User(id="12345")

    response = gateway_under_test.add_user(name= "John Doe", phone_number= "123456789", email="john.doe@test.it", address={
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
        })
    
    assert response == {"id": "12345"}
