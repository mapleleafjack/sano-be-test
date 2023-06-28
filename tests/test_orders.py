class TestOrders:
    def test_order_api_route_exists(self, test_client):
        response = test_client.post("/order")
        assert response.status_code == 200

    def test_order_api_route_returns_confirmation_of_order_being_sent(self, test_client):
        response = test_client.post("/order")
        assert response.data == b"Order sent successfully"