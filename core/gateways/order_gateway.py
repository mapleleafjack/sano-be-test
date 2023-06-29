from core.models import DNAKitOrder


class OrderGateway():
    def add_order(self, user, sequencing_type, shipping_info):
        if user is None or sequencing_type is None or shipping_info is None:
            return {"errors": ["NOT_PROVIDED"]}

        order = DNAKitOrder.create(user=user, sequencing_type=sequencing_type, shipping_info=shipping_info)

        return {"id": order.id}