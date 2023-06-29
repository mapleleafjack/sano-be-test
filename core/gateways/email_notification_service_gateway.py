import json
import requests


class EmailNotificationServiceGateway():
    def __init__(self):
        self.host = "https://dev.sanogenetics.com/dev/home-test/email-delivery-service"
        self.bearer = "7lPIazekwQu7Raz7FqBQmsLvlH29IDwG"

    def notify(self, user, message):
        if not user or not message:
            return {"errors": ["NOT_PROVIDED"]}
        
        if not user.email:
            return {"errors": ["EMAIL_NOT_PROVIDED"]}
        
        response = self._send_email(user, message)
        
        return response
    
    def _send_email(self, user, message):
        request_object = {
            "recipient": user.email,
            "message": message
        }

        response = requests.post(self.host, headers={
            "Authorization": f"Bearer {self.bearer}",
            'Content-Type': 'application/json'
        }, data=json.dumps(request_object))
    
        if response.status_code == 200:
            if response.json().get("status") == "success":
                return response.json().get("text")

        return {"errors": ["EMAIL_NOT_SENT"]}