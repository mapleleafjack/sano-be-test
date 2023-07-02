from core.use_cases.notify_user_usecase import NotifyUserUsecase


class AddOrderUsecase:
    def __init__(
        self,
        order_gateway,
        user_gateway,
        sms_notification_service_gateway,
        email_notification_service_gateway,
    ):
        self.order_gateway = order_gateway
        self.user_gateway = user_gateway
        self.sms_notification_service_gateway = sms_notification_service_gateway
        self.email_notification_service_gateway = email_notification_service_gateway

    def __call__(self, user_id, sequencing_type, shipping_info):
        if user_id is None or sequencing_type is None or shipping_info is None:
            return {"errors": ["NOT_PROVIDED"]}

        user = self.user_gateway.get_by_id(user_id)
        if not user:
            return {"errors": ["USER_NOT_FOUND"]}

        add_order_response = self.order_gateway.add_order(
            user=user, sequencing_type=sequencing_type, shipping_info=shipping_info
        )

        if "errors" in add_order_response:
            return add_order_response

        notify_user_usecase = NotifyUserUsecase(
            sms_notification_service_gateway=self.sms_notification_service_gateway,
            email_notification_service_gateway=self.email_notification_service_gateway,
        )

        notification_response = notify_user_usecase(
            user=user,
            sequencing_type=sequencing_type,
            order_id=add_order_response["id"],
        )

        return {
            "order_id": add_order_response["id"],
            "notification_response": notification_response,
        }
