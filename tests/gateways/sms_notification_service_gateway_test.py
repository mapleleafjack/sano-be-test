from unittest import mock
from core.gateways.sms_notification_service_gateway import SMSNotificationServiceGateway
from core.models import User
import pytest
import requests

@pytest.fixture
def gateway_under_test():
    return SMSNotificationServiceGateway()

def test_notification_service_returns_error_when_parameters_not_provided(gateway_under_test):
    assert gateway_under_test.notify(None, None) == {
        "errors": ["NOT_PROVIDED"]
    }
    
def test_notification_service_returns_error_when_phone_number_not_provided(gateway_under_test):
    user = User(phone_number=None)
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["PHONE_NUMBER_NOT_PROVIDED"]
    }

@mock.patch.object(requests, "post")
def test_notification_service_calls_post_function(mock_post, gateway_under_test):
    user = User(phone_number="123456789")
    gateway_under_test.notify(user, "message to send")
    mock_post.assert_called_once()


@mock.patch.object(requests, "post")
def test_sms_returns_error_when_sms_not_sent(mock_post, gateway_under_test):
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "status": "error"
    }
    user = User(phone_number="123456789")
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["SMS_NOT_SENT"]
    }

@mock.patch.object(requests, "post")
def test_sms_returns_error_when_server_response_not_200(mock_post, gateway_under_test):
    mock_post.return_value.status_code = 500
    user = User(phone_number="123456789")
    assert gateway_under_test.notify(user, "message to send") == {
        "errors": ["SMS_NOT_SENT"]
    }