from core.models import DNAKitOrder
from core.schemas import DNAKitOrderSchema


class OrderGateway:
    def add_order(self, user, sequencing_type, shipping_info):
        if user is None or sequencing_type is None or shipping_info is None:
            return {"errors": ["NOT_PROVIDED"]}

        order = DNAKitOrder.create(
            user=user, sequencing_type=sequencing_type, shipping_info=shipping_info
        )

        return {"id": order.id}

    def get_order_by_user_id(self, user_id):
        if user_id is None:
            return {"errors": ["NOT_PROVIDED"]}

        dna_kit_orders = self._get_data_form_db(user_id)
        dna_kit_order_data = DNAKitOrderSchema().dump(dna_kit_orders, many=True)

        return dna_kit_order_data

    def _get_data_form_db(self, user_id):
        return DNAKitOrder.select().where(DNAKitOrder.user_id == user_id)
