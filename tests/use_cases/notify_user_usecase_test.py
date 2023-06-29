from unittest.mock import MagicMock
from core.models import DNAKitOrder, User
from core.use_cases.notify_user_usecase import NotifyUserUsecase
import pytest


@pytest.fixture
def sms_notification_service_gateway_mock():
    return MagicMock()

@pytest.fixture
def email_notification_service_gateway_mock():
    return MagicMock()

@pytest.fixture
def usecase_under_test(sms_notification_service_gateway_mock, email_notification_service_gateway_mock):
    return NotifyUserUsecase(sms_notification_service_gateway_mock, email_notification_service_gateway_mock)

def test_usecase_retuns_error_when_user_not_provided(usecase_under_test):
    response = usecase_under_test(user=None, order=None)
    assert response == {
        "errors": ["NOT_PROVIDED"]
    }

def test_usecase_returns_phone_gateway_error_when_sms_gateway_returns_error_when_order_type_is_dna_whole_exome_sequencing(usecase_under_test, sms_notification_service_gateway_mock):
    sms_notification_service_gateway_mock.notify.return_value = {
        "errors": ["SMS_NOT_SENT"]
    }
    response = usecase_under_test(user=User(), order=DNAKitOrder(type="dna-whole-exome-sequencing"))
    assert response == {
        "errors": ["SMS_NOT_SENT"]
    }

def test_usecase_returns_email_gateway_error_when_email_gateway_returns_error_when_order_type_is_not_dna_whole_exome_sequencing(usecase_under_test, email_notification_service_gateway_mock):
    email_notification_service_gateway_mock.notify.return_value = {
        "errors": ["EMAIL_NOT_SENT"]
    }
    response = usecase_under_test(user=User(), order=DNAKitOrder(type="dna-whole-genome-sequencing"))
    assert response == {
        "errors": ["EMAIL_NOT_SENT"]
    }

def test_usecase_returns_sms_gateway_response_when_order_type_is_dna_whole_exome_sequencing(usecase_under_test, sms_notification_service_gateway_mock):
    sms_notification_service_gateway_mock.notify.return_value = {
        "status": "SMS sent"
    }
    response = usecase_under_test(user=User(), order=DNAKitOrder(type="dna-whole-exome-sequencing"))
    assert response == {
        "status": "SMS sent"
    }

def test_usecase_returns_email_gateway_response_when_order_type_is_not_dna_whole_exome_sequencing(usecase_under_test, email_notification_service_gateway_mock):
    email_notification_service_gateway_mock.notify.return_value = {
        "status": "Email sent"
    }
    response = usecase_under_test(user=User(), order=DNAKitOrder(type="dna-whole-genome-sequencing"))
    assert response == {
        "status": "Email sent"
    }