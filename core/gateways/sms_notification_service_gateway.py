import json
import requests


class SMSNotificationServiceGateway:
    def __init__(self):
        self.host = "https://dev.sanogenetics.com/dev/home-test/sms-delivery-service"
        self.bearer = "o8deGqg2vTGYXtvIsA05zOW8ywAPBQuB"

    def notify(self, user, message):
        if not user or not message:
            return {"errors": ["NOT_PROVIDED"]}

        if not user.phone_number:
            return {"errors": ["PHONE_NUMBER_NOT_PROVIDED"]}

        return self._send_sms(user, message)

    def _send_sms(self, user, message):
        request_object = {"recipient": user.phone_number, "message": message}

        response = requests.post(
            self.host,
            headers={
                "Authorization": f"Bearer {self.bearer}",
                "Content-Type": "application/json",
            },
            data=json.dumps(request_object),
        )

        if response.status_code == 200:
            if response.json().get("status") == "success":
                return response.json().get("text")

        return {"errors": ["SMS_NOT_SENT"]}
