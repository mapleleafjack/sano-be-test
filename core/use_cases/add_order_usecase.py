class AddOrderUsecase():
    def __init__(self, order_gateway, user_gateway):
        self.order_gateway = order_gateway
        self.user_gateway = user_gateway
    
    def __call__(self, user_id, sequencing_type, shipping_info):
        if (user_id is None or sequencing_type is None or shipping_info is None):
            return {"errors": ["NOT_PROVIDED"]}
        
        user = self.user_gateway.get_by_id(user_id)

        if not user:
            return {"errors": ["USER_NOT_FOUND"]}

        return self.order_gateway.add_order(user, sequencing_type, shipping_info)
    