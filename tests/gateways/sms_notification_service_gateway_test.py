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