from core.gateways.sms_notification_service_gateway import SMSNotificationServiceGateway
from core.models import User
import pytest

@pytest.fixture
def gateway_under_test():
    return SMSNotificationServiceGateway()

def x_test_notification_service_returns_response_from_sms_notification_service(gateway_under_test):
    user = User(phone_number="555-555-5555")

    assert gateway_under_test.notify(user, "message to send") == "SMS sent"