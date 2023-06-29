class GetAllUsersUsecase():
    def __init__(self, user_gateway, order_gateway):
        self.user_gateway = user_gateway
        self.order_gateway = order_gateway

    def __call__(self):
        user_data = self.user_gateway.get_all_users()

        for user in user_data:
            order = self.order_gateway.get_order_by_user_id(user["id"])
            user["orders"] = order

        return user_data