from unittest.mock import MagicMock
from core.use_cases.add_user_usecase import AddUserUsecase
import pytest

@pytest.fixture
def add_user_gateway_mock():
    return MagicMock()

@pytest.fixture
def usecase_under_test(add_user_gateway_mock):
    return AddUserUsecase(add_user_gateway_mock)

def test_add_user_usecase_returns_error_if_user_not_provided(usecase_under_test):
    response = usecase_under_test.add_user(name=None, phone_number=None, email=None, address=None)

    assert response == {"errors": ["NOT_PROVIDED"]}

def test_add_user_usecase_returns_error_when_both_phone_number_and_email_are_not_provided(usecase_under_test):
    response = usecase_under_test.add_user(name="John Doe", phone_number=None, email=None, address={
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
        })

    assert response == {"errors": ["NOT_PROVIDED"]}

def test_add_user_usecase_calls_gateway_function(usecase_under_test, add_user_gateway_mock):
    usecase_under_test.add_user(name="John Doe", phone_number="07858512504", email=None, address={
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
        })
    
    add_user_gateway_mock.add_user.assert_called_once()

def test_add_user_usecase_returns_error_when_gateway_returns_error(usecase_under_test, add_user_gateway_mock):
    add_user_gateway_mock.add_user.return_value = {"errors": ["SOME_ERROR"]}
    response = usecase_under_test.add_user(name="John Doe", phone_number="07858512504", email=None, address={
            "street": "123 Main Street",
            "city": "New York",
            "state": "NY",
            "postal_code": "10001",
        })
    
    assert response == {"errors": ["SOME_ERROR"]}