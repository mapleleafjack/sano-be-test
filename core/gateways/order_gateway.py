class OrderGateway():
    def add_order(self, user_id, sequencing_type, shipping_info):
        if user_id is None or sequencing_type is None or shipping_info is None:
            return {"errors": ["NOT_PROVIDED"]}

        return {"id": "12345"}