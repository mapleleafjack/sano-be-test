class NotifyUserUsecase():
    def __init__(self, sms_notification_service_gateway, email_notification_service_gateway):
        self.sms_notification_service_gateway = sms_notification_service_gateway
        self.email_notification_service_gateway = email_notification_service_gateway

    def __call__(self, user, order):
        if not user or not order:
            return {"errors": ["NOT_PROVIDED"]}
        
        if (order.type == "dna-whole-exome-sequencing"):
            return self.sms_notification_service_gateway.notify(user=user, message=f"Your order #{order.id} has been placed")
        else:
            return self.email_notification_service_gateway.notify(user=user, message=f"Your order #{order.id} has been placed")