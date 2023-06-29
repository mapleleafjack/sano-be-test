from unittest import mock
from core.gateways.email_notification_service_gateway import EmailNotificationServiceGateway
from core.models import User
import pytest
import requests

@pytest.fixture
def gateway_under_test():
    return EmailNotificationServiceGateway()

def test_email_notification_service_returns_error_when_parameters_not_provided(gateway_under_test):
    assert gateway_under_test.notify(None, None) == {
        "errors": ["NOT_PROVIDED"]
    }

def test_email_notification_service_returns_error_when_email_not_provided(gateway_under_test):
    user = User(email=None)
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["EMAIL_NOT_PROVIDED"]
    }

@mock.patch.object(requests, "post")
def test_email_notification_service_calls_post_function(mock_post, gateway_under_test):
    user = User(email="test.testington@gmail.com")
    gateway_under_test.notify(user, "message to send")
    mock_post.assert_called_once()


@mock.patch.object(requests, "post")
def test_email_returns_error_when_email_not_sent(mock_post, gateway_under_test):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "status": "error"
    }
    user = User(email="error@gmail.com")
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["EMAIL_NOT_SENT"]
    }

@mock.patch.object(requests, "post")
def test_email_returns_error_when_server_response_not_200(mock_post, gateway_under_test):
    mock_post.return_value.status_code = 500
    user = User(email="error@gmail.com")
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["EMAIL_NOT_SENT"]
    }