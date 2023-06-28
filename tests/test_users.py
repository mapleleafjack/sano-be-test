class TestUsers:
    def test_get_all_users_api(self, test_client):
        response = test_client.get("/users")
        assert response.status_code == 200
