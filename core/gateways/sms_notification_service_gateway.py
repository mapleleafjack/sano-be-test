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
        response = requests.post(self.host, headers={
            "Authorization": f"Bearer {self.bearer}"
        }, json={
            "to": user.phone_number,
            "message": message
        })

        return response