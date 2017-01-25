import random

from core.models import Order


class CreateOrderService(object):
    def __init__(self, user, store):
        self.user = user
        self.store = store

    def create(self, order_total):
        order_number = self._generate_order_number()
        order = Order.objects.create(store=self.store,
                                    user=self.user,
                                    external_id=order_number,
                                    total=order_total,
                                    status=Order.STATUS_NEW)
        return order

    def _generate_order_number(self):
        return random.randint(100000, 900000)