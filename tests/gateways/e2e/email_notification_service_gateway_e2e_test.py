from core.gateways.email_notification_service_gateway import EmailNotificationServiceGateway
from core.gateways.sms_notification_service_gateway import SMSNotificationServiceGateway
from core.models import User
import pytest

@pytest.fixture
def gateway_under_test():
    return EmailNotificationServiceGateway()

def test_notification_service_returns_response_from_email_notification_service(gateway_under_test):
    user = User(email="test.testington@gmail.com")

    assert gateway_under_test.notify(user, "message to send") =="Email sent"