from unittest import mock
from core.use_cases.add_order_usecase import AddOrderUsecase


class TestOrders:
    def test_order_api_route_exists(self, test_client):
        response = test_client.post("/order", json={"user_id": "12345", "sequencing_type": "whole-exome-sequencing", "shipping_info": {"shipping": "info"}})
        assert response.status_code == 200

    @mock.patch.object(AddOrderUsecase, "__call__")
    def test_order_api_route_returns_confirmation_of_order_being_sent(self, add_order_mock, test_client):
        add_order_mock.return_value = {"order_id": "12345", "notification_response": {"status": "SMS sent"}}

        response = test_client.post("/order", json={"user_id": "12345", "sequencing_type": "whole-exome-sequencing", "shipping_info": {"shipping": "info"}})

        assert response.json == {"order_id": "12345", "notification_response": {"status": "SMS sent"}}

    @mock.patch.object(AddOrderUsecase, "__call__")
    def test_order_api_route_returns_error_when_data_not_provided(self, add_order_mock, test_client):
        add_order_mock.return_value = {"errors": ["NOT_PROVIDED"]}

        response = test_client.post("/order", json={"user_id": None, "sequencing_type": None, "shipping_info": None})

        assert response.json == {"errors": ["NOT_PROVIDED"]}

    @mock.patch.object(AddOrderUsecase, "__call__")
    def test_order_api_calls_usecase_with_correct_parameters(self, add_order_mock, test_client):
        response = test_client.post("/order", json={"user_id": "4567", "sequencing_type": "whole-exome-sequencing", "shipping_info": {"shipping": "info"}})

        add_order_mock.assert_called_once_with(user_id="4567", sequencing_type="whole-exome-sequencing", shipping_info={"shipping": "info"})