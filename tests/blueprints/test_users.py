from unittest import mock
import uuid
from core.models import User
from core.use_cases.add_user_usecase import AddUserUsecase


class TestUsers:
    def test_get_all_users_api(self, test_client):
        response = test_client.get("/users")
        assert response.status_code == 200

    @mock.patch.object(AddUserUsecase, "add_user")
    def test_post_user_returns_error_when_gateway_returns_error(
        self, add_user, test_client
    ):
        add_user.return_value = {"errors": ["SOME_ERROR"]}

        response = test_client.post(
            "/users",
            json={
                "phone_number": "123456789",
                "email": "test.testington@gmail.com",
                "address": {
                    "street": "123 Main Street",
                },
            },
        )

        assert response.status_code == 200
        assert response.json == {"errors": ["SOME_ERROR"]}

    @mock.patch.object(AddUserUsecase, "add_user")
    def test_post_user_calls_usecase_with_correct_params(self, add_user, test_client):
        add_user.return_value = User(id=uuid.uuid4())

        response = test_client.post(
            "/users",
            json={
                "phone_number": "123456789",
                "email": "test.testington@gmail.com",
                "address": {
                    "street": "123 Main Street",
                },
            },
        )

        print(response.json)

        assert response.status_code == 200
        add_user.assert_called_once_with(
            name=None,
            phone_number="123456789",
            email="test.testington@gmail.com",
            address={
                "street": "123 Main Street",
            },
        )

    @mock.patch.object(AddUserUsecase, "add_user")
    def test_post_user_returns_id_of_new_user(self, add_user, test_client):
        add_user.return_value = User(id=1)

        response = test_client.post(
            "/users",
            json={
                "phone_number": "123456789",
                "email": "test.testington@gmail.com",
                "address": {
                    "street": "123 Main Street",
                },
            },
        )

        assert response.status_code == 200
        assert response.json == 1
