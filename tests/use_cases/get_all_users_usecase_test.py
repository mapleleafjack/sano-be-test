from unittest import mock
from unittest.mock import MagicMock
import uuid
from core.models import DNAKitOrder, User
from core.use_cases.get_all_users_usecase import GetAllUsersUsecase
import pytest


@pytest.fixture
def user_gateway():
    return MagicMock()


@pytest.fixture
def order_gateway():
    return MagicMock()


@pytest.fixture
def usecase_under_test(user_gateway, order_gateway):
    return GetAllUsersUsecase(user_gateway, order_gateway)


def test_get_all_users_usecase_calls_gateway(usecase_under_test, user_gateway):
    usecase_under_test()

    user_gateway.get_all_users.assert_called_once()


def test_get_all_users_usecase_returns_list_of_users_with_order_information(
    usecase_under_test, user_gateway, order_gateway
):
    user_id = uuid.uuid4()
    user_gateway.get_all_users.return_value = [
        {
            "email": "jack.musajo@gmail.com",
            "phone_number": "07858512504",
            "id": user_id,
            "name": "Chakri Musajo Somma",
            "created_at": "2023-07-02T22:25:42.526744",
        }
    ]

    order_gateway.get_order_by_user_id.return_value = [
        {
            "created_at": "2023-07-02T22:26:37.481275",
            "user": {
                "phone_number": "07858512504",
                "created_at": "2023-07-02T22:25:42.526744",
                "email": "jack.musajo@gmail.com",
                "name": "Chakri Musajo Somma",
                "id": user_id,
            },
            "sequencing_type": "whole-exome-sequencing",
            "shipping_info": {"some": "info"},
            "id": "KLNAuaEtUvGaJTgfCRU9ro",
        }
    ]

    response = usecase_under_test()

    assert "orders" in response[0]
    assert (len(response[0]["orders"])) == 1
