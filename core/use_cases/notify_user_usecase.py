class NotifyUserUsecase:
    def __init__(
        self, sms_notification_service_gateway, email_notification_service_gateway
    ):
        self.sms_notification_service_gateway = sms_notification_service_gateway
        self.email_notification_service_gateway = email_notification_service_gateway

    def __call__(self, user, sequencing_type, order_id):
        if not user or not sequencing_type:
            return {"errors": ["NOT_PROVIDED"]}

        if sequencing_type == "whole-exome-sequencing":
            return self.sms_notification_service_gateway.notify(
                user=user, message=f"Your order #{order_id} has been placed"
            )
        else:
            return self.email_notification_service_gateway.notify(
                user=user, message=f"Your order #{order_id} has been placed"
            )
