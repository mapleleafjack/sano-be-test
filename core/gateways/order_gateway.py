from core.models import DNAKitOrder


class OrderGateway():
    def add_order(self, user, sequencing_type, shipping_info):
        if user is None or sequencing_type is None or shipping_info is None:
            return {"errors": ["NOT_PROVIDED"]}

        order = DNAKitOrder.create(user=user, sequencing_type=sequencing_type, shipping_info=shipping_info)

        return {"id": order.id}
    
    def get_order_by_user_id(self, user_id):
        if user_id is None:
            return {"errors": ["NOT_PROVIDED"]}

        return DNAKitOrder.get_or_none(user_id=user_id)
        